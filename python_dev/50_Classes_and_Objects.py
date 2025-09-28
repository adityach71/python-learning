class Person:
    name = "Aditya"
    occupation = "Software Developer"
    networth = "10rs"

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Harry"
a.occupation = "Coder"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
