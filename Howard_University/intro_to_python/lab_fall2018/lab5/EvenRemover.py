# EvenRemover.py
# This class lets users add items into the class, get the items currently in the class, and remove all even items from the class.

# The class should be named EvenRemover.
# The __init__ method should take an array of integers and store them.
# There should be an add_item method that takes a single integer and stores it.
# There should be an add_items method that takes an array of integers and stores them.
# There should be a remove_evens method that removes all even numbers currently stored.
# There should be a get_items method that returns all items currently stored.

class EvenRemover():
    def __init__(self, array_integers):
        self.array_integers = array_integers
    
    def add_item(self, integer):
        self.array_integers.append(integer)
    
    def add_items(self, mult_integers):
        for val in mult_integers:
            self.array_integers.append(val)
        
    def remove_evens(self):
        for val in self.array_integers:
            if val%2 == 0:
                self.array_integers.remove(val)
    
    def get_items(self):
        return self.array_integers
        


# Example Code: (This code should work, and give the expected results, if your code is correct.
evenremover = EvenRemover([10, 11, 4, -3, 0])
print(evenremover.get_items()) # [10, 11, 4, -3, 0]
evenremover.remove_evens()
evenremover.add_item(3)
evenremover.add_items([1, 2, 3])
print(evenremover.get_items()) # [11, -3, 3, 1, 2, 3]
