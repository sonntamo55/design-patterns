from abc import ABC, abstractmethod
from numpy import double, argmin, argmax
from typing import List

class Vorhersage():
    def aktualisieren(self, temp:double, feuchtigkeit:double, druck:double):
        print("Vorhersage basierend auf:", temp, "Grad Celsius,", feuchtigkeit, "% Luftfeuchtigkeit,", druck, "hPa Luftdruck")

class AktuelleBedingungen():
    def aktualisieren(self, temp:double, feuchtigkeit:double, druck:double):
        print("Aktuelle Bedingungen:", temp, "Grad Celsius und", feuchtigkeit, "% Luftfeuchtigkeit")

class Statistik():
    stats:List[double] = []
    def aktualisieren(self, temp:double, feuchtigkeit:double, druck:double):
        self.stats.append(temp)
        temp_sum = 0.0
        for temp in self.stats:
            temp_sum += temp
        avg = round(temp_sum/len(self.stats), 2)
        print("Mit/Min/Max Temperatur = ", avg, "/", self.stats[argmin(self.stats)], "/", self.stats[argmax(self.stats)])

class Wetterdaten():
    
    stats:Statistik
    vorhersage:Vorhersage
    aktuell:AktuelleBedingungen
    temp:double
    druck:double
    feuchtigkeit:double

    def __init__(self, stats: Statistik, vorhersage: Vorhersage, aktuell: AktuelleBedingungen):
        self.stats = stats
        self.vorhersage = vorhersage
        self.aktuell = aktuell

    def messwerte_geaendert(self):
        self.stats.aktualisieren(self.temp, self.feuchtigkeit, self.druck)
        self.vorhersage.aktualisieren(self.temp, self.feuchtigkeit, self.druck)
        self.aktuell.aktualisieren(self.temp, self.feuchtigkeit, self.druck)

    def setze_messwerte(self, temp:double, feuchtigkeit: double, druck:double):
        self.temp = temp
        self.druck = druck
        self.feuchtigkeit = feuchtigkeit
        self.messwerte_geaendert()

if __name__ == "__main__":
    vs = Vorhersage()
    st = Statistik()
    ak = AktuelleBedingungen()
    wd = Wetterdaten(st, vs, ak)
    wd.setze_messwerte(30, 65, 1001)
    wd.setze_messwerte(28, 70, 998)
    wd.setze_messwerte(25, 80, 990)

    '''
        Die Wetterstation aktualisiert 3 Anzeigen, wenn sich die Messwerte ändern.
        Der Station sind die 3 Anzeigen bekannt.

        Aufgabe: Was muss man machen, wenn eine weitere Anzeige dazu kommt?

        Aufgabe: Ändern Sie den Code zum Observer Muster
            - Abstrakte Klasse "Subjekt" anlegen mit Methoden registriereBeobachter, entferneBeobachter, benachrichtigeBeobachter
            - Wetterdaten erbt von Subjekt
            - Abstrakte Klasse "Observer" anlegen mit Methode aktualisieren
            - Die 3 Anzeigen erben von Observer

        Aufgabe: Was muss man machen, wenn weitere Messwerte hinzukommen?
            - Verbessern Sie den Code entsprechend!

    '''