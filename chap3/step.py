#!/usr/bin/python3
def step_function(x):
    return np.array( x > 0, dtype=np.int)

import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)    # siat-tīng y kuainn ê huān-uî
plt.show()
