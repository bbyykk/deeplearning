#!/usr/bin/python3
import numpy as np

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[7,10],[8,11],[9,12]])
print(A.shape)
print(B.shape)
result = np.dot(A, B)
print(result)
