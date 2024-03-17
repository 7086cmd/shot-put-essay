import numpy as np

m = 4.0  # Mass of the shot put
g = 9.787  # Acceleration due to gravity
k = 0.00215  # Air resistance constant
theta = np.radians(37.0)  # Launch angle
v0 = -13.24  # Initial velocity
h = 2.08  # Release height

def set_config(_m = m, _g = g, _k = k, _theta = theta, _v0 = v0, _h = h):
    global m, g, k, theta, v0, h
    m = _m
    g = _g
    k = _k
    theta = _theta
    v0 = _v0
    h = _h

def get_config():
    return m, g, k, theta, v0, h
