from abc import ABC, abstractmethod

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

class FurnitureFactory(ABC):
    
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass
    
    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

class ModernFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_table(self) -> Table:
        return ModernTable()

class ArtDecoFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

    def create_table(self) -> Table:
        return ArtDecoTable()

class VictorianFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_table(self) -> Table:
        return VictorianTable()

if __name__ == "__main__":
    m_factory = ArtDecoFactory()
    m_factory.create_table()
    m_factory.create_chair()
    m_factory.create_sofa()