# from abc import ABC, abstractmethod

# class Parent(ABC):

#    def __init__(self, name):
#       self.name = name

#    @abstractmethod
#    def hello(self):
#       pass 

# class Child(Parent):
#    def hello(self):
#       print("Hello", self.name)   

# class AnotherChild(Parent):
#    def hello(self):
#       print("Bye", self.name)            

# c = Child("Sanchit")      
# a = AnotherChild("Sanchit")      

# c.hello()
# a.hello()




from abc import ABC, abstractmethod

class BankAccount(ABC):

   @abstractmethod
   def withdraw(self, amount):
      pass

class SavingAccount(BankAccount):

   def __init__(self, balance):
      self.balance = balance 

   def withdraw(self, amount):
         if amount <= self.balance:
             self.balance -= amount  
             print("Withdrawal Successful")
         else:
             print("Insufficent balance")             

account = SavingAccount(5000)             
account.withdraw(2000)