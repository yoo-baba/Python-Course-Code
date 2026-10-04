# class Point:

#    def __init__(self, x, y):
#       self.x = x
#       self.y = y

#    def __add__(self, other):
#         return Point(
#             self.x + other.x,
#             self.y + other.y
#         ) 

#    def __sub__(self, other):
#            return Point(
#                self.x - other.x,
#                self.y - other.y
#            ) 

# p1 = Point(10, 20)      
# p2 = Point(5, 15)  

# p3 =__enter__() & __exit__()

# print(p3.x)
# print(p3.y)



# class Number:

#    def __init__(self, value):
#       self.value = value

#    def __mul__(self, other):
#       return Number(self.value * other.value)   

#    def __truediv__(self, other):
#       return Number(self.value / other.value)   

# a = Number(10)      
# b = Number(5)      

# c = a / b

# print(c.value)




# class Student:

#    def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks

#    def __eq__(self, other):
#       return self.marks == other.marks   

#    def __gt__(self, other):
#       return self.marks > other.marks

#    def __lt__(self, other):
#       return self.marks < other.marks

#    def __ge__(self, other):
#       return self.marks >= other.marks
   
#    def __le__(self, other):
#       return self.marks <= other.marks 

#    def __ne__(self, other):
#       return self.marks != other.marks 

#    def __str__(self):
#       return f"Name: {self.name}, Marks: {self.marks}"

# s1 = Student("Rahul", 80)
# s2 = Student("Amit", 80)

# # print(s1 != s2)

# print(s1)




# class Student:

#    def __init__(self):
#       self.subject = ["Python", "Java", "C++"]

#    def __getitem__(self, index):
#          return self.subject[index]

# s = Student()

# print(s[0])
# print(s[1])
# print(s[2])



# class Greeting:

#    def __call__(self, name):
#       print("Hello", name)

# g = Greeting() 

# g("Sanchit")




class Money:

   def __init__(self, amount):
      self.amount = amount

   def __add__(self, other):
      return Money(self.amount + other.amount)   

   def __sub__(self, other):
      return Money(self.amount - other.amount)

   def __str__(self):
      return f"Rs.{self.amount}"   

salary = Money(50000)      
bonus = Money(10000)

total = salary + bonus
remaining = salary - bonus

print(total)
print(remaining)