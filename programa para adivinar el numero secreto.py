# -*- coding: utf-8 -*-
import random

numero_secreto = random.randint(1, 100)
intentos = 0
numero = input("ingresa un numero: ")
while True: 
    intentos +=1
    x = int (input("Intentalo de nuevo: "))
    if x < numero_secreto:
        print("buen intento, vuelve a intentarlo con un numero mayor: ")
    elif x > numero_secreto:
        print("Intenta con un numero menor: ")
    else: 
        print(f"Felicidades!!!! los has conseguido en {intentos} intentos")
        break
        
    