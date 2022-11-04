from abc import ABC, abstractmethod

class FlugVerhalten(ABC):

    @abstractmethod
    def fliegen(self):
        pass

class FliegtMitFluegeln(FlugVerhalten):

    def fliegen(self):
        print("Ich fliege mit Flügeln")

class FliegtNicht(FlugVerhalten):

    def fliegen(self):
        print("Ich kann nicht fliegen")

class QuakVerhalten(ABC):

    @abstractmethod
    def quaken(self):
        pass

class Quaken(QuakVerhalten):

    def quaken(self):
        print("Quak Quak")

class Quietschen(QuakVerhalten):

    def quaken(self):
        print("Quietsch Quietsch")

class StummenQuaken(QuakVerhalten):

    def quaken(self):
        print("Ich kann nicht quaken")

class Ente(ABC):

    flugverhalten:FlugVerhalten
    quakverhalten:QuakVerhalten

    def __init__(self, fv:FlugVerhalten, qv:QuakVerhalten):
        self.quakverhalten = qv
        self.flugverhalten = fv

    def tuQuaken(self):
        self.quakverhalten.quaken()

    def schwimmen(self):
        print("Ich schwimme!")

    def tuFliegen(self):
        self.flugverhalten.fliegen()

    @abstractmethod
    def anzeigen(self):
        pass

class StockEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Stockente")

class MoorEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Moorente")

class GummitEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Gummiente")

class LockEnte(Ente):

    def anzeigen(self):
        print("Sieht aus wie eine Lockente")



if __name__ == "__main__":
    stockente = StockEnte(FliegtMitFluegeln(), Quaken())
    moorente = MoorEnte(FliegtMitFluegeln(), Quaken())
    gummiente = GummitEnte(FliegtNicht(), Quietschen())
    lockente = LockEnte(FliegtNicht(), StummenQuaken())

    stockente.anzeigen()
    stockente.schwimmen()
    stockente.tuQuaken()
    stockente.tuFliegen()

    moorente.anzeigen()
    moorente.schwimmen()
    moorente.tuQuaken()
    moorente.tuFliegen()

    gummiente.anzeigen()
    gummiente.schwimmen()
    gummiente.tuQuaken()
    gummiente.tuFliegen()

    lockente.anzeigen()
    lockente.schwimmen()
    lockente.tuQuaken()
    lockente.tuFliegen()