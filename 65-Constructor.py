
class Student:
   def __init__(self, age, name ="Unknown"):
      self.name = name
      self.age = age

   def display(self):
      print("Name :", self.name)   
      print("Age :", self.age) 
      print("===================")  

student1 = Student( 25, "Sanchit") 
student2 = Student(22) 

student1.display()
student2.display()
