import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    numerical_gradient = np.zeros_like(x, dtype=float)
    for i in range(x.shape[0]):
        x_plus = x.copy();  x_plus[i]  += epsilon
        x_minus = x.copy(); x_minus[i] -= epsilon
        numerical_gradient[i] = (f(x_plus) - f(x_minus)) / (2 * epsilon)
    rel_error = np.linalg.norm(analytical_grad - numerical_gradient) / (
        np.linalg.norm(numerical_gradient) + np.linalg.norm(analytical_grad)
    )
    return (numerical_gradient, rel_error)
