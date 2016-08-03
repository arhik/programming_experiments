import numpy

import theano.tensor as T

x = T.fmatrix()
# x is a TensorVariable instance

# T.fmatrix is an object of TensorType

x.type 
# TensorType(float32, matrix)

x = T.scalar('myvar', dtype='int32')

print(x.type)

x = T.iscalar('myvar')

print(x.type)

x = T.TensorType(dtype='int32', broadcastable=())('myvar')

print(x.type)
# All three should output TensorType(int32, scalar)


x = T.scalar()

print(x.type)
#TensorType(float64, scalar) default

x = T.scalar(name='var', dtype='float32')

print(x.type)

print(x.get_parents())

x = T.vector(name='var', dtype='float32')

print(x.type)

x = T.row(name='var', dtype='float32')

print(x.type)

x = T.fmatrix()

x.type

# Custom TensorType

dtensor5 = T.TensorType('float64', (False,)*5)

dtensor5.dtype # Its a bit non-standard should explore more

dtensor5.value_zeros((1,4)) # Why does it accept 1,4 should explore more

from theano import shared

x = shared(numpy.random.randn(3,4))

x.get_value()


# copying functions

import theano

import theano.tensor as T

state = theano.shared.
