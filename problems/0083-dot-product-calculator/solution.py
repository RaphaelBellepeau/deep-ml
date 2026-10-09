import numpy as np

def calculate_dot_product(vec1, vec2):
	dot = 0
	for i in range(len(vec1)):
		dot += vec1[i]*vec2[i]
	return dot