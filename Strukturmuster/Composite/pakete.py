from typing import List
from xml.sax.saxutils import prepare_input_source
from numpy import double

class Produkt():
    name:str
    beschreibung:str
    preis:double

    def __init__(self, name:str, beschreibung:str, preis:double):
        self.name = name
        self.beschreibung = beschreibung
        self.preis = preis

    def __str__(self):
        return self.name + ": " + self.beschreibung + " (" + str(round(self.preis, 2)) + ")"

class Paket():
    name:str
    preis:double

    def __init__(self, name:str, preis:double):
        self.name = name
        self.preis = preis
        self.produkte: List[Produkt] = []

    def produkt_hinzufuegen(self, produkt: Produkt):
        self.produkte.append(produkt)

    def produkte_ausgeben(self):
        print(self)
        for produkt in self.produkte:
            print(produkt)

    def get_preis(self):
        ges_preis = self.preis
        for produkt in self.produkte:
            ges_preis += produkt.preis
        return ges_preis

    def __str__(self):
        return self.name + " (Einzelpreis: " + str(round(self.preis, 2)) + ")"


if __name__ == "__main__":
    produkt = Produkt("Computer", "Ein super Computer", 599.00)
    print(produkt)
    paket = Paket("Paket", 3.99)
    paket.produkt_hinzufuegen(produkt)
    paket.produkte_ausgeben()
    print("Paketpreis: " + str(round(paket.get_preis(), 2)))
    '''
        Was muss man tun, wenn Pakete wieder Pakete enthalten können sollen?
        Ändern Sie den Code so, dass Pakete und Produkte gleich behandelt
        werden können, d.h. wenden Sie das Composite-Muster an!
    '''
