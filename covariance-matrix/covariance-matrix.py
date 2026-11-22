import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x = np.asarray(X,dtype=float)
    xc = x - np.mean(x,axis=0)
    sigma = np.dot(xc.T,xc)/(len(x)-1)
    return sigma