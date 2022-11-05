# have to import abcplus
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

    def __str__(self):
        return "Eine Pizza"

class SalamiPizza(Pizza):
    def __str__(self):
        return "Eine SalamiPizza"

class SchinkenPizza(Pizza):
    def __str__(self):
        return "Eine SchinkenPizza"

class SpinatPizza(Pizza):
    def __str__(self):
        return "Eine SpinatPizza"

class BerlinerSalamiPizza(Pizza):
    def __str__(self):
        return "Eine Berliner SalamiPizza"

class BerlinerSchinkenPizza(Pizza):
    def __str__(self):
        return "Eine Berliner SchinkenPizza"

class BerlinerKrabbenPizza(Pizza):
    def __str__(self):
        return "Eine Berliner KrabbenPizza"

class BerlinerThunfischPizza(Pizza):
    def __str__(self):
        return "Eine Berliner ThunfischPizza"

class MuenchnerSalamiPizza(Pizza):
    def __str__(self):
        return "Eine Münchner SalamiPizza"

class MuenchnerSchinkenPizza(Pizza):
    def __str__(self):
        return "Eine Münchner SchinkenPizza"

class MuenchnerKrabbenPizza(Pizza):
    def __str__(self):
        return "Eine Münchner KrabbenPizza"

class MuenchnerThunfischPizza(Pizza):
    def __str__(self):
        return "Eine Münchner ThunfischPizza"

class MuenchnerKaesePizza(Pizza):
    def __str__(self):
        return "Eine Münchner KäsePizza"

# Pizzerias ###############################################
class Pizzeria(ABC):

    @abstractmethod
    def erstelle_pizza(self, typ) -> Pizza:
        pass

    def bestelle_pizza(self, typ) -> Pizza:
        pizza = self.erstelle_pizza(typ)

        if (pizza is not None):
            pizza.vorbereiten()
            pizza.backen()
            pizza.schneiden()
            pizza.einpacken()
            
        return pizza

class BerlinerPizzeria(Pizzeria):

    def erstelle_pizza(self, typ) -> Pizza:
        if (typ == "Salami"):
            pizza = BerlinerSalamiPizza()
        elif (typ == "Schinken"):
            pizza = BerlinerSchinkenPizza()
        elif (typ == "Krabben"):
            pizza = BerlinerKrabbenPizza()
        elif (typ == "Thunfisch"):
            pizza = BerlinerThunfischPizza()
        else:
            return None
        return pizza

class MuenchnerPizzeria(Pizzeria):

    def erstelle_pizza(self, typ) -> Pizza:
        if (typ == "Käse"):
            pizza = MuenchnerKaesePizza()
        elif (typ == "Salami"):
            pizza = MuenchnerSalamiPizza()
        elif (typ == "Schinken"):
            pizza = MuenchnerSchinkenPizza()
        elif (typ == "Krabben"):
            pizza = MuenchnerKrabbenPizza()
        elif (typ == "Thunfisch"):
            pizza = MuenchnerThunfischPizza()
        else:
            return None
        return pizza

# Main ####################################################
if __name__ == "__main__":
    pizzeria = MuenchnerPizzeria()
    pizza = pizzeria.bestelle_pizza("Käse")
    print(pizza)