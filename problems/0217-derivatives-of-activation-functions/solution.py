import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	def sigmoid(x):
		return 1/(1+np.exp(-x))

	def tanh(x):
		return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
	def relu(x):
		if x > 0:
			return 1
		else:
			return 0
	return {'sigmoid': sigmoid(x)*(1-sigmoid(x)), 'tanh': 1 - tanh(x)**2, 'relu': relu(x)}

