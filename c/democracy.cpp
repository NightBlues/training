#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

template <class T>
const vector<int> input_array(T total) {
  vector<T> * res = new vector<T>();
  res->reserve(total);
  for(int i=0; i < total; i++) {
    T tmp;
    cin >> tmp;
    res->push_back(tmp);
  }

  return *res;
}


template <class T>
void show(const vector<T> & array) {
  for(auto elt: array) {
    cout << elt << " ";
  }
  cout << endl;
}


int main() {
	int total;
	cin >> total;
	vector<int> groups = input_array(total);
    sort(groups.begin(), groups.end());
    int quorum = 0;
    for(int i=0; i < total / 2 + 1; i++) {
      quorum += (int)ceil(float(groups[i]) / 2.0);
    }
    cout << quorum << endl;

    return 0;
}
