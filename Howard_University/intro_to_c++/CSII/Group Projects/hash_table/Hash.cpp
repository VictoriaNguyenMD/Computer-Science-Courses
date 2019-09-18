#include "Hash.h"

int Hash::HashVal(vector<Candidate> &hashTable, string item){
   return (item.size()%hashTable.size());
}

bool Hash::HashInsert(vector<Candidate> &hashTable, string item){
   //Check in list
   if(Hash::checkInHashTable(hashTable, item) == true){
      cout << item << " is already a candidate" << endl;
      exit(EXIT_FAILURE);
   }
  // Hash function determines initial bucket
  int bucket = HashVal(hashTable, item);     
  int bucketsProbed = 0;
  int vector_size = hashTable.size();

   while (bucketsProbed < vector_size) {
     // Insert item in next empty bucket 
     if ((hashTable[bucket].name).empty()) {
        hashTable[bucket].name = item;
        return true;  
     }

      // Increment bucket index
     bucket = (bucket + 1) % vector_size;

      // Increment number of buckets probed
     ++bucketsProbed;
  }

   return false;      
}

void Hash::Print(vector<Candidate> &hashTable){
   for(Candidate cand: hashTable){
      cout << "Name: " << cand.name << endl;
      cout << "Votes: " << cand.votes << endl;
      cout << "********************************" << endl;
   }
}


void Hash::Vote(vector<Candidate> &hashTable, string item){
   if(Hash::checkInHashTable(hashTable, item) == false){
      cout << item << " is not a candidate" << endl;
      exit(EXIT_FAILURE);
   }
   
   for(Candidate &cand: hashTable){
      if(cand.name == item){
         cand.votes = cand.votes + 1;
      }
   }
}

int Hash::FindCandidate(vector<Candidate> &hashTable, string item){
   if(Hash::checkInHashTable(hashTable, item) == false){
      cout << item << " not found" << endl;
      exit(EXIT_FAILURE);
   }
   
   for(Candidate cand: hashTable){
      if(cand.name == item){
         return cand.votes;
      }
   }
   
   return -1;   
}

void Hash::FindLeader(vector<Candidate> &hashTable){
   int highestVotes = 0;
   int secondHighest = 0;
   Candidate leader;
   
   for(Candidate cand: hashTable){
      if(cand.votes > highestVotes){
         secondHighest = highestVotes;
         highestVotes = cand.votes;
         leader = cand;
      }
   }

   int diff = highestVotes - secondHighest;
   
   cout << leader.name << " is leading the race with " << diff << " votes" << endl;
}

bool Hash::checkInHashTable(vector<Candidate> &hashTable, string item){
   for(Candidate cand: hashTable){
      if(cand.name == item){
         return true;
      }
   }
   return false;
}
