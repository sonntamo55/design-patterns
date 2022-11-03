class Table:
    pass

class VictorianTable(Table):
    def __init__(self):
        print("New victorian table")

    def __str__(self):
        print("A victorian table")

class ModernTable(Table):
    def __init__(self):
        print("New modern table")

    def __str__(self):
        print("A modern table")

class ArtDecoTable(Table):
    def __init__(self):
        print("New art deco chair")

    def __str__(self):
        print("An art deco table")