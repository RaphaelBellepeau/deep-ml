import numpy as np
def orthogonal_projection(v, L):
	v, L  = np.array(v), np.array(L)

	return (v.dot(L)/ L.dot(L)) * L
