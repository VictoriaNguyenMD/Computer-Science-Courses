/*Once the header is included, it checks if a unique value (in this case HEADERFILE_H) is defined. 
Then if it's not defined, it defines it and continues to the rest of the page.*/

#ifndef NODE_H 
#define NODE_H 
#include <string>

using namespace std;

//Creates a struct of Flight
struct Flight{
  string flightNum = ""; 
  string destination = "";
};

//Creates a Node
struct Node{
  Flight flight;
  Node* prev = NULL;
  Node* next = NULL;
};

//Creates a class called LinkedList
class LinkedList{
  public:
    void Append(string dest = "None", string flight = "0136");//Created default values
    void Prepend(string dest = "None", string flight = "0136");
    void Remove(string dest = "None", string flight = "0136");
    void Print();
    void PrintReverse();
  private:
    Node* head = NULL;
    Node* tail = NULL;
};


#endif