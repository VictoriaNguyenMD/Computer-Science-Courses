//This file is the class function file

//Allows us to access the class header file
#include "LinkedList.h"

//Append function
void LinkedList::append(char val){
   Node* tmp = new Node; //Creates a temporary Node 
   tmp->data = val; //Assigns the temporary Node's data to val
   
   if(head == NULL){ //Empty LinkedList
      head = tmp;
      tail = tmp;
   }
   else{
      tail->nxt = tmp; //The last Node's nxt is assigned to the temporary Node
      tail = tmp; //Reassigns the tail ponter to the last Node
   }
   
   
}