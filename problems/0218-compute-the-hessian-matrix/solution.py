from typing import Callable
import numpy as np

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
	vector = lambda n: h * np.eye(len(point))[n]

	point = np.array(point, dtype = float)
	hessian = np.zeros((len(point),len(point)))
	for i in range(hessian.shape[0]):
		for j in range(hessian.shape[0]):
			if i == j:
				hessian[i,j] = (f(point + vector(i)) - 2*f(point) + f(point - vector(i)))/(h**2)
			else:
				hessian[i,j] = (f(point + vector(i) + vector(j)) - f(point + vector(i) - vector(j)) - f(point - vector(i) + vector(j)) + f(point - vector(i) - vector(j)))/(4*(h**2))
	return hessian


	