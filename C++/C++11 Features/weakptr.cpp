// #include <iostream>
// #include <memory>
// using namespace std;

// auto main() -> int
// {
//     auto sp = make_shared<int> (123);

//     auto wp = weak_ptr<int>{sp};

//     // wp = sp;
//     if (auto locked = wp.lock())
//         cout << "Locked" << endl;
//     if(wp.expired())
//         cout << "Expired" << endl;
    
// }