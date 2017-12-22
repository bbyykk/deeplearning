#!/usr/bin/python3
def relu(x):
    return np.maximum(0, x)

import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)    # siat-tīng y kuainn ê huān-uî
plt.show()
