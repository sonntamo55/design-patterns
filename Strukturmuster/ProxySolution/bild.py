from abc import ABC, abstractmethod

class IBild(ABC):

    @abstractmethod
    def zeichnen(self):
        pass

class Person():
    
    def __init__(self, id:int, vorname:str, nachname:str):
        print("Person wird geladen ...")
        self.id = id
        self.vorname = vorname
        self.nachname = nachname

    def bild_hinzufuegen(self, bild: IBild):
        self.bild = bild

    def get_bild(self):
        return self.bild

    def __str__(self):
        return str(self.id) + ": " + self.vorname + " " + self.nachname
    
class Datenbank():

    # Singleton
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Datenbank, cls).__new__(cls)
        return cls.instance

    def lade_person(self, id:int) -> Person:
        person = Person(id, "Max", "Mustermann")
        bild = BildProxy(id)
        person.bild_hinzufuegen(bild)
        return person

    def lade_bild(self, id:int) -> IBild:
        # id ist hier nur gefaked
        return Bild(400, 600, "Schönes Passfoto")

class Bild(IBild):

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

# Virtual Proxy
class BildProxy(IBild):

    person_id:int

    def __init__(self, id:int):
        self.person_id = id

    '''
    Lazy Loading: Bild wird erst geladen, wenn es gebraucht wird. 
    Achtung: Bild nicht mehrmals laden
    '''
    def zeichnen(self):
        if not hasattr(self, "original"):
            self.original = Datenbank().lade_bild(self.person_id)
        self.original.zeichnen()

if __name__ == "__main__":
    db = Datenbank()

    # Person wird geladen, das Bild nicht
    person = db.lade_person(55)
    print(person)

    # Bild wird geladen (Lazy Loading) und dann gezeichnet
    person.get_bild().zeichnen()

    # Bild wird nicht nochmal geladen, sondern nur gezeichnet
    person.get_bild().zeichnen()
