# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 18:20:15 2023

@author: Alumno
"""

def gorrito(x):
    return "^" + x

x = ["ana", "maria", "bernal"]
resultado = map(gorrito, x)
lista_con_gorrito = list(resultado)

print(lista_con_gorrito)


