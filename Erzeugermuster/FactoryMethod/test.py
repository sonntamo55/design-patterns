from pizzeria import Pizzeria

if __name__ == "__main__":
    pizzeria = Pizzeria()
    pizza = pizzeria.bestelle_pizza("Spinat")
    print(type(pizza))