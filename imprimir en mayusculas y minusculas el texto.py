# -*- coding: utf-8 -*-
texto = input("Ingrese un texto: ")

resultado = ''.join(map(lambda c, i: c.upper() if i % 2 == 0 else c.lower(), texto, range(len(texto))))

print("El resultado es:", resultado)

