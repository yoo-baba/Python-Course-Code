# class Student:

#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    # def __getattribute__(self, name):
#    #    print("Getting :", name)   
#    #    return super().__getattribute__(name)

#    def __getattr__(self, name):
#          print("Getting :", name)   
#          return super().__getattr__(name)   

# s = Student("Sanchit", 25)      

# print(s.name)
# print(s.age)



# class Student:

#    def __setattr__(self, name, value):
#       # print(f"Setting {name} = {value}")

#       # if name == "age" and value < 18:
#       #    raise ValueError("Age cannot be less than 18")

#       if name == "name":
#          value = value.upper()

#       object.__setattr__(self, name, value)

#    def __delattr__(self, name):
#       # print("Deleting :", name)

#       if name == "roll_no":
#          raise AttributeError("Roll number cannot be deleted")

#       object.__delattr__(self, name)

# s = Student()      

# s.name = "Sanchit"
# s.roll_no = 20

# # print(s.name)

# # del s.roll_no
# del s.name

# print(s.name)




# class Student:

#    def __init__(self):
#       self.name = "Sanchit"
#       self.age = 25

#    def __dir__(self):
#       return ["name", "age"]   

# s = Student()  

# print(dir(s))




class Demo:

   def __enter__(self):
      print("Entering")
      return "Hello from __enter__"

   def __exit__(self, exc_type, exc, tb):
      print("Exiting")   
      print("Exception Type:", exc_type)
      print("Exception Value:", exc)
      print("Traceback:", tb)

with Demo() as value:
   print("Inside with block")      
   print(value)      