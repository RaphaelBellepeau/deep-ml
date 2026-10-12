def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    b_transpose = [[b[j][i] for j in range(len(b))] for i in range(len(b[0]))]

    return [[sum(A * B for A, B in zip(a_rows, b_rows)) for b_rows in b_transpose] for a_rows in a]
	    