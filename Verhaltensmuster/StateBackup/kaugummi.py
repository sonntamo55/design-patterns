from abc import ABC, abstractmethod

class Kaugummiautomat():

    AUSVERKAUFT = 0
    KEINE_MUENZE = 1
    HAT_MUENZE = 2
    VERKAUFT = 3

    zustand = AUSVERKAUFT

    anzahl = 0

    def __init__(self, anz:int):
        self.anzahl = anz
        if anz > 0:
            self.zustand = self.KEINE_MUENZE

    def muenze_einwerfen(self):
        if self.zustand == self.HAT_MUENZE:
            print("Sie können keine weitere Münze einwerfen")
        elif self.zustand == self.KEINE_MUENZE:
            print("Sie haben eine Münze eingeworfen")
            self.zustand = self.HAT_MUENZE
        elif self.zustand == self.AUSVERKAUFT:
            print("Sie können keine Münze einwerfen, Automat ist ausverkauft")
        elif self.zustand == self.VERKAUFT:
            print("Bitte warten Sie, Sie erhalten einen Kaugummi")

    def muenze_auswerfen(self):
        if self.zustand == self.HAT_MUENZE:
            print("Münze wird zurückgegeben")
            self.zustand = self.KEINE_MUENZE
        elif self.zustand == self.KEINE_MUENZE:
            print("Münze kann nicht ausgegeben werden, Sie haben keine Münze eingeworfen")
        elif self.zustand == self.AUSVERKAUFT:
            print("Auswurf nicht möglich, Sie haben keine Münze eingeworfen")
        elif self.zustand == self.VERKAUFT:
            print("Zu spät, leider haben Sie den Griff schon gedreht")

    def griff_drehen(self):
        if self.zustand == self.HAT_MUENZE:
            print("Sie haben den Griff gedreht ...")
            self.zustand = self.VERKAUFT
            self.kugel_ausgeben()
        elif self.zustand == self.KEINE_MUENZE:
            print("Sie haben gedreht, aber es ist keine Münze da")
        elif self.zustand == self.AUSVERKAUFT:
            print("Sie haben gedreht, aber es sind keine Kaugummis da")
        elif self.zustand == self.VERKAUFT:
            print("Auch wenn Sie zweimal drehen, bekommen Sie kein zweites Kaugummi")

    def kugel_ausgeben(self):
        if self.zustand == self.HAT_MUENZE:
            print("Es wird kein Kaugummi ausgegeben")
        elif self.zustand == self.KEINE_MUENZE:
            print("Sie müssen zuerst bezahlen")
        elif self.zustand == self.AUSVERKAUFT:
            print("Es wird keine Kugel ausgegeben")
        elif self.zustand == self.VERKAUFT:
            print("Ein Kaugummi rollt aus dem Ausgabeschacht")
            self.anzahl -= 1
            if (self.anzahl == 0):
                print("Hoppla, keine Kaugummis mehr da")
                self.zustand = self.AUSVERKAUFT
            else:
                self.zustand = self.KEINE_MUENZE

    def __str__(self) -> str:
        res = "\nAnzahl Kaugummis: " + str(self.anzahl) + "\n"
        if self.zustand == self.HAT_MUENZE:
            res += "Automat enthält eine Münze"
        elif self.zustand == self.KEINE_MUENZE:
            res += "Automat bereit für Münzeinwurf"
        elif self.zustand == self.AUSVERKAUFT:
            res += "Automat ausverkauft"
        elif self.zustand == self.VERKAUFT:
            res += "Ein Kaugummi wurde verkauft"
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

    '''
    Der Automat ist naiv und unflexibel programmiert. Die Statusänderungen sind im Automaten hart-codier.
    Wenn jetzt ein Zustand hinzukommt, müssen sehr viele Änderungen vorgenommen werden.
    
    Aufgabe: Ändern Sie das Design nach dem State Pattern! 
        - Legen Sie für die 4 Status jeweils eine Klasse an
        - Es soll eine Superklasse "Status" geben, von der alle 4 Statusklassen erben
        - Die Logik wird aus dem Kaugummiautomaten in die Statusklassen verlagert

    Aufgabe: Was muss man machen, wenn ein weiterer Zustand eingeführt werden soll?
        - Zum Beispiel wenn man 2 Münzen für 1 Kaugummi braucht
    
    '''