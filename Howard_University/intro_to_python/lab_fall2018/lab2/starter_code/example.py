# Don't change this line.
def run():
    # Replace the example code below with your code.
    int_counter = int(input("Enter an integer: "))
    int_stop = int_counter * 2
    while int_counter < int_stop:
        print("Counter is currently: " + str(int_counter))
        if int_counter % 2 == 0:
            print("Counter is even!")
        else:
            print("Counter is odd!")
        int_counter += 1
    print("Done!")

# Don't change these lines.
if __name__ == "__main__":
    run()
