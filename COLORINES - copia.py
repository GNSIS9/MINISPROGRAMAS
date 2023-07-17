# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:16:39 2023

@author: Alumno
"""

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

interseccion = conjunto1.intersection(conjunto2)

print("Conjunto 1:", end=" ")
for elemento in conjunto1:
    if elemento in interseccion:
        print("\033[1;31m" + str(elemento) + "\033[0m", end=" ")  # Imprimir en rojo los elementos de la intersección
    else:
        print(elemento, end=" ")
print()

print("Conjunto 2:", end=" ")
for elemento in conjunto2:
    if elemento in interseccion:
        print("\033[1;31m" + str(elemento) + "\033[0m", end=" ")  # Imprimir en rojo los elementos de la intersección
    else:
        print(elemento, end=" ")
print()

print("Intersección:", end=" ")
for elemento in interseccion:
    print("\033[1;31m" + str(elemento) + "\033[0m", end=" ")  # Imprimir en rojo los elementos de la intersección
print()