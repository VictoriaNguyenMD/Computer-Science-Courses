def run():
    user_list = []
    user_input = input("What should the program do?" +
        "\n[A]dd a reading." +
        "\n[E]dit a reading." +
        "\n[P]rint existing readings." +
        "\n[R]emove a reading." +
        "\n[Q]uit.\n")
        
    if(user_input == "Q"):
        print("Goodbye!")
        
    while(user_input != "Q"):
        if(user_input == "A"):
            add_new_entry(user_list)
        elif(user_input == "E"):
            edit_entry(user_list)
        elif(user_input == "P"):
            print_entry(user_list)
        elif(user_input == "R"):
            remove_entry(user_list)
        
        user_input = input("What should the program do?" +
        "\n[A]dd a reading." +
        "\n[E]dit a reading." +
        "\n[P]rint existing readings." +
        "\n[R]emove a reading." +
        "\n[Q]uit.\n")
        
        if(user_input == "Q"):
            print("Goodbye!")
        
def add_new_entry(user_list):
    temp = float(input("What was the temperature?\n"))
    user_list.append(temp)
    return user_list

def remove_entry(user_list):
    remove_loc = int(input("Remove reading at which position?\n"))
    user_list.pop(remove_loc - 1)

def edit_entry(user_list):
    edit_loc = int(input("Edit reading at which position?\n"))
    edit_temp = float(input("What should the value be instead?\n"))
    user_list[edit_loc - 1] = edit_temp
    return user_list
    
def print_entry(user_list):
    initial_num = 1
    array_index = 0
    
    while(array_index < len(user_list)):
        print(str(initial_num) + ": " + str(user_list[array_index]))
        array_index += 1
        initial_num += 1

# Don't change anything below this line.
if __name__ == "__main__":
    run()
    
