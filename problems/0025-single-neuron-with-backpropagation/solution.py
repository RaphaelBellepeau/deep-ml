import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	updated_weights = initial_weights
	updated_bias = initial_bias
	sigmoid = lambda x: 1/(1+np.exp(-x))
	mse_values = []
	for epoch in range(epochs):
		z = updated_weights.dot(np.transpose(features)) + updated_bias
		output = sigmoid(z)
		MSE = np.mean((output - labels)**2)
		mse_values.append(MSE)
		grad_w = (2/len(features)) * np.transpose(features).dot((output - labels) * (output*(1-output)))
		grad_b = (2/len(features)) * sum((output - labels) * (output*(1-output)))

		updated_weights -= learning_rate * grad_w
		updated_bias -= learning_rate *grad_b


	return updated_weights, updated_bias, mse_values