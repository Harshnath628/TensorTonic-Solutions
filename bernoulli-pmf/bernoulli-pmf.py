import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.asarray(x,dtype=float)
    x = (p**x)*((1-p)**(1-x))
    return  {"pmf": x, "mean":float(p), "variance": float(p*(1-p))}