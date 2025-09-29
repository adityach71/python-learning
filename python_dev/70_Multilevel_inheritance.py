class Person:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"Name: {self.name}")

class Employee(Person):   # Inheriting from Person
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def showEmployee(self):
        print(f"Employee ID: {self.id}")

class Programmer(Employee):   # Inheriting from Employee
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def showProgrammer(self):
        print(f"Language: {self.lang}")


# Object of Programmer (inherits Person -> Employee -> Programmer)
p = Programmer("Aditya", 420, "Python")

# Accessing all levels
p.showName()        # from Person
p.showEmployee()    # from Employee
p.showProgrammer()  # from Programmer
