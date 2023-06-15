# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 19:38:07 2023

@author: Alumno
"""

cadena = input("Introduce una cadena de caracteres: ")
ultimos_caracteres = cadena[-6:].upper()
resultado = cadena[:-6] + ultimos_caracteres
print("La cadena con los últimos caracteres en mayúsculas es:", resultado)