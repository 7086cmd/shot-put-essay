import torch
from calculate.config import set_config
from calculate.calculate import displacement
import numpy as np
from .extend import print_extend

theta = torch.tensor([1.0], requires_grad=True)
v0 = torch.tensor([-12.0], requires_grad=True)
h = torch.tensor([2.0], requires_grad=True)
g = 9.787

v0_range = (-13.5, -10.0)
h_range = (1.6, 2.1)
theta_range = (0, np.radians(60))

learning_rate = 0.001
iterations = 10000


def optimize():
    global theta, v0, h
    for i in range(iterations):
        function = (
            v0 * torch.cos(theta) * ((v0**2 * torch.sin(theta) ** 2 + 2 * h * g) ** 0.5)
            - v0 * torch.sin(theta)
        ) / g
        function = -function

        function.backward()

        with torch.no_grad():
            theta += learning_rate * theta.grad
            v0 += learning_rate * v0.grad
            h += learning_rate * h.grad

            theta.clamp_(*theta_range)
            v0.clamp_(*v0_range)
            h.clamp_(*h_range)

            theta.grad.zero_()
            v0.grad.zero_()
            h.grad.zero_()

    print("Optimized theta (radian): %.2f" % theta.item())
    print("Optimized theta (degree): %.2f" % np.degrees(theta.item()))
    print("Optimized v0: %.2f" % v0.item())
    print("Optimized h: %.2f" % h.item())

    set_config(_theta=theta.item(), _v0=v0.item(), _h=h.item())
    displacement()

    print_extend(v0, h, theta)


if __name__ == "__main__":
    optimize()
