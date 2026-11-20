import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.array(x, dtype=float)

    result = 1 / (1 + np.exp(-x))

    if result.ndim == 0:
        return float(result)

    return result
    pass