# This is a matrix algebra function library for Python.
# Jaakko Astikainen, 2021

import numpy as np

def matsum(A, B):
    dims = np.shape(A)
    dim_m = dims[0] - 1
    dim_n = dims[1] - 1
    C = np.zeros((dim_m, dim_n))
    if np.shape(A) != np.shape(B):
        print("\nThe matrix dimensions do not match, you can sum two matrices of size m * n.\n")
    else:
        for i in range(0,dim_m):
            for j in range(0, dim_n):
                C[i, j] = A[i, j] + B[i, j]
    return C

#def matmult(A, B):