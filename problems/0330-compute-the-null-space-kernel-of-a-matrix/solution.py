import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    svd = np.linalg.svd(A)
    r = np.linalg.matrix_rank(A)
    return svd[2][r:].T