
#RANDOM proporciona varias funciones relacionadas 
#con la generación de números aleatorios
import random

#cadena es igual a string (cadena de caracteres)
#y el input es para que el programa interactue con la persona.
cadena1 = input("Introduce una palabra:")
cadena2 = input("Introduce otra palabra:")

aleat = random.random()

if aleat <= 0.5:
    resultado = cadena1 + " " + cadena2
   
else:
    respuesta = cadena1 + " " + cadena2
  

print("tus palabras fueron:", respuesta)

