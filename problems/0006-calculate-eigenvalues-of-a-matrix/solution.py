import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = matrix[0][0] + matrix[1][1] 
	det  = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

	return [(trace + np.sqrt(trace**2 - 4*det))/2, (trace - np.sqrt(trace**2 - 4*det))/2]