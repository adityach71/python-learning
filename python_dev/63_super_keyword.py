# class PerentClass:
#     def parent_method(self):
#      print("this is the parent method1")

# class ChildClass(PerentClass):
#     # def parent_method(self):
#     #     print("this is the child method")
#     #     super().parent_method()
#     def child_method(self):
#        print("this is the child method2")
#        super().parent_method()

# child_object = ChildClass()
# child_object.child_method()
# child_object.parent_method()





class Employee:
   def __init__(self, name, id):
      self.name = name
      self.id = id

class Programmer(Employee):
   def __init__(self, name , id , lang):
        super().__init__(name, id)
        self.lang = lang

rohan = Employee("Rohan Das", "420")
aditya = Programmer("Aditya", "2345", "python")
print(aditya.id,aditya.lang,aditya.name)