import numpy as np
from .config import get_config

def equation(t_solution):
    m, g, k, theta, v0, h = get_config()
    if k == 0:
        return t_solution * v0 * np.cos(theta)
    return np.abs(v0) * np.cos(theta) * (m/k) * (1 - np.exp(-k/m * t_solution))
