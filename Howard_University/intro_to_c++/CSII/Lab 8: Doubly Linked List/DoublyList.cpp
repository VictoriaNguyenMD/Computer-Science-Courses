#include "NODE.h"
#include <iostream>
#include <string>

//Appends a Node to the end of the LinkedList
void LinkedList::Append(string dest, string flight){
  Node* insert_node = new Node();
  insert_node->flight.destination = dest;

  if(head == NULL){ //If LinkedList is empty
    head = insert_node;
    tail = insert_node;
  }else{
    insert_node->prev = tail;
    tail->next = insert_node;
    tail = insert_node;
  }

}

//Adds a Node to the beginning of the LinkedList
void LinkedList::Prepend(string dest, string flight){
  Node* insert_node = new Node();
  insert_node->flight.destination = dest;


  if(head == NULL){ //If LinkedList is empty
    head = insert_node;
    tail = insert_node;
  }else{
    head->prev = insert_node; //Makes the head's previous equal to the new node
    insert_node->next = head; //Assign's the head's next to new node
    head = insert_node; //Points head to the new node
  }
  
}

//Removes the first appearance of the Node with destination dest
void LinkedList::Remove(string dest, string flight){
  bool found = false; //Node is not found, then false
  Node* temp = head;
  Node* tmp_prev = NULL;
  Node* tmp_next = NULL;

  if(head == NULL){ //If LinkedList is empty
    cout << "Cannot remove Node. This LinkedList is empty." << endl;
  }

  while(temp != NULL){ //Traverses through the LinkedList
    if(head->flight.destination == dest){ //if the head is the correct value
      head = head->next;
      head->prev = NULL;
      found = true;
      break;
    }else if(temp->flight.destination == dest){//if a middle or tail value is the correct value
      if(temp == tail){ //if tail value
        tail = tail->prev;
        tail->next = NULL;
        found = true;
        break;
      }

      tmp_prev = temp->prev;
      tmp_next = temp->next;

      tmp_prev->next = tmp_next;
      tmp_next->prev = tmp_prev;
      found = true; 
      break;

    }else{
      temp = temp->next; //value was not found at the node so it checks the next node
    } 
  }

  if(found == false){//Node was not found in linked list
    cout << "There is no Node with this flight destination name." << endl; 
  }

}

//Prints the LinkedList in forward order
void LinkedList::Print(){
  Node* temp = head;
  int index = 1;
  
  while(temp != NULL){
    if(temp == tail && index != 1){
       cout << index << ". " << temp->flight.destination << " to " << head->flight.destination << endl;
       break;
    }
    
    cout << index << ". " << temp->flight.destination << " to " << temp->next->flight.destination << endl;
    index = index + 1;
    temp = temp->next;
  }
}

//Prints the list in the reverse order, considering the head is the beginning of the Linked List, then it goes to tail
void LinkedList::PrintReverse(){
  Node* temp = tail;
  int index = 1;
  
  while(temp != NULL && index <= 8){
     if(index ==  1){
       cout << index << ". " << head->flight.destination << " to " << tail->flight.destination << endl;
       index = index + 1;
      }
    
    cout << index << ". " << temp->flight.destination << " to " << temp->prev->flight.destination << endl;
    index = index + 1;
    temp = temp->prev;
  }
}