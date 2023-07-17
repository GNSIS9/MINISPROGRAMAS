
lista = [('a', 80), ('b', 7), ('c', 4)]

# Encontrar el elemento máximo de la lista
maximo = max(lista, key=lambda x: x[1]) 

# Encontrar el elemento mínimo de la lista
minimo = min(lista, key=lambda x: x[1])

# Imprimir el elemento máximo
print(maximo)

# Imprimir el elemento mínimo
print(minimo)
