# This is a testing script to run the library functions.
# Jaakko Astikainen, 2021

import matrixlib as mat
import numpy as np

# Write test script here

a = 4
b = 5
A = np.array(np.random.rand(a, b))
B = np.array(np.random.rand(a, b))
M = mat.matsum(A, B)
print(M)

