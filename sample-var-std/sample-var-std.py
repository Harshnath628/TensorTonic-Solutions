import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x,dtype=float)
    mean = np.mean(x)
    squared_deviation = (x-mean)**2
    s2 = squared_deviation.sum()/(len(x)-1)
    return {"variance": float(s2), "standard_deviation": float(np.sqrt(s2))}
    
    