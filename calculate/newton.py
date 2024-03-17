from scipy.optimize import root
import numpy as np
from config import (m, g, k, theta, v0, h)

def equation(t):
    return (
        (m * g / k) * t
        - ((m * g / k - v0 * np.sin(theta)) * (-m / k) * (np.exp(-k * t / m) - 1))
        - h
    )


def solve():
    t_guess = 1.0

    result = root(equation, t_guess)

    if result.success:
        t_solution = result.x[0]
        print(f"The shot put is in the air for {t_solution:.2f} seconds")
        return t_solution
    else:
        print("No solution found")
