#!/usr/bin/python3
def sigmoid(x):
    return 1 / ( 1 + np.exp(-x))

import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)    # siat-tīng y kuainn ê huān-uî
plt.show()
