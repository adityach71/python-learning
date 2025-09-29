class Employee:
    companyName = "Apple"
    noOfEmployees= 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")


# Employee.showDetails(em1)
em1 = Employee("Aditya")
em1.raise_amount = 0.002
em1.companyName = "Apple India"
em1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)
em2 = Employee('Ariyan')
em2.companyName = "Nestle"
em2.showDetails()