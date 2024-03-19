import torch
from calculate.config import get_config

def f(t, m, g, k, v0, theta, h):
    term1 = (m * g / k) * t
    term2 = (m * g / k - v0 * torch.sin(theta)) * (-m / k) * (torch.exp(-k * t / m) - 1)
    return term1 - term2 - h

def newtons_method(func, initial_t, m, g, k, v0, theta, h, tolerance=1e-7, max_iterations=1000):
    t = initial_t.clone().detach().requires_grad_(True)  # Ensure t is a leaf tensor
    for iteration in range(max_iterations):
        value = func(t, m, g, k, v0, theta, h)
        if abs(value.item()) < tolerance:
            print(f"Converged in {iteration} iterations.")
            return t
        value.backward()
        if t.grad is None or t.grad.item() == 0:
            print("Zero gradient encountered. Stopping.")
            return t
        with torch.no_grad():  # Temporarily disable gradient tracking
            t -= value / t.grad  # Newton's update without tracking this operation
            t.grad.zero_()  # Reset the gradient for the next iteration
    print("Maximum iterations reached without convergence.")
    return t

def equation_torch(initial_t: float):
    _m, _g, _k, _theta, _v0, _h = get_config()

    m = torch.tensor(_m, requires_grad=True) # mass
    g = torch.tensor(_g, requires_grad=True)  # gravity
    k = torch.tensor(_k, requires_grad=True)  # air resistance constant
    theta = torch.tensor(_theta, requires_grad=True)  # launch angle
    v0 = torch.tensor(_v0, requires_grad=True)  # initial velocity
    h = torch.tensor(_h, requires_grad=True)  # release height

    # Initial guess for t
    initial_t = torch.tensor(initial_t, requires_grad=True)

    # Calculate
    t_solution = newtons_method(f, initial_t, m, g, k, v0, theta, h)
    print("Solution for t:", t_solution.item(), "with grad:")

    return t_solution


if __name__ == '__main__':
    equation_torch(1.0)