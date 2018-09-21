# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 22:43:51 2018

@author: Felipp
95: 1.96
90:1.64
99:2.58
"""

from Distribuciones import *
from Intervalos import *
from PruebaHipote import *
"""
===============================================
== Ejercicios Distribuciones de probabilidad
===============================================
"""
#1 Binomial
#print(toPorcent(dstBinomial(10,8,0.6)))
#1 .b
#print(toPorcent(dstBinomial(10,7,0.6) - dstBinomial(10,3,0.6)))// grande duda

#2Hipergeometrica
#print(dstHipergeometrica(20,8,3,1)) 

#3 Poisson
#print(toPorcent(dstPoisson(4,5.2)))

#4 Exponencial
#print(dstExponencial(2,8))

#5 Uniforme
#print (dstUniforme(12.7,14.5,10.2,18.3))

#6 Distribución normal 
#print(dstNormal(70.5,67,2),dstNormal(69.3,67,2))
#print(dstNormal(3.3,2.2,0.8))
#print(dstNormal(2.7,2.2,0.8), dstNormal(3,2.2,0.8))
#print(dstNormal(9.5,6,1.897), dstNormal(10.5,6,1.897))

#7 Distribucion normal a la distribucion binomial 
#uO = dstNormalToBin(72,150,0.45)
#o = uO[0]
#u = uO[1]

#print(dstNormal(71.5,u,o), dstNormal(72.5,u,o))

"""
===============================================
== QUIZ
===============================================
"""

#print(dstBinomial(10,4,0.6)*100)
#print(dstHipergeometrica(15,12,8,5)*100)
#print(dstPoisson(4,5)*100)
#print(dstExponencial(2,3))
#print(dstUniforme(15.8,16.5,13.9,18.1))
#print(dstNormal(34.8,36,1.9))
#print(dstNormal(16.27,16.1,1.2))


"""
===============================================
== EJERCICIOS INTERVALOS DE CONFIANZA
===============================================
"""

#print(estimarMiuNormal(35500,1.96, 7200,100))
#oX = hallaOConS(217.43,50)
#print(oX ,estimarMiuNormal(652.68,2.58, 217.43, 50))
#print(estimarMiuT(1275,2.201,235,12))
#print(estimarMiuT(102,1.729,8.5,20))
#p = calcP(500,275)
#print(estimarProporcion(p,1.64,500))
#p = calcP(1020,673)
#print(estimarProporcion(p,2.58,1020))
#print(calcularTamNU(1.96,6,2))
#print(calcularTamNU(2.58,3.5,1))
#print(calcularPr(1.96,0.01,0.5))
#print(calcularPr(1.96,0.02,0.5))
#print(calcularTamNU(2.58,165,50))
#print(calcularPr(2.58,0.1,0.5))
#1
#print(estimarMiuNormal(54.98,1.75,12.7,70))
#print(estimarMiuT(2365,2.861,983,20))
#p = calcP(1098,896)
#print(estimarProporcion(p,2.58,1098))
#print(calcularTamNU(1.96,750,100))
#print(calcularPr(1.96,0.03,0.5))


"""
===============================================
== EJERCICIOS PRUEBA E HIPOTESIS 
===============================================
"""

print(peh(200,298.10,97.30,312))
print(peh(64,2251,812,2100))

print(peh(150,201.3,45.5,212))