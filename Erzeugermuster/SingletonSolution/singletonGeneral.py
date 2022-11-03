
class Singleton():
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return Singleton()

if __name__ == '__main__':
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    print(s1 is s2)

    s1.attr = "some value"
    print(s2.attr)

    print("Same Ids?", id(s1) == id(s2))