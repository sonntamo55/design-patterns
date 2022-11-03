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

    def hole_bild(self):
        return self.bild

    def __str__(self):
        return str(self.id) + ": " + self.vorname + " " + self.nachname
    
class Datenbank():
    
    def load_person(self, id:int) -> Person:
        person = Person(id, "Max", "Mustermann")
        bild = self.bild_laden()
        person.bild_hinzufuegen(bild)
        return person

    def bild_laden(self) -> Bild:
        return Bild(400, 600, "Schönes Passfoto")

if __name__ == "__main__":
    db = Datenbank()
    person = db.load_person(55)
    print(person)
    person.hole_bild().zeichnen()
    person.hole_bild().zeichnen()
