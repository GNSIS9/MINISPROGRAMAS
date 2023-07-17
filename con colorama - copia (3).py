
from colorama import Fore, Style

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

interseccion = conjunto1.intersection(conjunto2)

color_conjunto1 = Fore.BLUE + Style.BRIGHT  
color_conjunto2 = Fore.RED + Style.BRIGHT  
color_interseccion = Fore.GREEN + Style.BRIGHT  
color_normal = Style.RESET_ALL  

print("Conjunto 1:", end=" ")
for elemento in conjunto1:
    if elemento in interseccion:
        print(f"{color_interseccion}{elemento}{color_normal}", end=" ")
    else:
        print(f"{color_conjunto1}{elemento}{color_normal}", end=" ")

print("\nConjunto 2:", end=" ")
for elemento in conjunto2:
    if elemento in interseccion:
        print(f"{color_interseccion}{elemento}{color_normal}", end=" ")
    else:
        print(f"{color_conjunto2}{elemento}{color_normal}", end=" ")

print("\nIntersección:", end=" ")
for elemento in interseccion:
    print(f"{color_interseccion}{elemento}{color_normal}", end=" ")