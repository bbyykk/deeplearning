#!/usr/bin/python3
def step_function(x):
    y = x > 0
    return y.astype(np.int)

import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)    # siat-tīng y kuainn ê huān-uî
plt.show()
