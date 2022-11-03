from pizzeria import *

if __name__ == "__main__":
    pizzeria = MuenchnerPizzeria()
    pizza = pizzeria.bestelle_pizza("Käse")
    print(type(pizza))