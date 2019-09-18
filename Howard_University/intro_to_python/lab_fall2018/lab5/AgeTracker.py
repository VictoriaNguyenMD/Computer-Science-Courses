# This file should contain a class called AgeTracker.
# It The __init__ method should take no arguments.
# There should be an add_person method that takes in a string, and an integer. The person and their age should be stored.
# There should be a remove_person method that takes in a string. The person and their age should be removed.
# There should be a have_birthday method that takes in a string. The person named should have their age increased by 1.
# There should be a get_birthday method that takes in a string and returns the person's age, if the name is currently stored, and -1 if the name is not stored.

class AgeTracker:
    def __init__(self):
        self.dict_people = {}
    
    def add_person(self, name, age):
        self.dict_people[name] = age
    
    def remove_person(self, name):
        del self.dict_people[name]
    
    def have_birthday(self, name):
        self.dict_people[name] += 1
    
    def get_birthday(self, name):
        if name not in self.dict_people:
            return -1
        else:
            return self.dict_people[name] 
        
# Example Code: (This code should work, and give the expected results, if your code is correct.
ages = AgeTracker()
ages.add_person("Alice", 12)
ages.add_person("Bob", 19)
ages.add_person("Carol", 80)
ages.have_birthday("Bob")
ages.remove_person("Carol")

print(ages.get_birthday("Alice")) # Should return 12
print(ages.get_birthday("Bob")) # Should return 20
print(ages.get_birthday("Carol")) # Should return -1
