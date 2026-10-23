import numpy as np

def calculate_correlation_matrix(X, Y=None):
	def correlation(A,B):
		Amean = np.mean(A, axis=0)
		Bmean = np.mean(B, axis=0)
		A_std = np.std(A, axis=0, ddof=1)
		B_std = np.std(B, axis=0, ddof=1)
		A_centered = A - Amean
		B_centered = B - Bmean
		At = A_centered.transpose()
		cov = At.dot(B_centered) / (A.shape[0] -1)
		corr  = cov / np.outer(A_std,B_std)
		return corr

	if Y is None:
		return correlation(X,X)
	else:
		return correlation(X,Y)
