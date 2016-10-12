#include <iostream>
#include <vector>
//auto and decltype

//auto to variables , decltype is general 

//DRY

//Higher level of abstraction

//type changes are better localized

//Easier refactoring

//simpler template code

//declaring variables
//  |_ auto allows to use lambda expressions
// alsways use auto 

// -ve code comprehension problem ? benefit > 

//mixed declaration not allowed
// const and volatile specifiers are removed
//arrays and functions are turned into pointers
using namespace std;

auto a=5.0, b = 10.0;

const std::vector<int> values;

auto add(double a, double b)
{
    return a+b;
}

auto f = add; //f is a pointer to fun
auto& g = add; // g is a reference to add

//explicit constructor then cop
auto main() -> int
{
    cin.get();
}
