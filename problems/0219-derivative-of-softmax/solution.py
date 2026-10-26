import numpy as np
def softmax_derivative(x: list[float]) -> list[list[float]]:
	J = []
	S  = sum(np.exp(s) for s in x)
	softmax = lambda a:  np.exp(a)/S
	for i,y in enumerate(x):
		Ji = []
		for j,z in enumerate(x): 
			if j == i:
				Ji.append(softmax(z)*(1-softmax(z)))
			else:
				Ji.append(-softmax(y)*softmax(z))
		J.append(Ji)
	return J
