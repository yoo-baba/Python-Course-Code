
# with open("data.txt", "r") as file:
#    print(file.read())


# count = 0

# with open("data.txt", "r") as file:
#    for line in file:
#       count += 1

# print("Total Lines:", count)      



# with open("data.txt", "w") as file:
#    file.write("Rahul\n")
#    file.write("Amit\n")
#    file.write("Neha\n")

# print("File written successfully.") 


# student = input("Enter a student:")

# with open("data.txt", "a") as file:
#    file.write(student + "\n")


# print("Saved successfully.")



with open("data.txt", "r") as source:
   content = source.read()

with open("students_file.txt", "w") as destination:
   destination.write(content)   

print("File Copied")   