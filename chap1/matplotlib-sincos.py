#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

### 添資料
# uì 0 到 6, 躘 0.1 
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

### 畫圖表
plt.plot(x, y1, label="sin")

### 予 cos 圖和 sin 無仝, 用短線節
plt.plot(x, y2, linestyle = "--", label="cos")

## x 標
plt.xlabel("x")
# y 標 
plt.ylabel("y")

# 主題
plt.title("sin kah cos")
plt.legend()
plt.show()

