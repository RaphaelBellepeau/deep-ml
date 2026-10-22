import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    A = A.astype(float)
    rank = 0
    for columns in range(min(A.shape)):
        column = np.abs((A[columns:,columns]))
        if np.max(column) < tol:
            pass
        else:
            index_max  = np.argmax(column)
            A[columns], A[columns + index_max] = A[columns + index_max].copy(), A[columns].copy()
            for r in range(columns + 1, A.shape[0]):
                factor = A[r, columns] / A[columns, columns]
                A[r, columns:] -= factor * A[columns, columns:]
            rank += 1
    return rank