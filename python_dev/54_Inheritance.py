class employee:
    def __init__(self, name , id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class programmer(employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = employee("Rhone Das", 400)
e1.showDetails()
e2 = programmer("Aditya", 4100)
e2.showDetails()
e2.showLanguage()
