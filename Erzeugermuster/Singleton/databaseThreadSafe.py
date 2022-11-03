from threading import Thread

class Database(): 

    # load person from DB
    def load_person(self, id) -> str:

        # create new cache dictionary if it doesn't exist
        if not hasattr(self, "cache"):
            self.cache = {}

        # return person if it is in the cache. Otherwise "load" it from the DB and add it to the cache
        if id in self.cache:
            print("cached")
            return self.cache[id]
        else:
            print("new")
            self.cache[id] = "Some Person"
            return self.cache[id]

def load_person_from_db():
    db = Database()
    db.load_person(55)

if __name__ == "__main__":
    process1 = Thread(target=load_person_from_db)
    process2 = Thread(target=load_person_from_db)
    process3 = Thread(target=load_person_from_db)
    process1.start()
    process2.start()
    process3.start()