#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:48:53 2020

@author: fabri
"""

import numpy as np
from scipy.signal import square, sawtooth, chirp
import numpy as np


def generador2021(t, fs, amplitud=1, DC=0, t1=1, f0=1, f1=100, frecuencia=1, fase=0, duty=0.5, width=1,
              primercorte=0.5, ancho=0.25, tipo=1):

    """
    Descripción de la función:
    Parámetros de entrada
    amplitud:     Amplitud de la señal periódica
    frecuencia:   Frecuencia de Sinusoide, Cuadrada o Diente de Sierra
    fase:         Fase de la función sinusoidal
    duty:         Duty Cycle para la Señal Cuadrada en porcentaje
    width:        Fracción entre 0 y 1, es donde ocurre el máximo de
                    la Diente de Sierra
    primercorte:  Primer corte del Sinc
    ancho:        Para los pulsos rectangulares y triangulares
    DC:           Nivel DC para las señales periódicas
    tipo:         Señal a ser generada.
                  Si Tipo=1,2,3,4,5 o 6 se generará
                      Cos, Cuadrada, Diente (periódicas), Sinc, Pulso Rec o
                      Pulso Triang (No periódicas) respectivamente.
    Parámetro de salida:
    y:            señal generada
    """
    
    if tipo > 11 or tipo < 0:
        print('ERROR: el valor de Tipo debe estar entre 1 y 11')

    else:
        # Esto es un diccionario, se usa para crear una estructura equivalente 
        # al switch de matlab
        tipos_signal = {1 : coseno(t, frecuencia, fase, duty, width,
                                   primercorte, ancho, tipo),
                        2 : cuadrada(t, frecuencia, fase, duty, width,
                                     primercorte, ancho, tipo),
                        3 : dte_sierra(t, frecuencia, fase, duty, width,
                                       primercorte, ancho, tipo),
                        4 : funcion_sinc(t, frecuencia, fase, duty, width,
                                         primercorte, ancho, tipo),
                        5 : pulso_rec(t, fs, ancho),
                        6 : pulso_tri(t, fs, ancho),
                        7 : señal_chirp(t, f0, t1, f1),
                        8 : esc(fs),
                        9 : sign(fs),
                        10 : np.exp(-t),
                        11 : np.exp(-abs(t)) 
                        
                      
                        }
        
        
        y = amplitud * tipos_signal[tipo] + DC
        
        return y
    
def coseno(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return np.cos(2 * np.pi * frecuencia * t + fase)

def cuadrada(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return square(2 * np.pi * frecuencia * t + fase)

def dte_sierra(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return sawtooth(2 * np.pi * frecuencia * t, width)

def funcion_sinc(t, frecuencia, fase, duty, width,
              primercorte, ancho, tipo):
    return np.sinc(t / primercorte)

def pulso_rec(t, fs, ancho):
    # se genera manualmente
   
    y = np.zeros(t.size)
    inicio = int(0.5*t.size) -int(ancho*fs/2) 
    fin = int(0.5*t.size) + int(ancho*fs/2)
    y[inicio:fin] = 1
    return y
    
def pulso_tri(t, fs, ancho):
    # el pulso triangular se genera convolucionando 2 rectangulares
    y = np.zeros(t.size//2 + 1)
    inicio = int(0.5*y.size) - int(ancho*fs/2) 
    fin = int(0.5*y.size) + int(ancho*fs/2)
    y[inicio:fin] = 1
    y = np.convolve(y,y)
    if y.size > t.size:
        y = y[:-1]  # quito una muestra para coincidir la longitud con t
    return y / np.max(y)

def señal_chirp(t,f0,t1,f1):
    return chirp(t,f0,t1,f1,'linear')

def esc(fs):
    return np.concatenate((np.zeros(2*fs),np.ones(2*fs)))

def sign(fs):
    return np.concatenate((-1*np.ones(2*fs),np.ones(2*fs)))



   
        