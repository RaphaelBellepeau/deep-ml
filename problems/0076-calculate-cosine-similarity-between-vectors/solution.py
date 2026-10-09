import numpy as np

def cosine_similarity(v1, v2):
	dot = v1.dot(v2)
	norm1, norm2 = 0.0, 0.0
	v1, v2 = v1**2, v2**2
	for x in v1:
		norm1 += x
	for x in v2:
		norm2 += x
	return dot/(norm1**(1/2) * norm2**(1/2))