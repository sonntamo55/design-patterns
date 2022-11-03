
from threading import Lock, Thread

class Singleton():
    
    _instance = None
    _lock: Lock = Lock()
    value = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance():
        return Singleton()

def test_singleton(value) -> None:
    singleton = Singleton.get_instance()
    if not singleton.value:
        singleton.value = value
    print(id(singleton))


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args=("foo",))
    process2 = Thread(target=test_singleton, args=("bar",))
    process1.start()
    process2.start()
    singleton = Singleton.get_instance()
    print(id(singleton))
    print(singleton.value)