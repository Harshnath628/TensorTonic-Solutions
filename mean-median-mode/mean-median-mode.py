from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x,dtype=float)
    a,b= np.unique(x,return_counts=True)
    p = max(list(zip(a,b)),key= lambda p:p[1])
    return {"mean":float(np.mean(x)),"median":float(np.median(x)),"mode":float(p[0])}
    
    
    