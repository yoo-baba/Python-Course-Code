# class Student:
#    def __init__(self, name):
#       self._name = name

#    @property
#    def name(self):
#       return self._name

# s = Student("Sanchit")

# print(s.name)




# class Student:
#    def __init__(self, marks):
#       self._marks = marks

#    @property
#    def marks(self):
#       return self._marks 

#    @marks.setter
#    def marks(self, value):  
#       if 0 <= value <= 100:
#          self._marks = value
#       else:
#          print("Invalid marks")         

# s = Student(80)

# print(s.marks)

# s.marks = 90
# print(s.marks)

# s.marks = 150




# class Rectangle:
#    def __init__(self, width, height):
#       self.width = width
#       self.height = height

#    @property
#    def area(self):   
#       return self.width * self.height

# r = Rectangle(10, 5)  

# print(r.area)
      




class Person:
   def __init__(self, name):
      self._name = name

   @property   
   def name(self):
      return self._name

   @name.setter   
   def name(self, name):
      self._name = name

   @name.deleter   
   def name(self):
      print("Deleting name")
      del self._name

p = Person("Sanchit")      

print(p.name)

p.name = "Rahul"

print(p.name)

del p.name

print(p.name)
