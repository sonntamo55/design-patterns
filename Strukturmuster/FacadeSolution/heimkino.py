class Verstaerker():

    lautstearke: int

    def ein(self):
        print("Verstärker eingeschaltet")

    def aus(self):
        print("Verstärker ausgeschaltet")

    def set_cd(self):
        print("Verstärker: auf CD gesetzt")

    def set_bluray(self):
        print("Verstärker: auf Bluray gesetzt")

    def set_radio(self):
        print("Verstärker: auf Radio gesetzt")

    def set_surround_sound(self):
        print("Verstärker: auf Surround Sound gesetzt")

    def set_stereo(self):
        print("Verstärker: auf Stereo Sound gesetzt")

    def set_lautstaerke(self, lautst):
        self.lautstearke = lautst
        print("Verstärker: auf Lautstärke", lautst, "gesetzt")
    
class Radio():
    def ein(self):
        print("Radio eingeschaltet")

    def aus(self):
        print("Radio ausgeschaltet")

    def set_am(self):
        print("Radio: auf AM gesetzt")

    def set_fm(self):
        print("Radio: auf FM gesetzt")

    def set_kanal(self, kanal):
        print("Radio: auf Kanal", kanal, "gesetzt")

class CdSpieler():
    def ein(self):
        print("CD-Spieler eingeschaltet")

    def aus(self):
        print("CD-Spieler ausgeschaltet")

    def auswerfen(self):
        print("CD-Spieler: CD ausgeworfen")

    def pause(self):
        print("CD-Spieler: Pause")

    def wiedergabe(self):
        print("CD-Spieler: Wiedergabe")

    def stopp(self):
        print("CD-Spieler: Stopp")

class BluraySpieler():
    def ein(self):
        print("Bluray-Spieler eingeschaltet")

    def aus(self):
        print("Bluray-Spieler ausgeschaltet")

    def auswerfen(self):
        print("Bluray-Spieler: Bluray ausgeworfen")

    def pause(self):
        print("Bluray-Spieler: Pause")

    def wiedergabe(self):
        print("Bluray-Spieler: Wiedergabe")

    def stopp(self):
        print("Bluray-Spieler: Stopp")

class Beamer():
    
    def ein(self):
        print("Beamer eingeschaltet")

    def aus(self):
        print("Beamer ausgeschaltet")

    def tv_modus(self):
        print("Beamer: auf TV-Modus gesetzt")
    
    def breitwand_modus(self):
        print("Beamer: auf Breitwand-Modus gesetzt")

class Beleuchtung():
    
    dimm: int

    def ein(self):
        print("Beleuchtung eingeschaltet")

    def aus(self):
        print("Beleuchtung ausgeschaltet")

    def dimmen(self, dimm):
        self.dimm = dimm
        print("Beleuchtung: gedimmt auf", dimm)

class Leinwand():
    
    status: int

    def hoch(self):
        self.status = 1
        print("Leinwand oben")

    def runter(self):
        self.status = 0
        print("Leinwand unten")

class PopcornMaschine():
    
    def ein(self):
        print("Popcorn-Maschine eingeschaltet")

    def aus(self):
        print("Popcorn-Maschine ausgeschaltet")

    def starten(self):
        print("Popcorn wird gemacht")

class HeimkinoFacade():
    popcorn: PopcornMaschine
    beleuchtung: Beleuchtung
    leinwand: Leinwand
    beamer: Beamer
    verstaerker: Verstaerker
    bluray: BluraySpieler

    def __init__(self):
        self.popcorn = PopcornMaschine()
        self.beleuchtung = Beleuchtung()
        self.leinwand = Leinwand()
        self.beamer = Beamer()
        self.verstaerker = Verstaerker()
        self.bluray = BluraySpieler()


    def film_schauen(self):
        print("\n=== Film schauen ===\n")

        self.popcorn.ein()
        self.popcorn.starten()

        self.beleuchtung.ein()
        self.beleuchtung.dimmen(10)

        self.leinwand.runter()

        self.beamer.ein()
        self.beamer.breitwand_modus()

        self.verstaerker.ein()
        self.verstaerker.set_bluray()
        self.verstaerker.set_surround_sound()
        self.verstaerker.set_lautstaerke(5)

        self.bluray.ein()
        self.bluray.wiedergabe()

    def film_beenden(self):
        print("\n=== Film beenden ===\n")

        self.popcorn.aus()
        
        self.verstaerker.aus()
        
        self.beamer.aus()

        self.beleuchtung.ein()

        self.bluray.auswerfen()
        self.bluray.aus()
        
        self.leinwand.hoch()

    def radio_hoeren(self):
        print("\n=== Radio hören ===\n")
        # jetzt kommt die Logik

    def radio_beenden(self):
        print("\n=== Radio beendedn ===\n")
        # jetzt kommt die Logik

    def cd_hoeren(self):
        print("\n=== CD hören ===\n")
        # jetzt kommt die Logik

    def cd_beenden(self):
        print("\n=== CD beenden ===\n")
        # jetzt kommt die Logik

if __name__ == "__main__":
    
    facade = HeimkinoFacade()
    facade.film_schauen()
    facade.film_beenden()
