import numpy as np

def lu_decomposition(A: list) -> tuple:
	A = np.array(A, dtype=float)
	L = np.identity(len(A))
	U = np.zeros_like(A)
	for i in range(len(A)):
		for j in range(i,len(A)):
			U[i,j] = A[i,j] - sum(L[i,k]*U[k,j] for k in range(i))
			if j > i:
				L[j,i] = (1/U[i,i]) * (A[j,i] - sum(L[j,k] * U[k,i] for k in range(i)))
	return L,U