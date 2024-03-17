from calculate.config import set_config
from calculate.calculate import displacement
import torch
import numpy as np


def get_disp(v0: torch.float, h: torch.float, theta: torch.float):
    set_config(_v0=v0, _h=h, _theta=theta)
    return displacement()


def extend(v0: torch.float, h: torch.float, theta: torch.float):
    v0_p = v0 + 0.1
    v0_m = v0 - 0.1
    h_p = h + 0.1
    h_m = h - 0.1
    theta_p = theta + np.radians(10)
    theta_m = theta - np.radians(10)

    disp_v0_p = get_disp(v0_p, h, theta)[0]
    disp_v0_m = get_disp(v0_m, h, theta)[0]
    disp_h_p = get_disp(v0, h_p, theta)[0]
    disp_h_m = get_disp(v0, h_m, theta)[0]
    disp_theta_p = get_disp(v0, h, theta_p)[0]
    disp_theta_m = get_disp(v0, h, theta_m)[0]

    return (
        ("v0", disp_v0_p, disp_v0_m),
        ("h", disp_h_p, disp_h_m),
        ("theta", disp_theta_p, disp_theta_m),
    )

def print_extend(v0: torch.float, h: torch.float, theta: torch.float):
    v0, h, theta = v0.item(), h.item(), theta.item()
    print(f"v0: {v0:.2f}, h: {h:.2f}, theta: {theta:.2f}")
    disp = get_disp(v0, h, theta)[0]
    print(f"Displacement: {disp:.2f}")
    print("Extending...")
    for name, p, m in extend(v0, h, theta):
        print(f"{name} +: {p:.2f} (diff: {p - disp:.2f}), {name} -: {m:.2f} (diff: {m - disp:.2f})")
    print("Done")
