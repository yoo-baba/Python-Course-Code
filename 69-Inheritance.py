class Animal:
   def eat(self):
      print("Animal is eating")

class Dog(Animal):
   def bark(self):
      print("Dog is barking")    

class Cat():
   def meow(self):
      print("Cat is Meowing")        

d = Dog() 

# print(isinstance(d, Animal))

print(issubclass(Cat, Animal))

# c = Cat()

# c.eat()
# c.meow()




# class Person:

#    def __init__(self):
#       self.name = "Sanchit"
#       self.age = 25

# class Student(Person):
#    pass      

# s = Student()

# print(s.name)
# print(s.age)



# class Person:

#    def __init__(self, name):
#       self.name = name

# class Student(Person):
#    def study(self):
#       print(self.name, "is studying")      

# s = Student("Rahul")

# print(s.name)
# s.study()




# class Person:

#    def __init__(self, name):
#       self.name = name

# class Student(Person):
#    def __init__(self, name, course):
#          self.name = name
#          self.course = course

# s = Student("Rahul", "Python")

# print(s.name)
# print(s.course)




# class Person:

#    def __init__(self, name):
#       self.name = name

# class Student(Person):
#    def __init__(self, name, course):
#          super().__init__(name)
#          self.course = course

# s = Student("Rahul", "Python")

# print(s.name)
# print(s.course)



# class Animal:
#    def sound(self):
#       print("Animal makes a sound")

# class Dog(Animal):
#    def sound(self):
#       super().sound()
#       print("Dog is barking")    
    

# d = Dog() 

# d.sound()



# class Animal:
#    def eat(self):
#       print("Eating")

# class Mammal(Animal):
#    def walk(self):
#       print("Walking")    

# class Dog(Mammal):
#    def bark(self):
#          print("Dog is barking")        

# d = Dog() 

# d.eat()
# d.walk()
# d.bark()



# class Father:
#    def skills(self):
#       print("Programming")

# class Mother:
#    def hobbies(self):
#       print("Painting")    

# class child(Father, Mother):
#    pass       

# c = child()

# c.skills()
# c.hobbies()



# class Father:
#    def __init__(self):
#       self.father_name = "Raj"

# class Mother:
#    def __init__(self):
#          self.mother_name = "Priya"  

# class child(Father, Mother):
#    def __init__(self):
#       Father.__init__(self)      
#       Mother.__init__(self)      

# c = child()

# print(c.father_name)
# print(c.mother_name)