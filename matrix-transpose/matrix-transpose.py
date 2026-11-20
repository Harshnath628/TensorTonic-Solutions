import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    #1.matrix method
    a = np.asarray(A) #creating  nparray
    m,n= a.shape
    b = np.zeros((n,m),dtype=a.dtype) #creating temp nparray
    for i in range(n):
        for j in range(m):
            b[i,j]=a[j,i]
    return b
