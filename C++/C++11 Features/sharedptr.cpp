//reference counted version of unique_ptr 
// additional runtime features
// cool but aware of it 

#include <iostream>
#include <memory>

using namespace std;
auto main() -> int
{
    auto sp = shared_ptr<int> {};
    if(sp.use_count()==0)
        cout << "zero count" << endl;
    if(sp.unique())
        cout << "Its uniques" << endl;

    // sp.reset(new int {123});

    sp = make_shared<int>(123);
    
    cin.get();
}