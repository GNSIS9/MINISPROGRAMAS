# -*- coding: utf-8 -*-
frase = input("Ingrese una frase: ")
frase = frase.lower().replace(" ", "")
es_palindromo = frase == frase[::-1]
print("La frase es un palíndromo." if es_palindromo else "La frase no es un palíndromo.")


