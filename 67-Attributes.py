# class Student:
#    city = "Mumbai"
#    # subject = []

#    # __slots__ = ("name", "age")

#    def __init__(self, name, age, fees):
#       self.name = name
#       self.age = age
#       self.__fees = fees
#       # self._state = state

#    def display(self):
#       print(self.__fees)   

# s1 = Student("Rahul", 20, 500)      
# # s2 = Student("Amit", 22)   
# # 
# print(s1._Student__fees)   

# # print(s1.name)
# # print(s1.__fees)
# # s1.display()

# s1.city = "Delhi"

# # Student.city = "Goa"
# s1.subject.append("Python")

# print(s2.subject)




# class Student:

#    def __init__(self, name):
#       self.name = name

# s1 = Student("Rahul") 
# s2 = Student("Amit") 

# s1.age = 20
# s1.city = "Mumbai"

# print(s2.name)
# print(s2.age)
# print(s2.city)



# class Student:
#    pass
   
# s1 = Student() 
# s2 = Student() 

# s1.name = "Rahul"
# s1.age = 20

# s2.name = "Amit"
# s2.email = "amit@gmail.com"

# print(s1.name)
# print(s2.email)



class Student:
   school = "ABC School"

   def __init__(self, name, age):
      self.name = name
      self.age = age

s1 = Student("Rahul", 20)

# print(s1.__dict__)
# print(Student.__dict__)

# print(vars(s1))
print(dir(s1))