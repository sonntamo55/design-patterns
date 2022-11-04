from abc import ABC, abstractmethod

class Kaffee():
    
    def zubereitungsrezept(self):
        self.koche_wasser()
        self.kaffee_aufbruehen()
        self.in_tasse_schuetten()
        self.milch_und_zucker_hinzufuegen()

    def koche_wasser(self):
        print("Wasser wird gekocht")

    def kaffee_aufbruehen(self):
        print("Lasse Kaffee durch Filter laufen")

    def in_tasse_schuetten(self):
        print("Getränk in Tasse schütten")

    def milch_und_zucker_hinzufuegen(self):
        print("Füge Milch und Zucker hinzu")

class Tee():
    
    def zubereitungsrezept(self):
        self.koche_wasser()
        self.tee_ziehen_lassen()
        self.in_tasse_schuetten()
        self.zitrone_hinzufuegen()

    def koche_wasser(self):
        print("Wasser wird gekocht")

    def tee_ziehen_lassen(self):
        print("Lasse Tee ziehen")

    def in_tasse_schuetten(self):
        print("Getränk in Tasse schütten")

    def zitrone_hinzufuegen(self):
        print("Füge Zitrone hinzu")



if __name__ == "__main__":
    kaffee = Kaffee()
    tee = Tee()
    kaffee.zubereitungsrezept()
    tee.zubereitungsrezept()
    '''
        Kaffee und Tee besitzen den gleichen Ablauf beim Rezept. In manchen Aspekten unterscheiden
        sie sich jedoch.
        Ändern Sie den Code hin zum TemplateMethod Muster:
            - Erstellen Sie eine abstrakte Klasse Heissgetraenk
            - Ziehen Sie folgende Methoden in die neue Klasse
                - zubereitungsrezept()
                - koche_wasser()
                - in_tasse_schuetten()
            - Kaffee und Tee erben von Heissgetraenk
            - Machen Sie das Hinzufügen von Zutaten optional über einen Hook
    '''