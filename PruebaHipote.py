# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:20:10 2018

@author: Felipe Arango 
"""
import math 

"""
==============================================================================
== PRUEBA E HIPOTESIS 
==============================================================================
"""

"""
===============================================
== Prueba para m >= 30 y pi 
===============================================
"""
def peh(n, x, s, u):
    sSn = s/(math.sqrt(n))
    xMu = x-u
    return xMu/sSn

#hallar p una cola (recibe z tabla in)
def hallaPUC(zT):
    return (0.5 - zT)

#hallar p dos colas (recibe z tabla in)
def hallaDC(zT):
    return (0.5 - zT)*2   