#include <iostream>
#include <string>
#include <sstream>
#include <stdexcept>
#include <typeinfo>

using namespace std;

#define STAT_LIST(list); cout << list.str() << " length=" << list.length() << "; size="<< list.getSize() << endl;

class MyBase {
public :
	void say() {
		cout << "Hello MyBase" << endl;
	}
};

class MySub : public MyBase {
public:
	void say() {
		cout << "Hello MySub" << endl;
	}
};


template <class T>
class DynamicList {
	T* elements;
	int base_size, size, current_max;

	int abs_index(int index) {
		if(index < 0) {
			index += current_max;
		}
		if(index < 0 || index > current_max) {
			throw out_of_range("Index out of range");
		}
		return index;
	}

	int calc_optimal_size() {
		int new_size = size;
		if(current_max == size) {
			new_size = size * 2;
		} else if (size >= current_max * 4) {
			new_size = size / 2;
		}

		if(new_size <= base_size) {
			new_size = base_size;
		}

		return new_size;
	}

	void reallocate() {
		if(calc_optimal_size() == size) {
			return;
		}
		// cout << "reallocating: " << calc_optimal_size() << endl;
		T* oldelements = elements;
		size = calc_optimal_size();
		elements = new T[size];
		for(int i=0; i < current_max; i++) {
			elements[i] = oldelements[i];
		}
		delete [] oldelements;
	}

public:
	DynamicList() : base_size(10), size(base_size), current_max(0) {
		elements = new T[size];
	}
	~DynamicList() {
		delete [] elements;
	}

	int length() {
		return current_max;
	}

	int getSize() {
		return size;
	}

	void append(T e) {
		reallocate();
		elements[current_max++] = e;
	}

	void remove(int index) {
		reallocate();
		index = abs_index(index);
		for(int i=index; i < current_max - 1; i++) {
			elements[i] = elements[i + 1];
		}
		current_max--;
	}

	string str() {
		ostringstream res;
		res << "[";
		for(int i=0; i < current_max; i++) {
			res << elements[i];
			if(i + 1 != current_max) {
				res << ", ";
			}
		}
		res << "]";
		return res.str();
	}

	T & operator[](int index) {
		index = abs_index(index);
		return elements[index];
	}
};


// My awesome test framework =)

void assertTrue(string desc, bool expr) {
	cout << "assert " << desc << " ... " << (expr ? "Ok" : "Fail") << endl;
}

void assertEqual(string v1, string v2, bool expr) {
	assertTrue(v1 + " == " + v2, expr);
}

#define quote(x) #x
#define assertExpr(expr); assertTrue(quote(expr), expr);

#define assertExc_(expr, exc, res)  \
	assertTrue(string("Expr \"") + quote(expr) + \
	           string("\" throws exception ") + quote(exc), res); \

#define assertFails(expr, exc); \
	try{ \
		expr; \
		assertExc_(expr, exc, false); \
	} catch(exc & e) { assertExc_(expr, exc, true); }


void test_list() {
	DynamicList<int> list = DynamicList<int>();
	for(int i = 0; i < 10; i++) {
		list.append(i);
	}
	assertExpr(list.length() == 10);
	list.append(100);
	assertExpr(list.length() == 11);
	assertExpr(list.getSize() == 20);
	for(int i=0; i < 6; i++) {
		list.remove(0);
	}
	assertExpr(list.length() == 5);
	assertExpr(list.getSize() == 20);
	list.remove(-1);
	assertExpr(list.length() == 4);
	assertExpr(list.getSize() == 10);
	// STAT_LIST(list);
	assertExpr(list[-2] == 8);
	// cout << "Second from end: " << list[-2] << endl;
	assertFails(list[5], out_of_range);
	// try {
	// 	cout << list[5] << endl;
	// } catch(out_of_range & e) {
	// 	cout << "Cought exception: " << e.what() << endl;
	// }
}

int main(int, char**) {
	// MySub my1 = MySub();
	// my1.say();
	test_list();

	return 0;
}
