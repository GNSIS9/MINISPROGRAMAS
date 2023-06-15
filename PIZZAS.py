# -*- coding: utf-8 -*-
from owlready2 import Property, Thing, get_ontology, AllDifferent, OneOf


onto = get_ontology("http://www.example.org/pizzas.owl")

# Aquí puedes agregar el código para definir tu ontología de pizzas

onto.save("pizzas.owl")

with onto:
    # Clase Pizza
    class Pizza(Thing):
        pass

    # Clase Ingrediente
    class Ingrediente(Thing):
        pass

    # Clase Tamaño
    class Tamaño(Thing):
        pass

    # Clase Tipo de Masa
    class Tipo_Masa(Thing):
        pass

    # Clase Cobertura
    class Cobertura(Thing):
        pass

    # Clase Salsa
    class Salsa(Thing):
        pass

    # Propiedad tieneIngrediente
    class tiene_Ingrediente(Property):
        domain = [Pizza]
        range = [Ingrediente]

    # Propiedad esTipo
    class es_Tipo(Property):
        domain = [Pizza]
        range = [str]
        functional = True  # Define la propiedad como funcional

    # Propiedad tieneTamaño
    class tiene_Tamaño(Property):
        domain = [Pizza]
        range = [Tamaño]

    # Propiedad utilizaMasa
    class utiliza_Masa(Property):
        domain = [Pizza]
        range = [Tipo_Masa]

    # Propiedad tieneCobertura
    class tiene_Cobertura(Property):
        domain = [Pizza]
        range = [Cobertura]

    # Propiedad tieneSalsa
    class tiene_Salsa(Property):
        domain = [Pizza]
        range = [Salsa]

    # Función calcularCalorías
    def calcular_Calorías(pizza):
        # Código para calcular las calorías de la pizza
        pass

    # Función estimarTiempoCocción
    def estimar_Tiempo_Cocción(pizza):
        # Código para estimar el tiempo de cocción de la pizza
        pass

      
    # Instancias de Pizza
    PizzaMargarita = Pizza("PizzaMargarita")
    PizzaPepperoni = Pizza("PizzaPepperoni")

    # Establece relaciones
    PizzaMargarita.tieneIngrediente.append(Ingrediente("MasaTrad"))
    PizzaMargarita.tieneIngrediente.append(Ingrediente("SalsaTomate"))
    PizzaMargarita.tieneIngrediente.append(Ingrediente("QuesoMozzarella"))
    PizzaMargarita.esTipo.append("Margarita")

    PizzaPepperoni.tieneIngrediente.append(Ingrediente("MasaTrad"))
    PizzaPepperoni.tieneIngrediente.append(Ingrediente("SalsaTomate"))
    PizzaPepperoni.tieneIngrediente.append(Ingrediente("QuesoMozzarella"))
    PizzaPepperoni.tieneIngrediente.append(Ingrediente("Pepperoni"))
    PizzaPepperoni.esTipo.append("Pepperoni")

