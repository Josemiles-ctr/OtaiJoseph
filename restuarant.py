class Restuarant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restuarant(self):
        print(f"Restuarant name is {self.name} and Restuarant type is {self.type}")

    def open_restuarant(self):
        print(f"Restuarant {self.name} is open")


restuarant = Restuarant("Fresh Hot", "First class")

restuarant.describe_restuarant()
restuarant.open_restuarant()
