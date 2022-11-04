from abc import ABC, abstractmethod
from numpy import double, argmin, argmax
from typing import List

class Wetter(ABC):

    @abstractmethod
    def get_temp(self) -> double:
        pass

    @abstractmethod
    def get_feuchtigkeit(self) -> double:
        pass

    @abstractmethod
    def get_druck(self) -> double:
        pass

class Observer(ABC):
    
    @abstractmethod
    def aktualisieren(self, wetter:Wetter):
        pass

class Subjekt(ABC):

    @abstractmethod
    def registriereBeobachter(self, obs:Observer):
        pass

    @abstractmethod
    def entferneBeobachter(self, obs:Observer):
        pass

    @abstractmethod
    def benachrichtigeBeobachter(self):
        pass



class Vorhersage(Observer):
    def aktualisieren(self, wetter:Wetter):
        print("Vorhersage basierend auf:", wetter.get_temp(), "Grad Celsius,", wetter.get_feuchtigkeit(), "% Luftfeuchtigkeit,", wetter.get_druck(), "hPa Luftdruck")

class AktuelleBedingungen(Observer):
    def aktualisieren(self, wetter:Wetter):
        print("Aktuelle Bedingungen:", wetter.get_temp(), "Grad Celsius und", wetter.get_feuchtigkeit(), "% Luftfeuchtigkeit")

class Statistik(Observer):
    stats:List[double] = []

    def aktualisieren(self, wetter:Wetter):
        self.stats.append(wetter.get_temp())
        temp_sum = 0.0
        for temp_d in self.stats:
            temp_sum += temp_d
        avg = round(temp_sum/len(self.stats), 2)
        print("Mit/Min/Max Temperatur = ", avg, "/", self.stats[argmin(self.stats)], "/", self.stats[argmax(self.stats)])

class Wetterdaten(Subjekt, Wetter):
    
    beobachter:List[Observer] = []
    temp:double
    druck:double
    feuchtigkeit:double

    def registriereBeobachter(self, obs:Observer):
        self.beobachter.append(obs)

    def entferneBeobachter(self, obs:Observer):
        self.beobachter.remove(obs)

    def benachrichtigeBeobachter(self):
        for obs in self.beobachter:
            obs.aktualisieren(self)

    def messwerte_geaendert(self):
        self.benachrichtigeBeobachter()

    def setze_messwerte(self, temp:double, feuchtigkeit: double, druck:double):
        self.temp = temp
        self.druck = druck
        self.feuchtigkeit = feuchtigkeit
        self.messwerte_geaendert()

    def get_temp(self) -> double:
        return self.temp

    def get_druck(self) -> double:
        return self.druck

    def get_feuchtigkeit(self) -> double:
        return self.feuchtigkeit

if __name__ == "__main__":
    vs = Vorhersage()
    st = Statistik()
    ak = AktuelleBedingungen()
    wd = Wetterdaten()
    wd.registriereBeobachter(st)
    wd.registriereBeobachter(ak)
    wd.registriereBeobachter(vs)
    wd.setze_messwerte(30, 65, 1001)
    wd.setze_messwerte(28, 70, 998)
    wd.setze_messwerte(25, 80, 990)