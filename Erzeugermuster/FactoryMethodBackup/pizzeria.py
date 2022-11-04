# have to import abcplus
from abc import ABC, ABCMeta

from pyparsing import abstractmethod
from pizza import *

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



