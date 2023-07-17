
#Se define una lista llamada "lista" que contiene varias palabras.
lista  = ["Alexa", "Paraguas", "Escoba", "Pizza", "Rama", "Enciclopedia", "Numerologia"]

#Se solicita al usuario que ingrese un número utilizando la función input(). 
#El valor ingresado se convierte a entero utilizando la función int() y se guarda en la variable "x".
x= int (input ("introduce un numero, el que mas te guste: "))

#Se utiliza un bucle for para recorrer cada palabra en la lista.
for palabra in lista:
#Dentro del bucle, se verifica si la longitud de la palabra (len(palabra))
#es mayor que el número ingresado por el usuario.
    if len(palabra) > x:
#Si la condición se cumple, se ejecuta el bloque de código dentro del if y se imprime la palabra en la consola.
        print(palabra)