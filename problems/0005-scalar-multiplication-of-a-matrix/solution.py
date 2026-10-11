def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [[values*scalar for values in rows]for rows in matrix ]
	return result