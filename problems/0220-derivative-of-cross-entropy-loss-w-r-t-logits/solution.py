import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	S = sum(np.exp(l) for l in logits)
	softmax = lambda x: np.exp(x)/S 
	for i,x in enumerate(logits):
		logits[i] = softmax(x)
	
	logits[target] -= 1
	return logits