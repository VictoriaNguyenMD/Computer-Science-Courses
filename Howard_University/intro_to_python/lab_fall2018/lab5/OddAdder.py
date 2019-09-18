# OddAdder.py:
# This class will let people add items one at a time, or as an array, and will keep track of all of the odd items added to it, as well as telling people what the total sum of all the things its keeping track of is.

# This class should be named OddAdder.
# The __init__ method should take no arguments.
# There should be an add_item method that takes in an integer and keeps track of it if it is odd, but not if it is even.
# There should be an add_items method that takes in an array of integers and keeps track of all of the ones that are odd, but not any of the even ones.
# There should be an add_all method that takes no parameters, and returns the sum of all the items the class is keeping track of.

class OddAdder:
    def __init__(self):
        self.array = []
        
    def add_item(self, val):
        if val%2 != 0:
            self.array.append(val)
    
    def add_items(self, vals):
        for val in vals:
            self.add_item(val)
    
    def add_all(self):
        total = 0
        for val in self.array:
            total += val
        return total
# Example Code: (This code should work, and give the expected results, if your code is correct.
oddadder = OddAdder()
oddadder.add_items([3, 3, 4, 1])
print(oddadder.add_all()) # 7
oddadder.add_item(4)
print(oddadder.add_all()) # 7
