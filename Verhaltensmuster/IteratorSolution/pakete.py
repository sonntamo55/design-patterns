from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from numpy import double

class Komponente(ABC):
    
    @abstractmethod
    def get_preis(self) -> double:
        pass

    @abstractmethod
    def ausgeben(self) -> str:
        pass

    @abstractmethod
    def erstelle_iterator(self) -> Iterator:
        pass

class Iterator(ABC):
    
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Komponente:
        pass

class PaketIterator(Iterator):

    elemente: List[Komponente] = []
    position:int

    def __init__(self, elem:List[Komponente]):
        self.position = 0
        self.elemente = elem

    def has_next(self) -> bool:
        if (self.position >= len(self.elemente) or self.elemente[self.position] == None):
            return False
        else:
            return True

    def next(self) -> Komponente:
        komp = self.elemente[self.position]
        self.position += 1
        return komp

class NullIterator(Iterator):

    def next(self) -> Komponente:
        return None

    def has_next(self) -> bool:
        return False

class Produkt(Komponente):
    name:str
    beschreibung:str
    preis:double

    def __init__(self, name:str, beschreibung:str, preis:double):
        self.name = name
        self.beschreibung = beschreibung
        self.preis = preis

    def get_preis(self) -> double:
        return self.preis

    def ausgeben(self):
        print(self)

    def erstelle_iterator(self) -> Iterator:
        return NullIterator()

    def __str__(self) -> str:
        return self.name + ": " + self.beschreibung + " (" + str(round(self.preis, 2)) + ")"

class Paket(Komponente):
    name:str
    preis:double
    
    def __init__(self, name:str, preis:double):
        self.name = name
        self.preis = preis
        self.kinder: List[Komponente] = []

    def hinzufuegen(self, kind: Komponente):
        self.kinder.append(kind)

    def entfernen(self, kind: Komponente):
        self.kinder.remove(kind)

    def ausgeben(self) -> str:
        print(self)
        print("Inhalt")
        it = self.erstelle_iterator()
        while it.has_next():
            it.next().ausgeben()

    def get_preis(self) -> double:
        ges_preis = self.preis
        for kind in self.kinder:
            ges_preis += kind.get_preis()
        return ges_preis
    
    def erstelle_iterator(self) -> Iterator:
        return PaketIterator(self.kinder)

    def __str__(self):
        return self.name + " (Einzelpreis: " + str(round(self.preis, 2)) + ")"

if __name__ == "__main__":
    produkt = Produkt("Computer", "Ein super Computer", 599.00)
    #print(produkt)
    paket = Paket("Großes Paket", 3.99)

    # ein Paket kann auch wieder ein Paket enthalten usw.
    paket2 = Paket("Kleines Paket", 2.00)
    produkt2 = Produkt("Maus", "Beidhändige Maus", 20.00)
    paket2.hinzufuegen(produkt2)
    paket.hinzufuegen(produkt)
    paket.hinzufuegen(paket2)
    paket.ausgeben()
    print("\nPaketpreis: " + str(round(paket.get_preis(), 2)))

    print("Mit einem bzw. 2 Iterator(en) selbst navigieren")
    it = paket.erstelle_iterator()
    it2 = paket.erstelle_iterator()
    print(it.next())
    print(it2.next())
    print(it2.next())
    print(it.next())
