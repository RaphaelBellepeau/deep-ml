import numpy as np

def simulate_clt(distribution: str, n: int, runs: int = 10000, seed: int = 42) -> dict:
    np.random.seed(seed)
    match distribution:

        case 'uniform':
            table = np.random.uniform(0, 1, size=(runs, n))
            table = np.mean(table, axis = 1)
            standarzation = lambda x: (x - 0.5)/(np.sqrt(1/12)/ np.sqrt(n))
            table = standarzation(table)
            return {'mean': np.mean(table, axis = 0), 'std': np.std(table, axis = 0)}
        case 'exponential':
            table = np.random.exponential(1.0, size=(runs, n))
            table = np.mean(table, axis = 1)
            standarzation = lambda x: (x - 1)/(1/ np.sqrt(n))
            table = standarzation(table)
            return {'mean': np.mean(table, axis = 0), 'std': np.std(table, axis = 0)}
        case 'bernoulli':
            table = (np.random.rand(runs, n) < 0.3).astype(float)
            table = np.mean(table, axis = 1)
            standarzation = lambda x: (x - 0.3)/(np.sqrt(0.3*0.7)/ np.sqrt(n))
            table = standarzation(table)
            return {'mean': np.mean(table, axis = 0), 'std': np.std(table, axis = 0)}

    
    