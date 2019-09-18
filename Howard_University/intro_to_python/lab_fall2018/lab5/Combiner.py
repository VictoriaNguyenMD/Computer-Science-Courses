# Combiner.py:
# This class takes two arrays of integers in when created, and can calculate either all possible sums or all possible multiplications consisting of one item from each array.

# The class should be named Combiner
# The __init__ method should take two int arrays as arguments.
# There should be a combine_addition method that takes no parameters and returns a list of the results of all additions consisting of one item in the first list, and one item in the second list.
# There should be a combine_addition method that takes no parameters and returns a list of the results of all multiplications consisting of one item in the first list, and one item in the second list.
# Order does not matter for the returned results.

class Combiner:
    def __init__(self, int_array1, int_array2):
        self.int_array1 = int_array1
        self.int_array2 = int_array2
    
    def combine_addition(self):
        temp = []
        
        for int1 in self.int_array1:
            for int2 in self.int_array2:
                temp.append(int1 + int2)
        
        return temp
    
    def combine_multiplication(self):
        temp = []
        
        for int1 in self.int_array1:
            for int2 in self.int_array2:
                temp.append(int1 * int2)
        
        return temp
    


# Example Code: (This code should work, and give the expected results, if your code is correct.
combiner = Combiner([1, 2], [0, 1])
print(combiner.combine_addition()) # [1, 2, 2, 3]
print(combiner.combine_multiplication()) # [0, 1, 0, 2]
