# class Dog:
#     def speak(self):
#         print("Woof!")

# class Cat:
#     def speak(self):
#         print("Meow!")

# class Cow:
#     def speak(self):
#         print("Moo!")        

# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.speak()
#     if type(animal) == Cat:
#         print("==============")


# class Animal:
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")       

# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.speak()




class Dog():
    def speak(self):
        print("Woof!")

class Person():
    def speak(self):
        print("Hello!")  

def make_speak(obj):
    obj.speak()             

dog = Dog()
person = Person()

make_speak(dog)
make_speak(person)