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
    class TipoMasa(Thing):
        pass

    # Clase Cobertura
    class Cobertura(Thing):
        pass

    # Clase Salsa
    class Salsa(Thing):
        pass

    # Propiedad tieneIngrediente
    class tieneIngrediente(Property):
        domain = [Pizza]
        range = [Ingrediente]

    # Propiedad esTipo
    class esTipo(Property):
        domain = [Pizza]
        range = [str]
        functional = True  # Define la propiedad como funcional

    # Propiedad tieneTamaño
    class tieneTamaño(Property):
        domain = [Pizza]
        range = [Tamaño]

    # Propiedad utilizaMasa
    class utilizaMasa(Property):
        domain = [Pizza]
        range = [TipoMasa]

    # Propiedad tieneCobertura
    class tieneCobertura(Property):
        domain = [Pizza]
        range = [Cobertura]

    # Propiedad tieneSalsa
    class tieneSalsa(Property):
        domain = [Pizza]
        range = [Salsa]

    # Función calcularCalorías
    def calcularCalorías(pizza):
        # Código para calcular las calorías de la pizza
        pass

    # Función estimarTiempoCocción
    def estimarTiempoCocción(pizza):
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

# Axiomas o reglas de restricción

# Restricciones de ingredientes
class_restriction = AllDifferent([Pizza.tieneIngrediente])
onto.add_axiom(class_restriction)

# Restricciones de tamaño
class_restriction = Or([Pizza.tieneTamaño == "Pequeña", Pizza.tieneTamaño == "Mediana", Pizza.tieneTamaño == "Grande"])
onto.add_axiom(class_restriction)


