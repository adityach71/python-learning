class Person:
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harry", "Coder")
b = Person("Divia", "HR")
c = Person()
a.info()
b.info()
# print(a.name)