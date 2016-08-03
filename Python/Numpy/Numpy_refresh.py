import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 50)

y = np.sin(x)

plt.plot(x,y)

plt.show()

x = np.random.rand(200)

y = np.random.rand(200)

size = np.random.rand(200)*50

color = np.random.rand(200)
plt.subplot(2,1,1)
scatter = plt.scatter(x,y,size,color)

plt.show()
