from numpy import double

# Die Legacy-Klasse der alten Bank
class LegacyBank():

    # Benötigt Kontonummer und BLZ für die Überweisung
    def ueberweisen(self, kontonr:str, blz:str, betrag:double):
        if not all(char.isdigit() for char in kontonr):
            print("Kontonummer ist keine Zahl")
            return

        if not all(char.isdigit() for char in blz):
            print("BLZ ist keine Zahl")
            return

        print(f"Überweisung von {betrag} EUR auf Konto {kontonr} BLZ {blz}")

# Der Client muss  den Legacy Code der alten Bank kennen
class Client():

    # Referenz auf die alte Bank
    bank:LegacyBank

    def __init__(self, bank: LegacyBank):
        self.bank = bank

    # Der Client implementiert die Transformationslogik
    def ueberweisen(self, iban:str, bic:str, betrag:double):
        kontonr = iban[12:22]
        blz = iban[4:12]
        self.bank.ueberweisen(kontonr, blz, betrag)


if __name__ == "__main__":
    cl = Client(LegacyBank())
    cl.ueberweisen("DE99123456780012345678", "BIC600", 1500)

    '''
        Die Transformationslogik befindet sich im Client. Das ist ungeschickt, denn es kann hier
        potenziell zu Änderungen kommen.
        
        Aufgabe: Ändern Sie das Design hin zum Adapter-Muster:
            - Legen Sie ein Interface für den Adapter an
            - Implementieren Sie das Interface durch einen konkreten Adapter
            - Der Adapter soll eine Referenz auf ein Bank-Objekt erhalten (Objektadapter)
            - Erstellen Sie die Transformationslogik im konkreten Adapter

    '''