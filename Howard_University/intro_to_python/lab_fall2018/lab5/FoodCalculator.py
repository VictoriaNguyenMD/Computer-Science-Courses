# FoodCalculator.py
# This class allows users to add the prices of food items one at a time, and to calculate the tax, tip, and total cost for the added food items.

# The class should be named FoodCalculator.
# The __init__ method should take no arguments.
# There should be an add_item method that takes a float and adds it to the current price.
# There should be a get_tax method that takes a float representing the tax rate and returns the tax on the current price.
# There should be a get_tip method that takes a float representing the tax and a float representing the tip, and returns the cost of the tip on the current price, assuming tip is calculated after tax.
# There should be a method called get_total_cost that takes in a float representing the tax, and a float representing the tip, and returns the total cost of the meal based on the current cost, tax, and tip.

class FoodCalculator:
    def __init__(self):
        self.total = 0.0
    
    def add_item(self,float_val):
        self.total += float_val
    
    def get_tax(self,tax):
        tax /= 100
        return self.total * tax
    
    def get_tip(self, tax, tip):
        tip /=100
        return (self.total + self.get_tax(tax)) * tip
    
    def get_total_cost(self, tax, tip):
        self.total += self.get_tax(tax) + self.get_tip(tax, tip)
        return self.total
        

# Example Code: (This code should work, and give the expected results, if your code is correct.
foodcalc = FoodCalculator()
foodcalc.add_item(100.00)
foodcalc.add_item(1900.00)
print(foodcalc.get_tax(10)) # 200.0
print(foodcalc.get_tip(10, 20)) # 440.0
print(foodcalc.get_total_cost(10, 20)) # 2640.0
