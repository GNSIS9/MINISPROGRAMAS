
Lista = ["Azulejo", "Bondad", "Entusiasmo", "Plenitud"]

# Creamos una nueva lista para almacenar las palabras invertidas
lista_invertida = []

# Recorremos cada palabra en la lista original
for palabra in Lista:
    # Invertimos el orden de las letras de la palabra y la agregamos a la lista invertida
    palabra_invertida = palabra[::-1]
    lista_invertida.append(palabra_invertida)

print(lista_invertida)
