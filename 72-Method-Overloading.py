# class Calculator:

#    def add(self, a, b, c=0):
#       return a + b + c

# obj = Calculator()

# print(obj.add(10, 20))
# print(obj.add(10, 20, 30))




# class Student:

#    def display(self, name, age=None):
#       if age is None:
#          print("Name", name)
#       else:
#          print("Name", name)
#          print("Age", age) 

# s = Student()          

# s.display("Sanchit")
# s.display("Rahul", 20)




# class Calculator:

#    def add(self, *args):
#       return sum(args)

# obj = Calculator()

# print(obj.add(10, 20, 30, 40, 50, 55))





# class Person:

#    def information(self, **kwargs):
#       for key, value in kwargs.items():
#          print(key, ":", value)

# p = Person()         

# p.information(name = "Rahul", age=25, city="Goa")





# class Shape:

#    def area(self, *args):

#       if len(args) == 1:
#          radius = args[0]
#          return 3.14 * radius * radius
#       elif len(args) == 2:
#          length, width = args
#          return length * width
#       else:
#          return "Invalid Arguments"

# s = Shape()         

# print(s.area(5))
# print(s.area(20, 10))




from functools import singledispatch

@singledispatch
def display(value):
   print("Unknown type")

@display.register
def _(value: int):
   print("Integer:", value)

@display.register
def _(value: str):
   print("String:", value)   

@display.register
def _(value: list):
   print("List:", value)   

display(10.20)   
display("Hello")   
display([1, 2, 3])   