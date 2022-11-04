from abc import ABC, abstractmethod

# Pizzen ##################################################
class Pizza(ABC):
    def backen(self):
        print("Backe Pizza")

    def vorbereiten(self):
        print("Bereite Pizza vor")

    def schneiden(self):
        print("Pizza schneiden")

    def einpacken(self):
        print("Packe Pizza ein")

    def __str__(self) -> str:
        return "Eine Pizza"

class SalamiPizza(Pizza):
    def __str__(self) -> str:
        return "Eine SalamiPizza"

class SchinkenPizza(Pizza):
    def __str__(self) -> str:
        return "Eine SchinkenPizza"

class SpinatPizza(Pizza):
    def __str__(self) -> str:
        return "Eine SpinatPizza"

# Pizzeria ################################################
class Pizzeria():

    def bestelle_pizza(self, typ) -> Pizza:

        if (typ == "Salami"):
            pizza = SalamiPizza()
        elif (typ == "Spinat"):
            pizza = SpinatPizza()
        elif (typ == "Schinken"):
            pizza = SchinkenPizza()
        else:
            pizza = Pizza()

        pizza.vorbereiten()
        pizza.backen()
        pizza.schneiden()
        pizza.einpacken()

        return pizza

# Main ####################################################
if __name__ == "__main__":
    pizzeria = Pizzeria()
    pizza = pizzeria.bestelle_pizza("Spinat")
    print(pizza)
