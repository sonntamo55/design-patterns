from abc import ABC, abstractmethod

class Ente(ABC):

    def quaken(self):
        print("Quak Quak")

    def schwimmen(self):
        print("Ich schwimme!")

    def fliegen(self):
        print("Ich fliege!")

    @abstractmethod
    def anzeigen(self):
        pass

class StockEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Stockente")

class MoorEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Moorente")

class GummiEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Gummiente")

    def fliegen(self):
        print("Ich kann nicht fliegen")

    def quaken(self):
        print("Quietsch Quietsch")

class LockEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Lockente")

    def fliegen(self):
        print("Ich kann nicht fliegen")

    def quaken(self):
        print("Ich kann nicht quaken")

if __name__ == "__main__":
    stockente = StockEnte()
    moorente = MoorEnte()
    gummiente = GummiEnte()
    lockente = LockEnte()

    stockente.anzeigen()
    stockente.schwimmen()
    stockente.quaken()
    stockente.fliegen()

    moorente.anzeigen()
    moorente.schwimmen()
    moorente.quaken()
    moorente.fliegen()

    gummiente.anzeigen()
    gummiente.schwimmen()
    gummiente.quaken()
    gummiente.fliegen()

    lockente.anzeigen()
    lockente.schwimmen()
    lockente.quaken()
    lockente.fliegen()


    '''
    Durch Vererbung bekommen die Unterklassen Verhalten, das manchmal nicht angemessen ist.
    Man muss es dann jedes mal überschreiben. Es kann auch zu Code-Dopplung kommen.

    Aufgabe: Ändern Sie die Anwendung hin zum Strategy-Pattern
        - Erstellen Sie Interfaces für das FlugVerhalten und das QuakVerhalten
        - Die Klasse Ente soll 2 Member bekommen vom Typ Flug- bzw. QuakVerhalten
        - Die Member müssen gesetzt werden können. Im Konstruktor oder über Setter oder beides. 
        - Es gibt verschiedene Verhalten, die die o.g. Interfaces implementieren: FliegtMitFluegeln, 
          FliegtNicht, Quaken, Quietschen, StummesQuaken
        - In der Ente-Klasse wird die Logik von fliegen() und quaken() an die Member delegiert

    Aufgabe 2: Was muss man ändern, wenn jetzt noch ein Raketenantrieb hinzukommt? Oder ein Pfeifen?
        - Erstellen Sie eine neue Ente: ModellEnte
        - Sie kann (noch) nicht fliegen, aber Pfeifen
        - Zur Laufzeit soll das Flugverhalten zu Raketenantrieb geändert werden
    '''