## The technical book I read.

The technical book I read recently is on google's 'Site reliability engineering. How google runs its production systems'. As a computer engineer I am always interested in fault tolerance, scalability and reliability of systems. This book walks through the history of google and gives us insight into google's production systems. I am still half way through and its touching every coursework I had in my masters. I wished for such book while I was studying those concepts. Also as aspirant of entrepreneurship this book also gave me an brief outline of what it takes to provide a reliable service. This is also a good resource to learn from google's mistakes. Hence I strongly recommend it.

## Regarding complexity of *is_subset* function. 

* Validation of input array in **IntSet** initializer is sequential pass through each element of array and check for *int* datatype. This has an O(n) complexity.
* Though *_validation* function is a bottleneck while construction of *Intset* object from *array* its good to check for invalid input.
* While construction of set is first part of the *is_subset* functionality the actual check for subset is done by checking for each element of *b*'s existance in the first *IntSet* datastructure *a*. If the *IntSet b* has *k* unique elements then the worst case complexity to check if *b* is a subset of *a*  is O(k) since the dictionary lookup is O(1).

Therefore the overall complexity of the *is_subset* function will be O(n).



-------
The Image below shows the locations of the top  5  closest users.


![Map of 5 users](https://github.com/arhik/programming_experiments/blob/master/Python/interview/images/top5ClosestUsers.png)
