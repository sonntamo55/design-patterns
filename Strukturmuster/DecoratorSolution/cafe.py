from numpy import double
from abc import ABC, abstractmethod

# Alle Klassen sind Getränke, auch die Dekorierer. 
class Getraenk(ABC):
    
    beschreibung: str = "Ein unbekanntes Getränk"

    def get_beschreibung(self) -> str:
        return self.beschreibung

    @abstractmethod
    def preis(self) -> double:
        # must be implemented by sub classes
        pass

    def __str__(self):
        return self.get_beschreibung() + ": " + str(round(self.preis(), 2))

# Der abstrakte Dekorierer. Auch er ist ein Getränk
class ZutatDecorator(Getraenk, ABC):

    getraenk:Getraenk

    def __init__(self, getraenk: Getraenk):
        self.getraenk = getraenk

    @abstractmethod
    def get_beschreibung(self) -> str:
        # must be implemented by sub classes
        pass
    
    @abstractmethod
    def preis(self) -> double:
        # must be implemented by sub classes
        pass

'''
    Die einzelnen Getränke legen ihren Namen und Preis fest
'''
class Espresso(Getraenk):

    def __init__(self):
        self.beschreibung = "Espresso"

    def preis(self) -> double:
        return 1.99

class Hausmischung(Getraenk):

    def __init__(self):
        self.beschreibung = "Hausmischung"

    def preis(self) -> double:
        return .89

class DunkleRoestung(Getraenk):

    def __init__(self):
        self.beschreibung = "Dunkle Röstung"

    def preis(self) -> double:
        return .99

class Entkoffeiniert(Getraenk):

    def __init__(self):
        self.beschreibung = "Entkoffeiniert"

    def preis(self) -> double:
        return 1.05

'''
    Die Dekorierer erben alle vom abstrakten Dekorierer. Sie müssen mit einem Objekt vom Typ Getränk instanziiert werden, 
    das sie "umschließen"/dekorieren. Sie addieren zusätzliche Kosten auf das umschlossene Objekt. Und Sie fügen der 
    Beschreibung eine Information über sich selbst hinzu. Das heißt, Dekorierer fügen Verhalten hinzu.
'''
class Schoko(ZutatDecorator):

    def get_beschreibung(self) -> str:
        return self.getraenk.get_beschreibung() + ", Schoko"

    def preis(self) -> double:
        return 0.2 + self.getraenk.preis()

class Milch(ZutatDecorator):

    def get_beschreibung(self) -> str:
        return self.getraenk.get_beschreibung() + ", Milch"

    def preis(self) -> double:
        return 0.1 + self.getraenk.preis()

class Milchschaum(ZutatDecorator):

    def get_beschreibung(self) -> str:
        return self.getraenk.get_beschreibung() + ", Milchschaum"

    def preis(self) -> double:
        return 0.1 + self.getraenk.preis()

class Soja(ZutatDecorator):

    def get_beschreibung(self) -> str:
        return self.getraenk.get_beschreibung() + ", Soja"

    def preis(self) -> double:
        return 0.15 + self.getraenk.preis()

'''
    Nun können wir Getränke und Dekorierer nutzen in allen möglichen Kombinationen
'''
if __name__ == "__main__":
    es = Schoko(Milch(Espresso()))
    print(es)

    hm = Soja(Hausmischung())
    print(hm)

    dr = Milchschaum(DunkleRoestung())
    print(dr)
