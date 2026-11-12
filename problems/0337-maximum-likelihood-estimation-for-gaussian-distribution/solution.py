import numpy as np

def gaussian_mle(data: np.ndarray) -> tuple:
    return (data.mean(), sum(((x - data.mean())**2)/len(data) for x in data))