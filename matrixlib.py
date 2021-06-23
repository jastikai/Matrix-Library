# This is a matrix algebra function library for Python.
# Jaakko Astikainen, 2021

import numpy as np

def matsum(A, B):
    dims = np.shape(A)
    dim_m = dims[0] - 1
    dim_n = dims[1] - 1
    C = np.zeros((dim_m, dim_n))
    if np.shape(A) != np.shape(B):
        print("\nThe matrix dimensions do not match, you can sum two matrices of size m x n.\n")
        return np.nan
    else:
        for i in range(0,dim_m):
            for j in range(0, dim_n):
                C[i, j] = A[i, j] + B[i, j]
    return C

def matmult(A, B):
    dims_A = np.shape(A)
    dims_B = np.shape(B)
    m_A = dims_A[0] - 1
    n_A = dims_A[1] - 1
    m_B = dims_B[0] - 1
    n_B = dims_B[1] - 1
    C = np.zeros((m_A, n_B))
    if n_A != m_B:
        print("\nThe matrix dimensions do not support matrix multiplication, for matrices with dimension m x n and o x p, it must be that n = o. \n")
        return np.nan
    else:
        for m in range(0, m_A):
            for n in range(0, n_B):
                C[m, n] = np.sum(A[m, n] * B[m, n])
    return C
