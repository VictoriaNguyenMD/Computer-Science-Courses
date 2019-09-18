  //This file is the class declaration file

#ifndef LINKEDLIST_H 
#define LINKEDLIST_H

#include <iostream>

using namespace std;


//Creates an empty node
struct Node{
   char data = 0;
   Node* nxt = NULL;
};

//Creates a LinkedLisHt data structure type
class LinkedList{
   public:
      void append(char data); //Appends to the end
      void insertBefore(char node, char data); //Inserts before Node data value of node
      void insertAfter(char node, char data); //inserts after Node data value of node
      void print();
   private: 
     Node* head = NULL; //Indicates the begining of the LinkedList
     Node* tail = NULL; //Indicates the end of the LinkedList
};

#endif