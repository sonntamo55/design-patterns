class Sofa:
    pass

class VictorianSofa(Sofa):
    def __init__(self):
        print("New victorian sofa")
    
    def __str__(self):
        print("A victorian sofa")

class ModernSofa(Sofa):
    def __init__(self):
        print("New modern table sofa")

    def __str__(self):
        print("A modern sofa")

class ArtDecoSofa(Sofa):
    def __init__(self):
        print("New art deco sofa")

    def __str__(self):
        print("An art deco sofa")