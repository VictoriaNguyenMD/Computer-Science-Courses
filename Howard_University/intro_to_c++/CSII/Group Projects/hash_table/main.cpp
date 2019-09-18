#include "Hash.h"
#include <fstream>

int main(){
   //Creates a hashTable and sets the size for it
   vector<Candidate> hashTable;
   hashTable.resize(50);
   ifstream inFS;
   string inFS_name = "candidates.txt";
   
   inFS.open(inFS_name);
   
   if(!inFS.is_open()){
      cout << "There is an error with opening the file." << endl;
      
   }

   while(inFS.good()){
      Candidate cand;
      getline(inFS, cand.name);
      Hash::HashInsert(hashTable, cand.name);
   }
   
   cout << "Enter an option:" << endl;
   cout << "A: Add candidate" << endl;
   cout << "V: Vote for a candidate" << endl;
   cout << "F: Find Candidate" << endl;
   cout << "D: Display candidates" << endl;
   cout << "L: Find Leader" << endl;
   cout << "X: Exit the program" << endl;
   
   string option;
   getline(cin, option);

   while(option != "x" and option != "X"){
      if(option == "a" or option == "A"){
         Candidate cand;
         getline(cin, cand.name);
         Hash::HashInsert(hashTable, cand.name);
      }else if(option == "v" or option == "V"){
         Candidate cand;
         getline(cin, cand.name);
         Hash::Vote(hashTable, cand.name);
      }else if(option == "f" or option == "F"){
         Candidate cand;
         getline(cin, cand.name);
         cout << "Name: " << cand.name << endl;
         cout << "Votes: " << Hash::FindCandidate(hashTable, cand.name) << endl;
      }else if(option == "d" or option == "D"){
         //Print HashTable
         Hash::Print(hashTable);
      }else if(option == "l" or option == "L"){
         Hash::FindLeader(hashTable); 
      }else{
         cout << "Invalid option." << endl;
      }
      
      getline(cin, option);
   }
   
   return -1;
}