# ClubLine.py
# This class simulates a line outside of a club. People can get into the line, leave the line, or get let into the club. At any time, the user can also request to look at the line.

# The class should be named ClubLine.
# The __init__ method should take an array of strings, representing names of people already in line.
# There should be an add_person method that takes in a string representing the name of the person who got in line.
# There should be a person_leaves method with takes in a string representing the name of the person who just left the line.
# There should be a person_admitted method which admits the person at the front of the line, removing them from the line.
# There should be a get_line method, which returns the current line.

class ClubLine:
    
    def __init__(self, array_clubline):
        self.array_clubline = array_clubline
    
    def add_person(self, name):
        self.array_clubline.append(name)
        
    def person_leaves(self, name):
        self.array_clubline.remove(name)
    
    def person_admitted(self):
        self.array_clubline.pop(0)
    
    def get_line(self):
        return self.array_clubline

# Example Code: (This code should work, and give the expected results, if your code is correct.
clubline = ClubLine(["Alice", "Bob", "Carol", "Dave"])
clubline.person_admitted()
clubline.add_person("Eve")
clubline.person_leaves("Carol")
print(clubline.get_line())# ["Bob", "Dave", "Eve"]
