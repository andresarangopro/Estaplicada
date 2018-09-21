# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 09:56:23 vv

@author: HP
"""
import math 
"""
==============================================================================
== INTERVALOS 
==============================================================================
"""

"""
===========================================================
==          INTERVALO DE CONFIANZA PARA ESTIMAR MIU      ==
==                  CON DISTRIBUCION NORMAL  > 30        ==
===========================================================
estimar miu = u
o: sigma Conocida desviacion
z: tabla Z
xB: media 
"""
def estimarMiuNormal(xB, z, oX, n):
    sup = xB + (z*(oX/math.sqrt(n)))
    inf = xB - (z*(oX/math.sqrt(n)))
    
    return inf, sup;

"""
===========================================================
==          INTERVALO DE CONFIANZA PARA ESTIMAR MIU      ==
==                  CON DISTRIBUCION T  > 30             ==
===========================================================
z: grados de libertad n-1 t 
"""

def estimarMiuT(xB, z, oX, n):
    sup = xB + (z*(oX/math.sqrt(n)))
    inf = xB - (z*(oX/math.sqrt(n)))
    
    return inf, sup;

"""
===========================================================
==          INTERVALO DE CONFIANZA PARA ESTIMAR (PI)     ==
==                  LA PROPORCIÓN POBLACIONAL            ==
===========================================================
"""

#retorna el valor p 
def calcP(n1,n2):
    return n2/n1

def estimarProporcion(p, z, n):
    sP = math.sqrt((p*(1-p))/n)
    sup = p +z*sP
    inf = p - z*sP
    
    return inf, sup, sP;

"""
===========================================================
==          INTERVALO DE CONFIANZA PARA HALLAR N         ==
==               EL TAMAÑO DE LA MUESTRA PARA ESTIMAR U  ==
===========================================================

Z nivel de cinfianza poblacional
o^2 : sigma cuadrada es la varianza poblacional
xB - u : es el error tolerable 
"""
def calcularTamNU(z, o, e):
    z2 = z**2
    o2 = o**2
    e2 = e**2
    return  (z2*o2)/e2

"""
===========================================================
==          INTERVALO DE CONFIANZA PARA HALLAR PI        ==
==     EL TAMAÑO DE LA MUESTRA PARA ESTIMAR POBLACIÓN    ==
===========================================================
"""

def calcularPr(z, p, pi):
    z2 = z**2
    piX = pi*(1-pi)
    p2 =(p**2)
    return  (z2*piX)/p2