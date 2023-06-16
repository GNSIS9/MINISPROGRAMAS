# -*- coding: utf-8 -*-
texto = input("Ingrese un texto: ")
resultado = ""

alternar_mayusculas = True

for caracter in texto:
    if alternar_mayusculas:
        resultado += caracter.upper()
    else:
        resultado += caracter.lower()
    alternar_mayusculas = not alternar_mayusculas

print("El resultado es:", resultado)