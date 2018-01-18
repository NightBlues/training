#include <string>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <set>
// #include <cstdlib>
using namespace std;

template <class T>
const vector<T> input_array(int total) {
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

template <class K, class T>
void show(const map<K, T> & mapping) {
  for(auto it = mapping.begin(); it != mapping.end(); it++) {
    cout << (*it).first << " -> " << (*it).second << endl;
  }
}

class PrefixTree {
  map<char, char> table = {
    {'i', '1'}, {'j', '1'},
    {'a', '2'}, {'b', '2'}, {'c', '2'},
    {'d', '3'}, {'e', '3'}, {'f', '3'},
    {'g', '4'}, {'h', '4'},
    {'k', '5'}, {'l', '5'},
    {'m', '6'}, {'n', '6'},
    {'p', '7'}, {'r', '7'}, {'s', '7'},
    {'t', '8'}, {'u', '8'}, {'v', '8'},
    {'w', '9'}, {'x', '9'}, {'y', '9'},
    {'o', '0'}, {'q', '0'}, {'z', '0'},
  };
  vector<pair<string, array<int, 10>>> tree;
  int addVertex() {
    array<int, 10> v = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
    tree.push_back(make_pair("", move(v)));
    return tree.size() - 1;
  }
  // important optimization:
  // if we already added to queue variant where we have
  // the same number of symbols from phone left
  // we dont add current choice even if consist of other words
  set<int> parsed;
public:
  PrefixTree() { // const vector<string> && words) {
    addVertex();
    // for(auto word: words) {
    //   addWord(word);
    // }
    // tree.resize(tree.size());
  };

  void addWord(const string & word) {
    int vertex = 0;
    for(char symbol: word) {
      char symbol_tr = this->table.at(symbol);
       int num = (int)(symbol_tr) - 48;
      array<int, 10> & edges = tree[vertex].second;
      if(edges[num] != -1) {
        vertex = edges[num];
      } else {
        int new_vertex = addVertex();
        tree[vertex].second[num] = new_vertex;
        vertex = new_vertex;
      }
    }
    tree[vertex].first = word;
  };

  void consume(const string & phone, string & prefix,
               queue<pair<string, string>> & result) {
    int vertex = 0;
    auto it = phone.begin();
    for(; it != phone.end(); it++) {
      if(tree[vertex].first.compare("") != 0 &&
         parsed.count(distance(it, phone.end())) == 0) {
        string next_prefix = prefix.length() == 0 ? prefix : prefix + " ";
        next_prefix.append(tree[vertex].first);
        string rest_phone = phone.substr(distance(phone.begin(), it));
        parsed.insert(distance(it, phone.end()));
        result.push(make_pair(move(rest_phone), move(next_prefix)));
      }
      int num = (int)(*it) - 48;
      int next_vertex = tree[vertex].second[num];
      if(next_vertex == -1) {
        break;
      }
      vertex = next_vertex;
    }

    if(tree[vertex].first.compare("") != 0 &&
       parsed.count(distance(it, phone.end())) == 0) {
      string next_prefix = prefix.length() == 0 ? prefix : prefix + " ";
      next_prefix.append(tree[vertex].first);
      string rest_phone = phone.substr(distance(phone.begin(), it));
      parsed.insert(distance(it, phone.end()));
      result.push(make_pair(move(rest_phone), move(next_prefix)));
    }
  };

  void show() {
    for(auto it = tree.begin(); it != tree.end(); it++) {
      for(auto elt: (*it).second) {
        cout << elt << " ";
      }
      cout  << " (" << (*it).first << ")" << endl;
    }
  };
};


int main() {
  string phone;
  int words_count;
  while(true)
  {
    cin >> phone;
    if(phone.compare("-1") == 0) {
      break;
    }
    cin >> words_count;
    // vector<string> words = input_array<string>(words_count);
    // PrefixTree tree = PrefixTree(input_array<string>(words_count));
    PrefixTree tree;
    for(int i=0; i < words_count; i++){
      string word;
      cin >> word;
      tree.addWord(word);
    }
    // tree.show();
    queue<pair<string,string>> variants;
    variants.push(make_pair(phone, ""));
    pair<string, string> res;
    while(!variants.empty()) {
      res = variants.front();
      variants.pop();
      if(res.first.length() == 0) {
        break;
      }
      tree.consume(res.first, res.second, variants);
    }
    if(res.first.length() == 0) {
      cout << res.second << endl;
    } else {
      cout << "No solution." << endl;
    }
  }
  
  return 0;
}
