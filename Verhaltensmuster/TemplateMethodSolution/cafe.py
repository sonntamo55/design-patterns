from abc import ABC, abstractmethod

class Heissgetraenk(ABC):

    def zubereitungsrezept(self):
        self.koche_wasser()
        self.aufgiessen()
        self.in_tasse_schuetten()

        # Das ist ein Hook
        if self.mit_zutaten():
            self.zutaten_hinzufuegen()

    def koche_wasser(self):
        print("Wasser wird gekocht")

    @abstractmethod
    def aufgiessen(self):
        pass

    def in_tasse_schuetten(self):
        print("Getränk in Tasse schütten")

    # Methode für den Hook
    def mit_zutaten(self) -> bool:
        return True

    @abstractmethod
    def zutaten_hinzufuegen(self):
        pass

class Kaffee(Heissgetraenk):
    
    zutaten:bool

    def __init__(self, zutaten:bool = True):
        self.zutaten = zutaten

    def aufgiessen(self):
        print("Lasse Kaffee durch Filter laufen")

    def zutaten_hinzufuegen(self):
        print("Füge Milch und Zucker hinzu")
    
    def mit_zutaten(self) -> bool:
        return self.zutaten

class Tee(Heissgetraenk):
    
    zutaten:bool

    def __init__(self, zutaten:bool = True):
        self.zutaten = zutaten

    def aufgiessen(self):
        print("Lasse Tee ziehen")

    def zutaten_hinzufuegen(self):
        print("Füge Zitrone hinzu")

    def mit_zutaten(self) -> bool:
        return self.zutaten

if __name__ == "__main__":
    kaffee = Kaffee(False)
    tee = Tee(True)
    kaffee.zubereitungsrezept()
    tee.zubereitungsrezept()