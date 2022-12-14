from abc import ABC

# Tables ##################################################
class Table(ABC):
    pass

class VictorianTable(Table):
    def __init__(self):
        print(self)

    def __str__(self):
        return "A victorian table"

class ModernTable(Table):
    def __init__(self):
        print(self)

    def __str__(self):
        return "A modern table"

class ArtDecoTable(Table):
    def __init__(self):
        print(self)

    def __str__(self):
        return "An art deco table"

# Sofas ###################################################
class Sofa(ABC):
    pass

class VictorianSofa(Sofa):
    def __init__(self):
        print(self)
    
    def __str__(self):
        return "A victorian sofa"

class ModernSofa(Sofa):
    def __init__(self):
        print(self)

    def __str__(self):
        return "A modern sofa"

class ArtDecoSofa(Sofa):
    def __init__(self):
        print(self)

    def __str__(self):
        return "An art deco sofa"

# Chairs ##################################################
class Chair(ABC):
    pass

class VictorianChair(Chair):
    def __init__(self):
        print(self)

    def __str__(self):
        return "A victorian chair"

class ModernChair(Chair):
    def __init__(self):
        print(self)

    def __str__(self):
        return "A modern chair"

class ArtDecoChair(Chair):
    def __init__(self):
        print(self)

    def __str__(self):
        return "An art deco chair"


if __name__ == "__main__":
    m_chair = ModernChair()
    ad_chair = ArtDecoChair()
    m_table = ModernTable()
    v_sofa = VictorianSofa()
    '''
        Der Client hängt von den konkreten Klassen ab und muss sich die
        Klassenfamilien berücksichtigen.
        Ändern Sie den Code hin zum Abstract Factory Muster:
            - Erstellen Sie eine abstrakte FurnitureFactory, die Stuhl, Tisch und Sofa erzeugen kann
            - Erstellen Sie 3 konkrete Möbelfabriken für die 3 Produktfamilien viktorianisch, modern und Art Deco
            - Lassen Sie die 3 konkreten Möbelfabriken die Erzeugnisse erstellen
            - Lassen Sie den Client eine Möbelfabrik benutzen

    '''