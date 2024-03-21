import polars as pl
from .df import df
import numpy as np
from calculate.config import set_config
from calculate.calculate import displacement

loss, total = 0.0, 0.0

for row in df.rows():
    v = 0 - row[3]
    h = row[5]
    distance = row[2] - row[7]
    angle = np.radians(row[4])

    set_config(_v0=v, _h=h, _theta=angle)
    disp = displacement()[0]

    print(f"v0: {v:.2f}, h: {h:.2f}, theta: {angle:.2f}")

    print(f"Displacement: {disp:.2f}")

    diff = disp - distance

    print(f"Diff: {diff:.2f}")

    loss += np.abs(diff)

    total += distance

loss = loss / len(df)

total = total / len(df)


print(f"Loss: {loss:.2f} per row, and the loss rate is {loss / total:.2f}")
