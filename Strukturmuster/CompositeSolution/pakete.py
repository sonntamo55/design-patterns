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

    def __str__(self) -> str:
        return self.name + ": " + self.beschreibung + " (" + str(round(self.preis, 2)) + ")"

class Paket(Komponente):
    name:str
    preis:double
    kinder:List[Komponente]

    def __init__(self, name:str, preis:double):
        self.name = name
        self.preis = preis
        self.kinder = []

    def hinzufuegen(self, kind: Komponente):
        self.kinder.append(kind)

    def entfernen(self, kind: Komponente):
        self.kinder.remove(kind)

    def ausgeben(self) -> str:
        print(self)
        print("Inhalt")
        for kind in self.kinder:
            kind.ausgeben()

    def get_preis(self) -> double:
        ges_preis = self.preis
        for kind in self.kinder:
            ges_preis += kind.get_preis()
        return ges_preis
    
    def __str__(self):
        return self.name + " (Einzelpreis: " + str(round(self.preis, 2)) + ")"

if __name__ == "__main__":
    produkt = Produkt("Computer", "Ein super Computer", 599.00)
    paket = Paket("Großes Paket", 3.99)

    # ein Paket kann auch wieder ein Paket enthalten usw.
    paket2 = Paket("Kleines Paket", 2.00)
    produkt2 = Produkt("Maus", "Beidhändige Maus", 20.00)
    paket2.hinzufuegen(produkt2)
    paket.hinzufuegen(produkt)
    paket.hinzufuegen(paket2)
    paket.ausgeben()
    print("\nPaketpreis: " + str(round(paket.get_preis(), 2)))
