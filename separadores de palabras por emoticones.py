# -*- coding: utf-8 -*-

import random

texto = input("Ingrese un texto: ")
separadores = ["😁", "😊", "😃", "😉", "😎", "😍", "🥳", "🤩", "🔥",  "🌈", "🎉", "🎊"]  # Lista de separadores posibles
palabras = texto.split()

resultado = ' '.join([palabra + random.choice(separadores) for palabra in palabras])[:-len(random.choice(separadores))]

print("El resultado es:", resultado)
