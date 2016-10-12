// naked pointers are bad

//exclusively owns object to which it points

//can't be copoie

//can be moved

// make_unique 

// avoid explicit new 
#include <iostream>
#include <memory>

using namespace std;

                
            
        

struct Hen
{
    unsigned id;
    float eggs;

    Hen(unsigned id_, float egg_):
        id{id_},
        eggs{egg_}
    {
    }

    ~Hen()
    {
        cout<<"Hen is destroyed"<<endl;
    }
};

auto GetHen() -> unique_ptr<Hen>
{
    return make_unique<Hen>(3,4.23f);
}

auto UpdateHen(unique_ptr<Hen> hen) -> unique_ptr<Hen>
{
    hen -> eggs += 1.8f;
    return hen;
}

auto main() -> int
{
    // auto sp = unique_ptr<int> { new int {123}};
    // auto sp = make_unique<int> (123) //perfect forwarding 
    // auto hen = make_unique<Hen>(1,5.6f);
    // if (hen) 
    // cout<<"Before: Hen owns the pointer"<<endl;
    // auto hen2 = move(hen);
    // if (hen) 
    // cout<<"Hen owns the pointer"<<endl;
    // if(hen2)
    // cout<<"Hen2 owns the pointer"<< endl;
    // cin.get();
    // Hen copy = *hen;
    // Hen & ref = *hen;
    // Hen * ptr = hen.get(); //.release to release instead;
    // hen.reset(ptr);

    // auto hen = GetHen();
    // hen = UpdateHen(move(hen));
    // cout << hen->eggs << endl;

 
}