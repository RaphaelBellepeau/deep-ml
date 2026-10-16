import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    return {'mean': np.mean(data), 'median':np.median(data),'mode': (v:=np.unique(data, return_counts=True))[0][np.argmax(v[1])] ,'variance': np.var(data),'standard_deviation': np.std(data), '25th_percentile':np.percentile(data, 25),'50th_percentile':np.percentile(data, 50), '75th_percentile':np.percentile(data,75), 'interquartile_range': np.percentile(data, 75) - np.percentile(data, 25)}
  