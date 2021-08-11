#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NOTA: en Python, a diferencia de matlab, uno no necesita crear un archivo 
aparte para construir una función. No obstante, en este caso lo hacemos así,
para facilitar su reutilización.

La estructura de las funciones es del tipo:
    
def mi_funcion(param1, param2, param3):
    .
    .
    (código que va a ejecutar la función)
    .
    .
    return resul1, resul2
    
mi_funcion es una funcion que recibe tres parámetros y devuelve dos valores
    
Luego hago un llamado a esa función para ejecutarla:

r1, r2 = mi_funcion(param1 = a, param2 = b, param3 = c)

A continuación creamos una función que grafica una fft a partir de una señal x

"""

import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def graficar_fft(x, fs, N='default', objeto_ax=None, title='', log=False):
    
    """
    Funcion que calcula la transformada de Fourier de x
    y grafica su modulo y fase (el eje x muestra los valores de frecuencia)
    
    Parámetros:
            
            x: es la señal a la que se le desea hallar la fft
            
            fs: es la frecuencia de muestreo de la senal original

            objeto_ax (opcional): es una instancia de un contenedor gráfico para poder
                graficar subplots.
            
            N (opcional): es el numero de puntos de la fft, debe ser una potencia de 2,
                de no ser asi, el algoritmo corrige tal que N es la proxima 
                potencia de 2 mas cercana al N proporcionado por el usuario

            title (opcional): texto para incluir como titulo del gráfico

            log (opcional): recibe un valor booleano, por defecto toma un valor False y 
                el gráfico generado es lineal, usando True como valor el argumento se 
                puede hacer un gráfico logarítmico.
            
    Retorna:
        
            MX: contiene la Transformada de Fourier

    """

    # Coloca los valores por default para N
    if N == 'default':
        N = proxima_potencia_de_2(np.size(x))
        print('muestras:', N)
        
    # Calcula la fft, haciendo zero padding
    X = fft(x,N)
    lim = int(np.ceil((N+1)/2) - 1)
    X = np.append(X[lim:1:-1], X[0:lim])  # Se corrige el espectro para ver 
                                                 # el nivel DC en el origen

    MX = np.abs(X)  # Se busca el modulo de X
    MX = MX / np.size(MX)  # Se escala para que la magnitud no sea funcion del tamano del vector x
    
    f =np.linspace((-N/2), (N/2), N-1) * fs/N  # Se genera el eje de frecuencias
    
    if objeto_ax == None:
        figura, objeto_ax = plt.subplots()  # Se grafica el modulo              
        
    if log:
        f = f[f >= 20]
        objeto_ax.loglog(f, MX[-f.size:])
        objeto_ax.set_xticks([63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000])
        objeto_ax.get_xaxis().set_major_formatter(ticker.ScalarFormatter())

    else:
        objeto_ax.plot(f,MX)
        
    objeto_ax.grid(which='both')
    objeto_ax.set_xlabel('frecuencia [Hz]')
    objeto_ax.set_ylabel('amplitud')
    objeto_ax.set_title(title)
            
    return MX

# funcion accesoria para calcular la potencia de 2 mas cercana a un numero
def proxima_potencia_de_2(numero):
    if numero > 1:
        for i in range(1, int(numero)):
            if (2 ** i >= numero):
                return 2 ** i
    else:
        print('Ingrese un número mayor o igual a 2')