# Don't change this line.
def run():
    # Replace the code below with your code.
    
    string_num = input("Enter a temperature:\n")
    
    while(string_num != "exit"):
    
        float_num = float(string_num)
        string_conversion = input("Is that in C or in F?\n")
        
        if(string_conversion == "C"):
            float_num_CtoF = (float_num * (9/5)) + 32
            print("That's " + str(float_num_CtoF) + " in Fahrenheit.")
        
        elif(string_conversion == "F"):
            float_num_FtoC = float_num_FtoC = (float_num - 32) * (5/9)
            print("That's " + str(float_num_FtoC) + " in Celsius.")
        
        else:
            print("You inputed neither C or in F")
        
        string_num = input("Enter a temperature:\n")
    
    print("Goodbye!")
        

# Don't change these lines.
if __name__ == "__main__":
    run()

