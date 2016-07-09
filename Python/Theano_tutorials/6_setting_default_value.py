"""

2016-07-04-15:52:19

arhik

"""

"""
    The aim of this script is to show you how to set the default values of an
    Argument
"""


import theano.tensor as T
from theano import In, function

x,y = T.dscalars('x','y')
z = x+y
f = function([x, In(y, value=1)],z)
print(f(23))
