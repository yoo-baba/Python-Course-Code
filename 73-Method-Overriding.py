# class Animal:
#    def sound(self):
#       print("Animal makes a sound")

# class Dog(Animal):
#    def sound(self):
#       print("Dog barks")

# dog = Dog()
# dog.sound()




# class Person:
#    def __init__(self, name):
#       self.name = name

#    def show(self):
#       print("Name :", self.name)   

# class Student(Person):
#    def __init__(self, name, course):
#       self.name = name
#       self.course = course

# student = Student("Sanchit", "Python")      

# student.show()
# print(student.course)




class Animal:
   def sound(self):
      print("Animal makes a sound")

class Dog(Animal):
   def sound(self):
      super().sound()
      print("Dog barks")

dog = Dog()
dog.sound()