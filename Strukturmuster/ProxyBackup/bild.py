from abc import ABC, abstractmethod

class Bild():

    def __init__(self, hoehe: int, breite: int, meta:str):
        print("Bild wird geladen ... (Teuer!)")
        self.hoehe = hoehe
        self.breite = breite
        self.meta = meta

    def zeichnen(self):
        print("Bild wird gezeichnet ...")
        print(self)

    def __str__(self):
        return self.meta + " (" + str(self.breite) + "x" + str(self.hoehe) + ")"

class Person():
    
    def __init__(self, id:int, vorname:str, nachname:str):
        print("Person wird geladen ...")
        self.id = id
        self.vorname = vorname
        self.nachname = nachname

    def bild_hinzufuegen(self, bild: Bild):
        self.bild = bild

    def get_bild(self):
        return self.bild

    def __str__(self):
        return str(self.id) + ": " + self.vorname + " " + self.nachname
    
class Datenbank():
    
    def lade_person(self, id:int) -> Person:
        person = Person(id, "Max", "Mustermann")
        bild = self.lade_bild()
        person.bild_hinzufuegen(bild)
        return person

    def lade_bild(self) -> Bild:
        return Bild(400, 600, "Schönes Passfoto")

if __name__ == "__main__":
    db = Datenbank()
    person = db.lade_person(55)
    print(person)
    person.get_bild().zeichnen()
    person.get_bild().zeichnen()

    '''
    Wenn eine Person geladen wird, dann auch gleich ihr Bild. Das Bild wird in der Anwendung selten benötigt.
    Es ist also besser, das Bild erst bei Bedarf nachzuladen.
    
    Aufgabe: Ändern Sie den Code so, dass das Proxy-Muster für das Bild verwendet wird (genauer: Virtual Proxy)
        - Bild und BildProxy teilen sich ein Interface IBild
        - Die Datenbank erstellt einen Proxy statt des echten Bildes
        - Die Datenbank sollte ein Singleton sein, damit der Proxy gut darauf zugreifen kann
        - Wenn das Bild benötigt wird (Methode „zeichnen“), lädt der Proxy es nach.
        - Wenn es bereits geladen ist, wird es nicht erneut geladen

    '''