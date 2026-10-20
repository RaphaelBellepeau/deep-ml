def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	def determinant(matrix):
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	trace = 0
	for i,x in enumerate(matrix):
		trace += x[i]
	if len(matrix) == 2:
		return (determinant(matrix), trace)
	else:
		M = matrix
		A = [[M[1][1],M[1][2]],[M[2][1],M[2][2]]]
		B = [[M[1][0],M[1][2]],[M[2][0],M[2][2]]]
		C = [[M[1][0],M[1][1]],[M[2][0],M[2][1]]]
		return (M[0][0] * determinant(A) - (M[0][1] * determinant(B)) + M[0][2] * determinant(C), trace)