# have to import abcplus
from abc import ABC, ABCMeta

from pyparsing import abstractmethod
from pizza import *

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

    def bestelle_pizza(self, typ) -> Pizza:
        return super().bestelle_pizza(typ)

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

    def bestelle_pizza(self, typ) -> Pizza:
        return super().bestelle_pizza(typ)

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


