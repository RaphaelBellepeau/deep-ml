def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) == len(b):
		return [sum(m * v for m,v in zip(rows, b)) for rows in a]
	else:
		return -1