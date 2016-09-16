#include <iostream>

struct Node
{
	char name[15];
	int value;
	int id;
	Node * parent;
	Node * child;
};

int main()
{
	int x;
	int y;
	char nameit[10] = "Hello";
	std::cout << nameit;
	
	//Node t initialize
	Node t;
	t.id = 1;
	
	//Node next initialize
	Node next;
	
	//Node linking
	t.child = &next;
	next.id  = 10;
	std::cout << (*t.child).id;
}


