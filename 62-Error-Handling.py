
# try:
#    num = int(input("Enter Number:"))
#    print(100 / num)
# except ZeroDivisionError:
#    print("Cannot divide by zero") 

# except ValueError:
#    print("Invalid Value")

# except:   
#    print("Something went wrong")



# try:
#    num = int(input("Enter Number:"))
#    print(100 / num)
# except (ZeroDivisionError,ValueError):
#    print("Invalid Value") 

# except:   
#    print("Something went wrong")




try:
   num = int(input("Enter Number:"))
   print(100 / num)

except ZeroDivisionError as e:
   print("Error :",e) 

except ValueError as e:
   print("Error :",e)

except Exception as e:   
   print("Error :",e)   

