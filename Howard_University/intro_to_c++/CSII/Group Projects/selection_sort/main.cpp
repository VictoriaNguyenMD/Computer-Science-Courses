#include <iostream>
#include "Sort.h"
#include "Sort.cpp"
#include <vector>

using namespace std;

int main() {
  vector<int> temp = {10, 2, 78, 4, 45};

  // for(auto v: temp){
  //   cout << v << endl;
  // }

  Sort<vector<int>>::SelectionSort(temp);
}