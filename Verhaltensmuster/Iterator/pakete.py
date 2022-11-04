from abc import abstractmethod
from typing import List
from numpy import double

class Komponente():
    
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

    '''
    Das Composite-Pattern funktioniert hier ganz gut. Was wir jedoch nicht können:
    Wir können nicht selbst über unsere Struktur iterieren (das haben wir bisher
    den Komponenten selbst überlassen).
    Damit verbunden ist, dass wir nicht gleichzeitig über die Struktur iterieren können.

    Aufgabe: Wir brauchen einen Iterator, der über die Kinter iterieren kann.
        - Abstrakte Klasse "Iterator" anlegen, mit Methoden has_next() und next()
        - 2 konkrete Iteratoren, die von der Klasse Iterator erben: PaketIterator und 
          NullIterator (für Produkte – da gibt es ja nichts zu iterieren)
        - Paket und Produkt brauchen eine Methode erstelle_iterator(), die den 
          entsprechenden Iterator liefert
        - Der PaketIterator läuft einfach über die Kinder eines Paketes
        - Für den Test sollen in der Main 2 Iteratoren gleichzeitig über die Kinder
          eines Paketes laufen

    '''