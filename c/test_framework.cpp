#include <string>
#include <vector>
#include <iostream>
#include <sstream>

// My awesome test framework =)
void assertTrue(std::string desc, bool expr) {
  std::cout << "assert " << desc << " ... " << (expr ? "Ok" : "Fail") << std::endl;
}

void assertEqual(std::string v1, std::string v2, bool expr) {
	assertTrue(v1 + " == " + v2, expr);
}

#define quote(x) #x
#define show_id(ctx, obj) cout << #ctx << ":ID(" << #obj << "): " << &(obj) << endl;
#define assertExpr(expr); assertTrue(quote(expr), expr);

#define assertExc_(expr, exc, res)  \
	assertTrue(string("Expr \"") + quote(expr) + \
	           string("\" throws exception ") + quote(exc), res); \

#define assertFails(expr, exc); \
	try{ \
		expr; \
		assertExc_(expr, exc, false); \
	} catch(exc & e) { assertExc_(expr, exc, true); }


// helpers
template <class T>
std::string show(const std::vector<T> & array) {
  std::ostringstream result;
  for(auto elt: array) {
    result << elt << " ";
  }

  return result.str();
}

#define showVector(v) quote(v) + std::string(" [") + show(v) + std::string("] ")
#define assertVectorEqual(vector1, vector2) \
  assertEqual(showVector(vector1), showVector(vector2), vector1 == vector2)
