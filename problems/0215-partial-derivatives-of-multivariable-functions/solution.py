import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	match func_name:
		case 'poly2d':
			return (2*point[0]*point[1] + point[1]**2, 2*point[1]*point[0] + point[0]**2 )
		case 'exp_sum':
			return (np.exp(point[0] + point[1]), np.exp(point[0] + point[1]))
		case 'product_sin':
			return (np.sin(point[1]), point[0]*np.cos(point[1]))
		case 'poly3d':
			return (2*point[0]*point[1], (point[0]**2) + point[2]**2, 2*point[1]*point[2])
		case 'squared_error':
			return (2*point[0] - 2*point[1], 2*point[1] - 2*point[0])
			