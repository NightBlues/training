#include <iostream>
#include <vector>

#include "test_framework.cpp"

using namespace std;

template<class T>
void insert_sort(vector<T> & v) {
  for(unsigned int i=0; i < v.size(); i++) {
    for(unsigned int j=0; j < i; j++) {
      if(v[i] < v[j]) {
        T tmp = v[i];
        for(unsigned int k=i; k > j; k--) {
          v[k] = v[k-1];
        }
        v[j] = tmp;
        break;
      }
    }
  }
}

void test_sorting() {
  vector<int> sorted = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  vector<int> a = {3, 9, 7, 8, 6, 0, 1, 2, 4, 5};
  assertVectorEqual(sorted, sorted);
  insert_sort(a);
  assertVectorEqual(a, sorted);
  a = {0, 1, 2, 3, 4};
  assertExpr(a.size() == 5);
  insert_sort(a);
  assertVectorEqual(a, vector<int>({0, 1, 2, 3, 4}));
}


int main() {
  test_sorting();
  
  return 0;
}
