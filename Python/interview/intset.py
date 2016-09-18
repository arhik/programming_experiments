#!/usr/bin/env python2

# Copyright (C) 2016  <arhik@groundsignal.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.




"""
This module defines the IntSet datastructure and
an is_subset function.
"""

class IntSet:
    """
    IntSet datastructure is a set datastructure with only
    Integers as elements
    """
    def __init__(self, a):
        """
        InsSet Initializer takes an list datastructure as input
        validates it and returns the dictionary of hashed elements
        as keys and elements as values

        @param a : list or tuple of integers. Can be empty. 
        
        @returns : None
        """
        assert hasattr(a, '__iter__')
        for i in a: self._validate(i)
        self.set_elems = {hash(item):item for item in a}
    
    @staticmethod
    def _validate(x):
        """
        Static method to validate the input list or tuple 
        datastructure. Raises TypeError if not integer type
        
        @param x : object to be checked for integer type.
        @returns : None

        """
        if not isinstance(x, int):
            raise TypeError("Only Integer Arrays are allowed")

    def __contains__(self,a):
        """
        Container protocol for IntSet. 
        Returns True if object 'a' is in IntSet

        @returns : True or False
        """
        if a in self.set_elems: # Since hash(int a) is an a 
            return True
        else:
            return False
        
    def __iter__(self):
        """
        Iterable protocol
        """
        for i in self.set_elems:
            yield i

    def __eq__(self, rhs):
        """
        Defines equality of IntSet objects
        """
        if not isinstance(rhs, IntSet):
            raise TypeError("Cannot compare IntSet with an unknown object")
        return self.set_elems == rhs.set_elems

    def __repr__(self):
        """
        Representation of IntSet object
        """
        return("IntSet with elements {}".format(set(self.set_elems)))

    def issubset(self,b):
        """
        Checks if IntSet 'b' is subset of 'self'.
        Raises TypeError if type of given input is not IntSet.

        @returns : True if subset
                   False if not subset
        """
        if not isinstance(b, IntSet):
            raise TypeError("Given input is not of IntSet type:")
        for i in b:
            if i not in self:
                return False
        return True


def is_subset(a, b):
    """
    Constructs IntSet objects of 'a' and 'b' list or tuple objects
    and tests is 'b' is a subset of 'a'

    @param a: Potential superset of 'b'
    @param b: Potential subset of 'a'

    @returns : True - if 'b' is subset of 'a'
               False - otherwise
    """
    try:
        a = IntSet(a)
        b = IntSet(b)
    except TypeError as e:
        print(e)
        raise e
    return(a.issubset(b))
