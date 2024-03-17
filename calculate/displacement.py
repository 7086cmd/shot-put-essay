import numpy as np
from config import (m, g, k, theta, v0, h)

def equation(t_solution):
    return np.abs(v0) * np.cos(theta) * (m/k) * (1 - np.exp(-k/m * t_solution))
