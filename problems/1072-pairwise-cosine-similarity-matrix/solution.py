import numpy as np

def pairwise_cosine_similarity(X):
   X_norms = np.linalg.norm(X, axis = 1, keepdims = True)
   X_norms = np.where(X_norms == 0, 1, X_norms)
   X = X/X_norms
   S = X.dot(X.transpose())
   S = np.round(S, decimals=4)
   return S