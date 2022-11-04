from __future__ import annotations
from abc import ABC, abstractmethod

class Zustand(ABC):
    
    automat:Kaugummiautomat

    def __init__(self, autom:Kaugummiautomat) -> None:
        self.automat = autom    

    @abstractmethod
    def muenze_einwerfen(self):
        pass

    @abstractmethod
    def muenze_auswerfen(self):
        pass

    @abstractmethod
    def griff_drehen(self):
        pass

    @abstractmethod
    def kugel_ausgeben(self):
        pass

class VerkauftZustand(Zustand):

    def muenze_einwerfen(self):
        print("Bitte warten Sie, Sie erhalten einen Kaugummi")

    def muenze_auswerfen(self):
        print("Zu spät, leider haben Sie den Griff schon gedreht")

    def griff_drehen(self):
        print("Auch wenn Sie zweimal drehen, bekommen Sie kein zweites Kaugummi")

    def kugel_ausgeben(self):
        print("Ein Kaugummi rollt aus dem Ausgabeschacht")
        self.automat.anzahl -= 1
        if self.automat.anzahl > 0:
            self.automat.zustand = self.automat.keine_muenze_zustand
        else:
            print("Hoppla, keine Kaugummis da!")
            self.automat.zustand = self.automat.ausverkauft_zustand

    def __str__(self) -> str:
        return "Ein Kaugummi wurde verkauft"

class AusverkauftZustand(Zustand):

    def muenze_einwerfen(self):
        print("Sie können keine Münze einwerfen, Automat ist ausverkauft")

    def muenze_auswerfen(self):
        print("Auswurf nicht möglich, Sie haben keine Münze eingeworfen")

    def griff_drehen(self):
        print("Sie haben gedreht, aber es sind keine Kaugummis da")

    def kugel_ausgeben(self):
        print("Es wird keine Kugel ausgegeben")

    def __str__(self) -> str:
        return "Automat ausverkauft"

class KeineMuenzeZustand(Zustand):

    def muenze_einwerfen(self):
        print("Sie haben eine Münze eingeworfen")
        self.automat.zustand = self.automat.hat_muenze_zustand

    def muenze_auswerfen(self):
        print("Münze kann nicht ausgegeben werden, Sie haben keine Münze eingeworfen")

    def griff_drehen(self):
        print("Sie haben gedreht, aber es ist keine Münze da")

    def kugel_ausgeben(self):
        print("Sie müssen zuerst bezahlen")

    def __str__(self) -> str:
        return "Automat bereit für Münzeinwurf"

class HatMuenzeZustand(Zustand):

    def muenze_einwerfen(self):
        print("Sie können keine weitere Münze einwerfen")

    def muenze_auswerfen(self):
        print("Münze wird zurückgegeben")
        self.automat.zustand = self.automat.keine_muenze_zustand

    def griff_drehen(self):
        print("Sie haben den Griff gedreht ...")
        self.automat.zustand = self.automat.verkauft_zustand
        self.automat.kugel_ausgeben()

    def kugel_ausgeben(self):
        print("Es wird kein Kaugummi ausgegeben")

    def __str__(self) -> str:
        return "Automat enthält eine Münze"
       
class Kaugummiautomat():

    ausverkauft_zustand:Zustand
    keine_muenze_zustand:Zustand
    hat_muenze_zustand:Zustand
    verkauft_zustand:Zustand

    zustand:Zustand

    anzahl = 0

    def __init__(self, anz:int):
        self.ausverkauft_zustand = AusverkauftZustand(self)
        self.keine_muenze_zustand = KeineMuenzeZustand(self)
        self.hat_muenze_zustand = HatMuenzeZustand(self)
        self.verkauft_zustand = VerkauftZustand(self)
        self.zustand = self.ausverkauft_zustand
        self.anzahl = anz
        if anz > 0:
            self.zustand = self.keine_muenze_zustand

    def muenze_einwerfen(self):
        self.zustand.muenze_einwerfen()

    def muenze_auswerfen(self):
        self.zustand.muenze_auswerfen()

    def griff_drehen(self):
        self.zustand.griff_drehen()

    def kugel_ausgeben(self):
        self.zustand.kugel_ausgeben()

    def __str__(self) -> str:
        res = "\nAnzahl Kaugummis: " + str(self.anzahl) + "\n"
        res += str(self.zustand)
        return res + "\n"
        

if __name__ == "__main__":
    ka = Kaugummiautomat(5)
    print(ka)
    ka.muenze_einwerfen()
    ka.griff_drehen()
    print(ka)

    ka.muenze_einwerfen()
    ka.muenze_auswerfen()
    ka.griff_drehen()
    
    print(ka)

    ka.muenze_einwerfen()
    ka.griff_drehen()
    ka.muenze_einwerfen()
    ka.griff_drehen()
    ka.muenze_auswerfen()

    print(ka)

    ka.muenze_einwerfen()
    ka.muenze_einwerfen()
    ka.griff_drehen()
    ka.muenze_einwerfen()
    ka.griff_drehen()
    ka.muenze_einwerfen()
    ka.griff_drehen()

    print(ka)   