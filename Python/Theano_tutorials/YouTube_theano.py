import theano
import theano.tensor as T
from theano import pp

x = T.dmatrix('x')
s = 1/(1+T.exp(-x))

logistic = theano.function([x],s)
logistic([[0,1], [-1, -2]])

a, b = T.dmatrices('a', 'b')

diff = a - b

abs_diff = abs(diff)

diff_squared = diff**2

f = theano.function([a,b], [diff, abs_diff, diff_squared])

f([[31,2],[22,25]],[[1,2],[2,5]])


from theano import Param

x, y = T.dscalars('x','y')

z = x + y

f = theano.function([x, Param(y, default=1)], z)

from theano import In
f = theano.function([x, In(y, value=1)], z)

f(1)


from theano import shared

state = shared(0)

inc = T.iscalar('inc')

accumulator = theano.function([inc], state ,updates= [(state, state + inc)])

accumulator(0)

fn_of_state = state*2 + inc

foo = T.scalar(dtype= state.dtype)

skip_shared = theano.function([inc, foo], fn_of_state, givens=[(state, foo)])

print(skip_shared(23,43))

y = x**2
gy = T.grad(y, x)
pp(gy)



# Logistic regression

import numpy 

import theano

import theano.tensor as T

rng = numpy.random

N = 400

dim = 784

D = (rng.randn(N,dim), rng.randint(size=N, low=0, high=2))

training_steps = 10000

x = T.dmatrix('x')
y = T.dmatrix('y')
w = theano.shared(rng.randn(dim), name="w")
b = theano.shared(0., name='b')

print("Initial model:")
print(w.get_value())
print(b.get_value())

p_1 = 1/(1 + T.exp(-(T.dot(x,w)+b)))

prediction = p_1 > 0.5
xent = -y*T.log(p_1) - (1-y)*T.log(1-p_1)
cost = xent.mean() + 0.01*(w**2).sum()
gw, gb = T.grad(cost, [w,b])


# compile

train = theano.function(
        inputs = [x,y],
        outputs = [prediction, xent],
        updates = ((w, w-0.1*gw), (b,b-0.1*gb)))

predict = theano.function(inputs=[x], outputs=prediction)

# train

for i in range(training_steps):
    pred, err = train(D[0], D[1])

print("Final model:")
print(w.get_value())
print(b.get_value())
print("target values for D:")
print(D[1])
print("prediction on D:")

rng.random((3,4)) + 1j*rng.random((3,4))
