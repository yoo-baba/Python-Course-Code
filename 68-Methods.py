# class BankAccount:

#    def set_balance(self, balance):
#       self.balance = balance

#    def deposit(self, amount):
#       self.balance += amount

#    def withdraw(self, amount):
#          self.balance -= amount 

# def show_balance(self):
#       # print("Balance :", self.balance)
#       return self.balance    

# BankAccount.show_balance = show_balance    

# account = BankAccount()

# account.set_balance(10000)

# account.deposit(5000)
# account.withdraw(2000)

# print(account.show_balance())



# class Student:

#    def set_marks(self, math, science):
#       self.math = math
#       self.science = science

#    def total(self):
#       return self.math + self.science   

#    def display(self):
#       print("Math :", self.math)   
#       print("Science :", self.science)   
#       print("Total :", self.total())  

#    def greet(self):
#       print("Hello!")    

# s = Student()      

# s.set_marks(80,90)
# s.display()

# del Student.greet

# s.greet()




# class Student:

#    school = "ABC School"

#    @classmethod
#    def show_school(cls):
#       print(cls.school)

#    @classmethod
#    def change_school(cls, new_school):
#       cls.school = new_school

# Student.show_school() 

# Student.change_school("XYZ School") 

# Student.show_school() 





class Math:

   @staticmethod
   def square(number):
      return number * number

   @staticmethod
   def cube(number):
      return number * number * number

print(Math.square(5))   
print(Math.cube(3))   