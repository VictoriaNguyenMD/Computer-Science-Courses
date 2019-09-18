#include "Stack.h"

#include <iostream>
#include <list>
#include <iterator>
#include <string>
using namespace std;


//Adds a value to the top of the Stack
void Stack::push(int val){
  list_stack.push_front(val);
}

//Remove the top value
void Stack::pop(){
  list_stack.pop_front();
}

//Looks at the top value
int Stack::peek(){
  if(list_stack.empty() == true){
     cout << "List is empty" << endl;
  }
  return list_stack.front();
}

//Prints the values in the list
void Stack::print(){
   if(list_stack.empty() == true){
     cout << "List is empty" << endl;
  }
  //Creates a list iterator for int
  list<int>::iterator iter;

  //For range loop
  for(iter = list_stack.begin(); iter != list_stack.end(); iter++){
    cout << *iter << endl; //dereferences the iter pointer
  }
}

/*Take the top two elements of the stack/front two elements of the queue, perform whatever operation the user gives 
(+, -, *, /, or %) and take the result and push it to the stack/queue.*/
void Stack::math_first_two(string math_choice){
   int first = list_stack.front();
   list_stack.pop_front();
   int second = list_stack.front();
   list_stack.pop_front();
   
   if(math_choice == "+"){
      list_stack.push_front(first+second);
   }else if(math_choice == "-"){
      list_stack.push_front(first-second);
   }else if(math_choice == "*"){
      list_stack.push_front(first*second);
   }else if(math_choice == "/"){
      list_stack.push_front(first/second);
   }else if(math_choice == "%"){
      list_stack.push_front(first%second);
   }else{
      cout << "Not a valid math operator" << endl;
   }
}
  
//Returns the legnth of the list  
int Stack::length(){
   size = list_stack.size();
   return size;
}
