#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:57:20 2021

@author: fabricio.chungo
"""

import numpy as np
from manipulacion import desplaza, girodesplaza, desplazagiro
import matplotlib.pyplot as plt

T = 0.01
fs = 1/T
t = np.arange(-2,2+T,T)

x1 = np.exp(t)
x2 = np.sin(t)


def sistema_1(x):
    salida = 3*x + 5
    return salida

def sistema_2(x, fs):
    salida = girodesplaza(x, fs, 0.25, 1)
    return salida

def sistema_3(x, t):
    salida = (t - 1) * x
    return salida

def sistema_4(x):
    salida = x ** 2
    return salida

# y1 = sistema_1(x1)
# y2 = sistema_1(x2)

y1 = sistema_2(x1, fs)
y2 = sistema_2(x2, fs)
y_sumar_salidas = y1 + y2
y_sumar_entradas = sistema_2(x1 + x2, fs)

# y1 = sistema_1(x1)
# y2 = sistema_1(x2)

# y1 = sistema_1(x1)
# y2 = sistema_1(x2)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, x1)
ax2.plot(t, y1)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, x2)
ax2.plot(t, y2)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, y_sumar_entradas)
ax2.plot(t, y_sumar_salidas)

#%%

superposicion = False
resultado = False

y_sumar_entradas = sistema_2(x1 + x2, fs)
y_sumar_salidas = y1 + y2

if (y_sumar_entradas == y_sumar_salidas).all():
    superposicion = True

if superposicion:
    resultado = True
    mensaje = 'Se cumple superposición'
else:
    mensaje = 'No se cumple superposición'
    
print(mensaje)

#%%

# def linealidad (x1, x2, y1, y2, a, funcion):
    
#     homogeneidad = False
#     superposicion = False
     
#     a_x1 = a*x1
#     y_multiplicar_entrada = funcion(a_x1)
#     y_multiplicar_salida = a*y1
        
#     if (y_multiplicar_entrada == y_multiplicar_salida).all():
#         homogeneidad = True
    
#     y_sumar_entradas = sistema_1(x1 + x2)
#     y_sumar_salidas = y1 + y2
    
#     if (y_sumar_entradas == y_sumar_salidas).all():
#         superposicion = True
    
#     if homogeneidad and superposicion:
#         resultado = True
#         mensaje = 'El sistema es lineal'
#     else:
#         mensaje = 'El sistema no es lineal'
    
#     return resultado

#%%

def pulso_rec(t, fs, ANCHO):
    y = np.zeros(t.size)
    inicio = int(0.5*t.size) -int(ANCHO*fs/2)
    fin = int(0.5*t.size) + int(ANCHO*fs/2)
    y[inicio:fin] = 1
    return y

xpuls = pulso_rec(t, fs, 0.25)
plt.plot(t, xpuls)

xpuls_desp = desplaza(xpuls, fs, 0.5)
plt.plot(t, xpuls_desp)