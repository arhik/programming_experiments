#!/usr/bin/env python
# -*- coding: utf-8 -*-

# LCS.py
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
def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    L = [[0]*(m+1) for i in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1],L[i-1][j])
    print(L)
    return(L)

@timefn
def LCS_sol(s1,s2):
    L = LCS(s1,s2)
    sol = ""
    (i,j) = len(s1),len(s2)
    while L[i][j] > 0:
        if s1[i-1]==s2[j-1]:
            sol += str(s1[i-1])
            i -= 1
            j -= 1

        elif L[i-1][j] < L[i][j-1]:
            j -= 1
        else:
            i -= 1
    print("The LCS for given strings\n - string1: {}\n - string2 {}\n is {}".format(s1,s2,sol))
    return(sol)

def main():
    sol = LCS_sol("GTTCCTAATA","CGATAATTGAGA")

if __name__ == "__main__":
    main()
