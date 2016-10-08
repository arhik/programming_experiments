#include <iostream>
#include <vector>

#include "Region.h"

int main()
{
    Region test;
    test.x = 5;
    test.setProfileEnable(false);

    std::cout << test.getProfileEnable() << std::endl;
    std::cout << "Hello. I am karthik." << std::endl;
    std::cout << test.x << std::endl;
    std::cin.get();
}
