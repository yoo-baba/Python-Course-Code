class Student:
   def __init__(self, name):
      self.name = name
      print("Object Created")

   def __del__(self):
         print("Object Destroyed")   

student = Student("Sanchit") 

del student
# student.__del__()

print(type(student))

print("Program Continues...")
