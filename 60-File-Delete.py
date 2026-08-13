
import os

if os.path.exists("test.txt"):
   os.remove("test.txt")
   print("File Deleted")
else:
   print("File not found")   

   



