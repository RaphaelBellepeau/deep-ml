import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
	entropy = 0
	cross_entropy = 0
	for x,y in zip(P,Q):
		if x == 0:
			pass
		else:
			entropy += x*np.log(x)
			cross_entropy += x*np.log(y)
		
	return -entropy, -cross_entropy
			