# -*- coding: utf-8 -*-

def max_min(lista):
    
    maximo = max(lista)
    minimo = min(lista)
    
    resultado1 = {
    "maximo" : maximo,
    "minimo" : minimo        
    }
    return resultado1 

def sumatotal(lista):
    
    suma = sum(lista)
    
    return suma 

lista = [8, 24, 1, 7]

resultado1= max_min(lista)
print(resultado1)

resultado2= sum(lista)
print(resultado2)
    