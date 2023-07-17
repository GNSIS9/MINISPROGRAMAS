#creamos dos tuplas, recordando que trabajan con listas
C1 = set([4, 3, 7])
C2 = set([2, 5, 4])
#Definicion de la funcion, para ejecutar la interseccion
def interseccion (c1, c2) :
    #definimos, lo que nos va a devolver la funcion
    return  C1.intersection(C2)
#definimos una variable, con el valor de la funcion
x = interseccion(C1, C2)
#imprimimos la variable
print(x)
