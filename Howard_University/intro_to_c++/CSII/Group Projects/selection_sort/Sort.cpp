#include "Sort.h"
#include <vector>

using namespace std;

template<typename MyType>
void Sort<MyType>::SelectionSort(MyType numbers){
   for (int i = 0; i < numbers.size() - 1; ++i) {

   // Find index of smallest remaining element
   int indexSmallest = i;
   for (int j = i + 1; j < numbers.size(); ++j) {

      if (numbers[j] < numbers[indexSmallest]) {
         indexSmallest = j;
      }
   }

   // Swap numbers[i] and numbers[indexSmallest]
   int temp = numbers[i];
   numbers[i] = numbers[indexSmallest];
   numbers[indexSmallest] = temp;
  }

  for(auto v: numbers)
    cout << v << endl;
 
}