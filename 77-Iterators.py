# numbers = [10, 20, 30, 40]
# numbers = ["Red", "Green", "Blue"]
# text = "Python"
# student = {
#    "name": "Sanchit",
#    "age": 22,
#    "city": "Goa"
# }

# it = iter(student)

# print(student[next(it)])
# print(student[next(it)])
# print(student[next(it)])
# print(next(it))
# print(next(it))



# numbers = [10, 20, 30]

# iterator = iter(numbers)

# while True:
#    try:
#       number = next(iterator)
#       print(number)
#    except StopIteration:
#       break   



# class MyNumbers:

#    def __iter__(self):
#       self.number = 1
#       return self

#    def __next__(self):

#       if self.number <= 5:

#          value = self.number
#          self.number += 1
#          return value

#       else:

#          raise StopIteration

# obj = MyNumbers()  

# iterator = iter(obj)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for number in obj:
#    print(number)




# class EvenNumbers:

#    def __iter__(self):
#       self.number = 2
#       return self

#    def __next__(self):

#       if self.number <= 10:

#          value = self.number
#          self.number += 2
#          return value

#       else:

#          raise StopIteration

# obj = EvenNumbers()  

# for number in obj:
#    print(number)




class ListIterator:

   def __init__(self, items):
      self.items = items
      self.index = 0

   def __iter__(self):
      return self

   def __next__(self):

      if self.index < len(self.items):

         value = self.items[self.index]
         self.index += 1
         return value

      else:
         raise StopIteration

numbers = [10, 20, 30, 40]      

obj = ListIterator(numbers)  

for number in obj:
   print(number)