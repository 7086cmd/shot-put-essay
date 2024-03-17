import numpy as np
from .config import get_config
import torch


def equation(t_solution):
    m, g, k, theta, v0, h = get_config()
    if k == 0:
        return t_solution * v0 * np.cos(theta)
    return np.abs(v0) * np.cos(theta) * (m / k) * (1 - np.exp(-k / m * t_solution))


def equation_torch(t_solution: torch.float):
    m, g, k, theta, v0, h = get_config()
    m = torch.tensor([m], dtype=torch.float)
    g = torch.tensor([g], dtype=torch.float)
    k = torch.tensor([k], dtype=torch.float)
    theta = torch.tensor([theta], dtype=torch.float)
    v0 = torch.tensor([v0], dtype=torch.float)
    h = torch.tensor([h], dtype=torch.float)
    if k == 0:
        return t_solution * v0 * torch.cos(theta)
    return (
        torch.abs(v0)
        * torch.cos(theta)
        * (m / k)
        * (1 - torch.exp(-k / m * t_solution))
    )
