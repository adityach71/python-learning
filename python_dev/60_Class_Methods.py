class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company name is {self.company}")
        
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee()
e1.name = "Aditya"
e1.show()
e1.changeCompany("TESLA")
e1.show()
print(Employee.company)