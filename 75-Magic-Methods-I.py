# class Student:

#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def __str__(self):
#      return f"{self.name} is {self.age} year old"   

#    def __repr__(self):
#       return f"Student('{self.name}' , '{self.age}')"       

# s = Student("Sanchit", 25)

# print(s)
# print(repr(s))


class Team:

   def __init__(self, players):
      self.players = players

   def __len__(self):
      return len(self.players)

   def __getitem__(self, index):
      return self.players[index]

   def __setitem__(self, index, value):
      self.players[index] = value

   def __delitem__(self, index):
         del self.players[index] 

   def __contains__(self, player):
            return player in self.players 

   def __iter__(self):
       return iter(self.players) 

   def __reversed__(self):
       return reversed(self.players)

team = Team(["Rahul", "Amit", "Sanchit"]) 

print(list(reversed(team)))

# for player in team:
#     print(player)

# print(len(team))

# team[1] = "Salman"

# del team[0]

# print(team[0])
# print(team[1])

# print("Amit" in team)
# print("John" in team)
