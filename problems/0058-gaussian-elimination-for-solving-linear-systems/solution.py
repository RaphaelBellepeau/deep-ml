import numpy as np

def gaussian_elimination(A, b):
	Ab = np.column_stack((A,b))
	def matrix_rank(A: np.ndarray, Ab,  tol: float = 1e-10) -> int:
		Ab = np.column_stack((A, b)).astype(float)
    
		num_rows, num_cols = A.shape  
		
		for columns in range(num_cols):
			column = np.abs(Ab[columns:, columns])
			
			if np.max(column) < tol:
				pass
			else:
				index_max = np.argmax(column)
				Ab[columns], Ab[columns + index_max] = Ab[columns + index_max].copy(), Ab[columns].copy()
				
				for r in range(columns + 1, num_rows):
					factor = Ab[r, columns] / Ab[columns, columns]
					Ab[r, columns:] -= factor * Ab[columns, columns:]
					
		return Ab
	Ab = matrix_rank(A, Ab)
	x = np.zeros(len(A))
	for i in range(len(A) - 1, -1, -1):
		sum_val = Ab[i, -1]
		for j in range(i + 1, len(A)):
			sum_val -= Ab[i, j] * x[j]
		x[i] = sum_val / Ab[i, i]
		
	return x.tolist()
