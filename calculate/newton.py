from scipy.optimize import root
import numpy as np
from .config import get_config


def equation(t):
    m, g, k, theta, v0, h = get_config()
    if k == 0:
        return 1 / 2 * g * t**2 + v0 * np.sin(theta) * t + h
    return (
        (m * g / k) * t
        - ((m * g / k - v0 * np.sin(theta)) * (-m / k) * (np.exp(-k * t / m) - 1))
        - h
    )


def equation_torch(t):
    import torch

    m, g, k, theta, v0, h = get_config()
    if k == 0:
        return 1 / 2 * g * t**2 + v0 * torch.sin(theta) * t + h
    return (
        (m * g / k) * t
        - ((m * g / k - v0 * torch.sin(theta)) * (-m / k) * (torch.exp(-k * t / m) - 1))
        - h
    )


def solve():
    t_guess = 1.0

    result = root(equation, t_guess)

    if result.success:
        t_solution = result.x[0]
        return t_solution
    else:
        raise ValueError("No solution found")
