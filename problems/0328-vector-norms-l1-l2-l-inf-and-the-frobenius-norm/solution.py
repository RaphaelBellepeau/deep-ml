import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    if norm_type == 'l1':
        norm = 0.0
        for x in np.nditer(np.abs(arr)):
            norm += x
        return norm
    if norm_type == 'l2':
        norm = 0.0
        for x in np.nditer(arr ** 2):
            norm += x
        return norm ** (1/2)
    if norm_type == 'linf':
        return float(np.max(np.abs(arr.flat)))
    if norm_type == 'frobenius':
        if arr.ndim == 2:
            norm = 0.0
            for x in np.nditer(arr ** 2):
                norm += x
            return norm ** (1/2)
        else:
            raise ValueError("expected 2d array")
    else:
        raise ValueError("norm type unknown")
