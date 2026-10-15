import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	grad_arr = np.array(gradient)
	magnitude = (sum(grad_arr**2))**(1/2)
	if magnitude == 0:
		return {'magnitude': magnitude, 'direction': np.zeros_like(grad_arr),'descent_direction':np.zeros_like(grad_arr)}

	
	return {'magnitude': magnitude, 
	'direction': grad_arr/magnitude,
	 'descent_direction':grad_arr/magnitude*-1}