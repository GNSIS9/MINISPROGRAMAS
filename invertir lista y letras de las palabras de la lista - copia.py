
Lista = ["Azulejo", "Bondad", "Entusiasmo", "Plenitud"]
L = Lista[::-1]
print(L)

# Creamos una nueva lista para almacenar las palabras invertidas en el orden de las letras
lista_letras_invertidas = []

# Recorremos cada palabra invertida en la lista L
for palabra in L:
    # Invertimos el orden de las letras de la palabra y la agregamos a la lista de letras invertidas
    letras_invertidas = palabra[::-1]
    lista_letras_invertidas.append(letras_invertidas)

print(lista_letras_invertidas)
