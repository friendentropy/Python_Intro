class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def show_info(self):
        print(f"My name is {self.name}",
              f"and my age is {self.age}",
              f"and my location is {self.location}")


myobj = Person("John", 45, "Springfield")
myobj2 = Person("Paul", 75, "Boston")
myobj3 = Person("Smith", 28, "Athens")
myobj4 = Person("Mike", 17, "Soa Paulo")
myobj.show_info()
myobj2.show_info()
myobj3.show_info()
myobj4.show_info()
