from numpy import double

# Die Getränke erben von dieser Superklasse
class Getraenk():
    
    beschreibung: str = "Ein unbekanntes Getränk"
    milch: bool = False
    milchschaum: bool = False
    schoko: bool = False
    soja: bool = False

    # Hier setzen wir die Beschreibung der Zutaten zusammen
    def get_beschreibung(self) -> str:
        zutaten_beschreibung = ""
        if self.milch:
            zutaten_beschreibung += ", Milch"
        if self.soja:
            zutaten_beschreibung += ", Soja"
        if self.schoko:
            zutaten_beschreibung += ", Schoko"
        if self.milchschaum:
            zutaten_beschreibung += ", Milchschaum"
        return zutaten_beschreibung

    # Hier setzen wir den Preis der Zutaten zusammen
    def preis(self) -> double:
        zutaten_preis = 0.0
        if self.milch:
            zutaten_preis += .1
        if self.soja:
            zutaten_preis += .15
        if self.schoko:
            zutaten_preis += .2
        if self.milchschaum:
            zutaten_preis += .1
        return zutaten_preis

    # Pretty print für das Getränk
    def __str__(self):
        return self.get_beschreibung() + ": " + str(round(self.preis(), 2))

'''
    Die einzelnen Getränke legen ihren Namen und Preis fest und nutzen die Zutateninfos aus der Superklasse
'''
class Espresso(Getraenk):

    def get_beschreibung(self) -> str:
        return "Espresso" + super().get_beschreibung()

    def preis(self) -> double:
        return 1.99 + super().preis()

class Hausmischung(Getraenk):

    def get_beschreibung(self) -> str:
        return "Hausmischung" + super().get_beschreibung()

    def preis(self) -> double:
        return .89 + super().preis()

class DunkleRoestung(Getraenk):

    def get_beschreibung(self) -> str:
        return "Dunkle Röstung" + super().get_beschreibung()

    def preis(self) -> double:
        return .99 + super().preis()

class Entkoffeiniert(Getraenk):

    def get_beschreibung(self) -> str:
        return "Entkoffeiniert" + super().get_beschreibung()

    def preis(self) -> double:
        return 1.05 + super().preis()


if __name__ == "__main__":
    es = Espresso()
    es.milch = True
    es.schoko = True
    print(es)

    hm = Hausmischung()
    hm.soja = True
    print(hm)

    dr = DunkleRoestung()
    dr.milchschaum = True
    print(dr)
