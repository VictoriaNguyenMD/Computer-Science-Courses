/* 
Victoria Nguyen
@02762017

Lab 6: Creating Separate Files for Classes

[Step 1]: Create a ClassName.h, ClassName.cpp,and a main file. 
[Step 2]: Write the #include guards in order to prevent the header file from being included multiple times in the cpp file. Refer to this for further information https://stackoverflow.com/questions/3246803/why-use-ifndef-class-h-and-define-class-h-in-h-file-but-not-in-cpp
[Step 3]: Write the class for ItemToPurchase containing private and public members in the h file. This is known as the "Class declaration" header file.
[Step 4]: In the cpp file, create a default and non default constructor.
[Step 5]: Write functions within the cpp file corresponding to the ItemToPurchase class
[Step 6]: Create a vector in main storing objects of ItemToPurchase type
[Step 7]: Use a for loop to loop through the objects and ask the user details about each object (name, price, quantity)


Note: cpp means C preprocessor. It processes the C program language before it is compiled
*/

#include <iostream>
#include <string>
using namespace std;

//Allows us to access the class header file
#include "ItemToPurchase.h"

//Initalizes a default constructor. A default constructor does not have a return type so no "void"
ItemToPurchase::ItemToPurchase(){
  itemName = "none";
  itemPrice = 0;
  itemQuantity = 0;
}

//Initalize SetName Mutator
void ItemToPurchase::SetName(string name){
  itemName = name;
}

//Initalize GetName Accessor
string ItemToPurchase::GetName(){
  return itemName;
}

//Initalize SetPrice Mutator
void ItemToPurchase::SetPrice(int price){
  itemPrice = price;
}

//Initalize GetPrice Accessor
int ItemToPurchase::GetPrice(){
  return itemPrice;
}

//Initalize SetQuantity Mutator
void ItemToPurchase::SetQuantity(int quantity){
  itemQuantity = quantity;
}

//Initalize GetQuantity Accessor
int ItemToPurchase::GetQuantity(){
  return itemQuantity;
}