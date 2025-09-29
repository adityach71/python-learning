class Employee:
    def __init__(self):
        self.__name= "Harry"

a = Employee()
# print(a.__name)# Cannot be accessed directly
print(a._Employee__name)# Can be accessed indirectly
print(a.__dir__())