#ifndef HASH_H
#define HASH_H

#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Candidate{
   string name;
   int votes = 0;
};

class Hash{
   public:
      static bool HashInsert(vector<Candidate> &hashTable, string item);   
      static int HashVal(vector<Candidate> &hashTable, string item);
      static void Vote(vector<Candidate> &hashTable, string item);
      static int FindCandidate(vector<Candidate> &hashTable, string item);
      static void FindLeader(vector<Candidate> &hashTable);
      static void Print(vector<Candidate> &hashTable);
      static bool checkInHashTable(vector<Candidate> &hashTable, string item);
   private:
      //string
};


#endif