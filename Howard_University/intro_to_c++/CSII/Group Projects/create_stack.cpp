/* 
Victoria Nguyen
02762017

Linked List
Step 1: Create a Stack
Step 2: Write the push, pop, peek, and print functions within the public
Step 3: Create a list instance that will indicate the stack
Step 4: Implement the functions
Step 5: Test the code
*/

#include <iostream>
#include <list>
#include <iterator>

using namespace std;

//Creates a stack class that contains the functions for the stack
class Stack{
  //Last in, first out
  public:
    void push(int val); //Adds a value to the top
    void pop(); //Remove the top val (no return value)
    void peek(); //looks at the first value
    void print(); //print out the stack
  private:
    list<int> list_stack; //Creates object of list int
};

//Adds a value to the top of the Stack
void Stack::push(int val){
  list_stack.push_front(val);
}

//Remove the top value
void Stack::pop(){
  list_stack.pop_front();
}

//Looks at the top value
void Stack::peek(){
  cout << list_stack.front() << endl;
}

//Prints the values in the list
void Stack::print(){
  //Creates a list iterator for int
  list<int>::iterator iter;

  //For range loop
  for(iter = list_stack.begin(); iter != list_stack.end(); iter++){
    cout << *iter << endl; //dereferences the iter pointer
  }
}

int main(){
  Stack stack;

  stack.push(1);
  stack.push(2);
  stack.push(3); 

  cout << "\nTesting the Push & Print Function" << endl;
  cout << "Top/Last In" << endl;
  stack.print();
  cout << "Bottom/First In" << endl; 

  cout << "\nTesting Pop Function" << endl;
  stack.pop();
  stack.print();

  cout << "\nTesting Peek Function" << endl;
  stack.peek();

}


