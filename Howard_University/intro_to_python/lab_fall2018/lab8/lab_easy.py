class Number():
    def __init__(self):
        self.value = 0

def simple_math():
    number = 0
    add_simple(number, 10)
    subtract_simple(number, 5)
    multiply_simple(number, 7)
    divide_simple(number, 5)
    print(number)
    return number

def class_math():
    number = Number()
    add_class(number, 10)
    subtract_class(number, 5)
    multiply_class(number, 7)
    divide_class(number, 5)
    print(number.value)
    return number

### Don't change anything above this line ###

def add_class(number, amount):
    number.value += amount

def add_simple(number, amount):
    number += amount

def subtract_class(number, amount):
    number.value -= amount

def subtract_simple(number, amount):
    number -= amount
    
def multiply_class(number, amount):
    number.value *= amount

def multiply_simple(number, amount):
    number *= amount
    
def divide_class(number, amount):
    number.value /= amount
    
def divide_simple(number, amount):
    number /= amount

if __name__ == "__main__":
    print("Pass by value (non-class):")
    simple_math()
    print("Pass by reference (classes):")
    class_math()

