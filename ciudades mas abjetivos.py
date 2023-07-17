# -*- coding: utf-8 -*-
lista= [1,2,3,4,5] 
def cuadrado(numero):
    return numero*numero
l = []
for e in lista:
    l.append(cuadrado(e))
    
print(l)