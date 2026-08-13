file = open("students.txt", "r")

# print(file.read())
# content = file.read(8)

# print(content)

# print(file.readline(), end="")
# print("Hello")
# print(file.readline(), end="")
# print(file.readline(), end="")

# lines = file.readlines()
# print(lines)

for line in file:
   print(line.strip())

file.close()