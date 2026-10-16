def dice_statistics(n: int) -> tuple[float, float]:
	e = (1/n) * sum(i for i in range(1, n + 1))
	var =(1/n) * sum((i - e)**2 for i in range(1, n + 1))
	return (e,var)