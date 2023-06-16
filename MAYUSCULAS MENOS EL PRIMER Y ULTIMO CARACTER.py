# -*- coding: utf-8 -*-
cadena1 = input("Introduce una palabra: ")
mayusculas = cadena1[0] + cadena1[1:-1].upper() + cadena1[-1]
print("La palabra en mayúsculas, excepto el primer y último caracter, es:", mayusculas)

#cadena1[0] equivale al primer caracter
#cadena1[1:-1] equivale a crear una subcadena, excepto el primer y ultimo caractery le sumamos
# upper() que nos sirve para poner las cadenas de caracteres en mayusculas.
#cadena1[-1] equivale al ultimo caracter
