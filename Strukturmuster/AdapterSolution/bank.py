from abc import ABC, abstractmethod
from numpy import double

# Die legacy Klasse der alten Bank
class LegacyBank():

    # Benötigt Kontonummer und BLZ für die Überweisung
    def ueberweisen(self, kontonr:str, blz:str, betrag:double):
        if not all(char.isdigit() for char in kontonr):
            print("Kontonummer ist keine Zahl")
            return

        if not all(char.isdigit() for char in blz):
            print("BLZ ist keine Zahl")
            return

        print(f"Überweisung von {betrag} EUR auf Konto {kontonr } BLZ {blz}")

# Interface des BankAdapters
class IBank(ABC):

    @abstractmethod
    def ueberweisen(self, kontonr:str, blz:str, betrag:double):
        # wird vom konkreten Adapter implementiert
        pass

# Der konkrete BankAdapter
class BankAdapter(IBank):

    # Referenz auf den legacy Code der alten Bank
    bank: LegacyBank

    # Die Referenz auf die alte Bank wird im Konstruktor mitgegeben
    def __init__(self, bank: LegacyBank):
        self.bank = bank

    # Die Adapterlogic: aus der IBAN werden Kontonummer und BLZ
    def ueberweisen(self, iban:str, bic:str, betrag:double):
        kontonr = iban[12:22]
        blz = iban[4:12]
        self.bank.ueberweisen(kontonr, blz, betrag)

# Der Client kennt den Legacy Code der alten Bank nicht, sondern lediglich das Interface des Adapters
class Client():

    # Referenz auf den Adapter
    bank:IBank

    def __init__(self, bank: IBank):
        self.bank = bank

    # Der Client kann die Überweisung einfach mit IBAN und BIC ausführen
    def ueberweisen(self, iban:str, bic:str, betrag:double):
        self.bank.ueberweisen(iban, bic, betrag)


if __name__ == "__main__":
    cl = Client(BankAdapter(LegacyBank()))
    cl.ueberweisen("DE99123456780012345678", "BIC600", 1500)