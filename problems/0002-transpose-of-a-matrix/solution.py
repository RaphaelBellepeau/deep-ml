def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []
    data = []
    for columns in range(len(a[0])):
        for rows in range(len(a)):
            data.append(a[rows][columns])
        b.append(data)
        data = []
    return b