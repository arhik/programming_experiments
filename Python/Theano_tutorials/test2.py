from theano import function, pp

import theano.tensor as T

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
print(pp(z))
