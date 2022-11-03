# Die legacy Klasse der alten Bank
class Bank():

    # Benötigt Kontonummer und BLZ für die Überweisung
    def ueberweisen(self, kontonr, blz):
        if not all(char.isdigit() for char in kontonr):
            print("Kontonummer ist keine Zahl")
            return

        if not all(char.isdigit() for char in blz):
            print("BLZ ist keine Zahl")
            return

        print("Überweisung auf Konto", kontonr, "BLZ", blz)

# Interface des BankAdapters
class BankAdapter():

    def ueberweisen(self, kontonr:str, blz:str):
        # wird vom konkreten Adapter implementiert
        pass

# Der konkrete BankAdapter
class KonkreterBankAdapter(BankAdapter):

    # Referenz auf den legacy Code der alten Bank
    bank: Bank

    # Die Referenz auf die alte Bank wird im Konstruktor mitgegeben
    def __init__(self, bank: Bank):
        self.bank = bank

    # Die Adapterlogic: aus der IBAN werden Kontonummer und BLZ
    def ueberweisen(self, iban:str, bic:str):
        kontonr = iban[12:22]
        blz = iban[4:12]
        self.bank.ueberweisen(kontonr, blz)

# Der Client kennt den Legacy Code der alten Bank nicht, sondern lediglich das Interface des Adapters
class Client():

    # Referenz auf den Adapter
    bank:BankAdapter

    def __init__(self, bank: BankAdapter):
        self.bank = bank

    # Der Client kann die Überweisung einfach mit IBAN und BIC ausführen
    def ueberweisen(self, iban:str, bic:str):
        self.bank.ueberweisen(iban, bic)


if __name__ == "__main__":
    cl = Client(KonkreterBankAdapter(Bank()))
    cl.ueberweisen("DE99123456780012345678", "BIC600")