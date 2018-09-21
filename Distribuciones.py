# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:34:08 2018

@author: HP
"""

import math
from functools import reduce


"""
===========================================================
== VARIABLES 
===========================================================
"""

e = 2.71828

"""
==============================================================================
== DISTRIBUCIONES DE PROBABILIDAD
==============================================================================
"""

"""
===========================================================
== DISTRIBUCIÓN BINOMIAL
===========================================================

#pi = exito
1- pi es la probabilidad de fracaso
n es el tamaño de la muestra
x es el valor al que se desea encontrar la probabilidad
"""
def dstBinomial(n,x,pi):
    difXN =n-x #(n-x)
    pF = factorial(n)/(factorial(x)*factorial(difXN))  
    piX = pi**x  #pi elevado a x
    difPi = (1-pi)**difXN # (1-pi)
    x =  pF*(piX*difPi) #(n!/x!(x-n)!*pi**x*(1-pi)**n-x)
    return x

"""
===========================================================
== DISTRIBUCIÓN  HIPERGEOMETRICA 
===========================================================

nt = N es el tamaño de la población 
r = es el número de éxitos en la población 
nm = n es el tamaño de la muestra
x es el número de éxitos en la muestra 
"""

def dstHipergeometrica(nt, r, nm, x):
    c1 = combinaciones(r,x)#rCx
    difNr = nt-r #N-r
    difnx = nm-x #n-x
    c2 = combinaciones(difNr,difnx) #N-r C n-x
    c3 = combinaciones(nt, nm) #NCn
    result = (c1*c2)/c3
    return result


"""
===========================================================
== DISTRIBUCIÓN POISSON
===========================================================
 
x = es el número de veces que ocurre el evento 
u = miu el número promedio de ocurrencias por unidad de tiempo o de espacio
e = número euler:2.71828, la base logaritmo natural 
"""

def dstPoisson(x, u):    
    return ((u**x)*(e**-u))/(factorial(x))


"""
===========================================================
== DISTRIBUCIÓN EXPONENCIAL
===========================================================

t es el lapso de tiempo
u = miu es la tasa promedio de ocurrencia
e = número euler:2.71828, la base logaritmo natural 
"""
def dstExponencial(t, u):
    exp= -u*t
    return 1-e**exp


"""
===========================================================
== DISTRIBUCIÓN UNIFORME
===========================================================

u = miu : E(X)= a+b/2
oC = sigma cuadrado: (b-a)**2/12
o = sqrt(oC)
"""

def dstUniforme(x1, x2, rango1, rango2):
    rango = (rango2-rango1)
    return (x2-x1)/rango 

"""
===========================================================
== DISTRIBUCIÓN NORMAL
===========================================================

Z es la desviación normal
X es algún valor especifíco de la variable aleatoria.
u = miu es la media
o = Sigma es la desviación estándar
"""

def dstNormal(x, u, o):
    return (x-u)/o

"""
==========================================================
== DISTRIBUCIÓN NORMAL CUANDO DAN Z                     ==
==========================================================
"""

def dstNormalCZ(z, u, o):
    return (z*o)+u

"""
==========================================================
== DISTRIBUCIÓN NORMAL A LA DISTRIBUCION BINOMIAL       ==
==========================================================

x: algún valor especifico 
n: cantidad
pi: porcentaje 
"""

def dstNormalToBin(x, n, pi):
    u= n*pi
    o= math.sqrt(n*pi*(1-pi))
    return u, o

"""
==============================================================================
== DISTRIBUCIONES MUESTRALES 
==============================================================================
"""


"""
======================================
== METODOS Y FUNCIONES
======================================
"""
# retorna el factorial de n número 
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def toPorcent(n):
    return n * 100

# retorna las combinaciones posibles de dos numeros
def combinaciones(m, n):        
    return factorial(m) // (factorial(n) * factorial(m - n))