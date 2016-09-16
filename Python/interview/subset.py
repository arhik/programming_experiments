#!/usr/bin/env python

class Set:
    """
    This Set class takes the list of elements and makes a set of elements
    """
    __slots__ = 's'
    def __init__(self, arr):
        try:
            s = set(arr)
        except e:
            print(e)

    def __call__(self, arr):
        return set(arr)

t = Set([1,3,4,5])

print(list(t))


