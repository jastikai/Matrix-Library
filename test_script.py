# This is a testing script to run the library functions.
# Jaakko Astikainen, 2021

import matrixlib as mat
import numpy as np

# Write test script here

a = 4
b = 9
A = np.array(np.random.rand(a, b))
B = np.array(np.random.rand(b, a))
print("\nThe sum of test matrices is:\n")
M_0 = mat.matsum(A, B)
#print(M_0)

M_1 = mat.matmult(A, B)
print("\nThe product of test matrices is:\n")
print(M_1)