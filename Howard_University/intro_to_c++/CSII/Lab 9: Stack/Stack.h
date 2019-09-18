#ifndef STACK_H
#define STACK_H

#include <iostream>
#include <list>
#include <iterator>
#include <string>

using namespace std;

//Creates a stack class that contains the functions for the stack
class Stack{
  //Last in, first out
  public:
    void push(int val); //Adds a value to the top
    void pop(); //Remove the top val (no return value)
    int peek(); //looks at the first value
    void print(); //print out the stack
    void math_first_two(string math_choice);
    int length();
    
  private:
    list<int> list_stack; //Creates object of list int
    int size;
};


#endif