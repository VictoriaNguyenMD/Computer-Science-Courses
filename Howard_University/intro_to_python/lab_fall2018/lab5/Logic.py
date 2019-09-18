# Logic.py
# This class lets the user start out with a boolean value, apply boolean operations to it, and see the result at any point.

# The class should be named Logic.
# The __init__ method should take a boolean value, which will be the initial value.
# There should be a method called boolean_and, which takes one boolean value, then and's it with the current value.
# There should be a method called boolean_or, which takes one boolean value, then or's it with the current value.
# There should be a method called boolean_not, which not's the current value.
# There should be a get_value method, which returns the current value.

class Logic:
    def __init__(self, bool_val):
        self.bool_val = bool_val
        
    def boolean_and(self, val):
        self.bool_val = self.bool_val and val
        
    def boolean_or(self, val):
        self.bool_val = self.bool_val or val
    
    def boolean_not(self):
        self.bool_val = not self.bool_val
    
    def get_value(self):
        return self.bool_val


# Example Code: (This code should work, and give the expected results, if your code is correct.
logic = Logic(True)
logic.boolean_and(True)
print(logic.get_value()) # True
logic.boolean_or(False)
logic.boolean_not()
print(logic.get_value()) # False
