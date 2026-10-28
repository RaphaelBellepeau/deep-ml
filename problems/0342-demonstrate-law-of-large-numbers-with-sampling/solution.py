import numpy as np

def law_of_large_numbers(n_samples: int, population_mean: float, population_std: float) -> float:
   return (1/n_samples) * sum(np.random.normal(population_mean,population_std) for i in range(n_samples))