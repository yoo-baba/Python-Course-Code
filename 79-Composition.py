# class Engine:
#    def start(self):
#       print("Engine Started")

# class Car:
#    def __init__(self):
#        self.engine = Engine()     

#    def start(self):    
#       self.engine.start()
#       print("Car started")

# car = Car()      
# car.start()




# class Engine:
#    def start(self):
#       print("Engine Started")

# class Car:
#    def __init__(self, engine):
#        self.engine = engine   

#    def start(self):    
#       self.engine.start()
#       print("Car started")

# engine = Engine()
# car = Car(engine)   

# car.start()





# class Engine:
#    def start(self):
#       print("Engine started")

# class Battery:
#    def supply_power(self):
#       print("Battery supplying power")      

# class Wheel:
#    def rotate(self):
#       print("Wheel rotating") 

# class Car:
#    def __init__(self):
#       self.engine = Engine()          
#       self.battery = Battery()
#       self.wheels = [
#          Wheel(),
#          Wheel(),
#          Wheel(),
#          Wheel()
#       ]

#    def start(self):
#       self.battery.supply_power()     
#       self.engine.start()

#    def drive(self):
#       for wheel in self.wheels:      
#          wheel.rotate()

# car = Car()         

# car.start()
# car.drive()




class Address:
   def __init__(self, city, state):
      self.city = city
      self.state = state

class Person:
   def __init__(self, name, city, state):
      self.name = name      
      self.address = Address(city, state)

person = Person("Sanchit", "Chandigarh", "Punjab")      

print(person.name)
print(person.address.city)
print(person.address.state)
