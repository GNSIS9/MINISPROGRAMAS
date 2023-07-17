# -*- coding: utf-8 -*-
import math

def super_funcion(lista):
    #calcula el minimo
    a = min(lista)
    #calcula el maximo
    b = max(lista)
    #calcula la suma total
    c = sum(lista)
    #calcula el promedio de la lista
    d = 0
    for i in lista:
        d += i 
    promedio = d / len(lista)
    
    # Calcula la desviación estándar
    media = sum(lista) / len(lista)
    suma = 0
    for i in lista:
        suma += (i - media) ** 2
    desviacion = math.sqrt(suma / len(lista))

    #usamos el corchete, porque creamos un diccionario
    respuesta = {
        "el minimo": a,
        "el maximo": b,
        "la suma": c,
        "el promedio": promedio,
        "la desviacion": desviacion
    }
    
    return respuesta
    
lista = [8, 24, 1, 7]
resultado = super_funcion(lista)
print(resultado)

 