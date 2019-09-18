# Don't change this line.
def run():
  
  # Your code here. Indent all code by 2 spaces.
  print("What is your name?")
  string_name = input()
  
  print("What is your age?")
  string_age = input()
  
  print("What is the target year?")
  string_target_year = input()
  
  int_new_age = int(string_age) + (int(string_target_year) - 2018)

  print("Hello, " + string_name + "! You are " + string_age + " years old. In the year " + string_target_year + ", you will be " + str(int_new_age) + " years old.")
 
# Ignore this for now.
# We'll learn what it means later!
if __name__ == "__main__":
  run()
