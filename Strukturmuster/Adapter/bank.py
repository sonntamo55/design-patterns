# Die Legacy-Klasse der alten Bank
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

# Der Client muss  den Legacy Code der alten Bank kennen
class Client():

    # Referenz auf die alte Bank
    bank:Bank

    def __init__(self, bank: Bank):
        self.bank = bank

    # Der Client implementiert die Transformationslogik
    def ueberweisen(self, iban:str, bic:str):
        kontonr = iban[12:22]
        blz = iban[4:12]
        self.bank.ueberweisen(kontonr, blz)


if __name__ == "__main__":
    cl = Client(Bank())
    cl.ueberweisen("DE99123456780012345678", "BIC600")