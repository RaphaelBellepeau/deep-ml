def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	s = 0
	if mode == 'row':
		for rows in matrix:
			for value in rows:
				s += value
			means.append(s/len(rows))
			s = 0
	else:
		for i in range(len(matrix[0])):
			for columns in matrix:
				s += columns[i]
			means.append(s/len(matrix))
			s = 0
	return means
	