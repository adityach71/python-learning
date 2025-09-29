class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal!")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark")


d = Dog("Dog", "Doggerman")
d.make_sound()   # Bark

a = Animal("Dog", "Dog")
a.make_sound()   # Sound made by the animal!


# Quick Quiz
class Cat(Animal):
    def __init__(self, name, catage):
        super().__init__(name, species="Cat")
        self.catage = catage

    def make_sound(self):
        print("meow")

    def hi(self):
        print("hi")


c = Cat("Kitty", "2 years")
c.make_sound()   # meow
c.hi()           # hi

v = Animal("Cat", "Cat")
v.make_sound()   # Sound made by the animal!
