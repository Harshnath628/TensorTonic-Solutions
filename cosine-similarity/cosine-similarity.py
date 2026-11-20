import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a,dtype=np.float32)
    b = np.asarray(b,dtype=np.float32)
    dot = np.dot(a,b)
    norm_a = np.sqrt(np.dot(a,a))
    norm_b = np.sqrt(np.dot(b,b))
    if not( norm_a and norm_b): return 0.0
    return float(dot/(norm_a*norm_b))