class hello:
   test = "----- Testing -----"
   
   def message(self, name):
      print("Hello", name)
      print(self.test)

   def bye(self):
         print("Bye Everyone")      

a = hello()
a.message("Sanchit")
# a.bye()

b = hello()
a.message("Rohit")


