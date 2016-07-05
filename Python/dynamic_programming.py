#!/usr/env python

# dynamic_programming.py
#
# Copyright (C) 2016 arhik <karthik.katipalli@gmail.com>
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
    Dynamic programming example for finding edit distance of two strings
    Performance analysis of algorithm is also done to compare and contrast
    data structure selection for efficiency.
"""

from functools import wraps
import time

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn:" + fn.__name__ + " took " + str(t2-t1) + " seconds")
        return result
    return measure_time

@timefn
def editDistance1(s1, s2):
    m = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
    ops = [[-1]*(len(s2)+1) for i in range(len(s1)+1)]
    for i in range(len(s2)+1):
        m[0][i] = i
    for i in range(len(s1)+1):
        m[i][0] = i
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            cost = 1
            if(s1[i-1]==s2[j-1]):
                cost = 0
            replacecost = m[i-1][j-1] + cost
            removecost = m[i-1][j] + 1
            insertcost = m[i][j-1] + 1
            costs = [replacecost, removecost, insertcost]
            m[i][j] = min(replacecost, removecost, insertcost)
            ops[i][j] = costs.index(m[i][j])
    print("Edit distance is {2} \nGiven: \nstring1: {0} and \nstring2: {1}.\n".format(s1,s2,m[len(s1)][len(s2)]))
    return(m,ops)

@timefn
def editDistance2(s1, s2):
    # Need to think of more efficient implementation like optimize calls or
    # use cython just for fun

    m = [[0]*(len(s2)+1) for i in range(len(s1)+1)]
    ops = [[-1]*len(s2)+1 for i in range(len(s1)+1)]
    for i in range(len(s2)+1):
        m[0][i] = i
    for i in range(len(s1)+1):
        m[i][0] = i
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            cost = 1
            if(s1[i-1]==s2[j-1]):
                cost = 0
            replacecost = m[i-1][j-1] + cost
            removecost = m[i-1][j] + 1
            insertcost = m[i][j-1] + 1
            costs = [replacecost, removecost, insertcost]
            m[i][j] = min(replacecost, removecost, insertcost)
            ops[i][j] = costs.index(m[i][j])
    print(m[len(s1)][len(s2)])
    return((m, ops))


@timefn
def editDistance_operations(s1,s2):
    REPLACE = 0
    REMOVE  = 1
    INSERT  = 2
    sol_map, ops = editDistance1(s1,s2)
    (i,j) = (len(s1),len(s2))
    while(i != 0 or j!=0):
        if ops[i][j] == REMOVE or j==0:
            print("REMOVE operation \n\t\t - {0} is removed ".format(s1[i-1]))
            i -= 1
        elif ops[i][j] == INSERT or i==0:
            print("INSERT operation: \n\t\t - {0} is inserted".format(s1[i-1]))
            j -= 1
        else:
            if(sol_map[i-1][j-1]!=sol_map[i][j]):
                print("Replace operation: \n\t\t - {0} is replaced with {1}".format(s1[i-1], s2[j-1]))
            i -=1
            j -=1

def main():
    editDistance_operations("OJIJDFIJUSDLFIJHSDLIHSDLFKJHSDIFUOSEFJLKSJDFLSKJSDIOFUSLDKJFS","JOIJSDFLKJSDGLKJSDVOINZ><MCOPIJSDFPOSDFSDFCTCA")

if __name__ == "__main__":
    main()
