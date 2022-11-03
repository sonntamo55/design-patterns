class Chair:
    pass

class VictorianChair(Chair):
    def __init__(self):
        print("New victorian chair")

    def __str__(self):
        return "A victorian chair"

class ModernChair(Chair):
    def __init__(self):
        print("New modern chair")

    def __str__(self):
        return "A modern chair"

class ArtDecoChair(Chair):
    def __init__(self):
        print("New art deco chair")

    def __str__(self):
        return "An art deco chair"