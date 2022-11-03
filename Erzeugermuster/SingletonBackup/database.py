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

if __name__ == "__main__":
    db = Database()
    db.load_person(55)
    db.load_person(55)
    db2 = Database()
    db2.load_person(55)
    db3 = Database()
    db3.load_person(55)
