# -*- coding: utf-8 -*-
cadena1 = "Hola"
cadena2 = "Hola  mundo  feliz  "

if cadena1 in cadena2:
    print("La cadena1 está presente en cadena2.")

cadena2 = cadena2.replace("  ", " ")
print(cadena2)
