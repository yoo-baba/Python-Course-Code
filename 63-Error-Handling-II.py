
# try:
#    # num = int(input("Enter Number : "))
#    print(10 / 2)

# except:
#    print("Error")

# else:
#    print("Success")   

# finally:
#    print("Always Executes")



# try:
#    file = open("data.txt")

# except FileNotFoundError:
#    print("File not found")

# else:
#    print(file.read())   
#    file.close()

# finally:
#    print("Program Finished")



# age = int(input("Age : "))

# if age < 18:
#    raise Exception("Not Eligible")

# print("Eligible")   

correct_password = "python123"

try:
   password = input("Password: ")

   if password != correct_password:
      raise ValueError("Incorrect Password")

except ValueError as e:
      print(e)

else:
    print("Login Successful")      