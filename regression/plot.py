from df import df
import matplotlib.pyplot as plt
import polars as pl
import numpy as np

df = df.with_columns([
    (pl.col("angle") * (np.pi / 180)).alias("angle_radians")
])

df = df.with_columns([
    (pl.col("velocity") * np.cos(pl.col("angle_radians"))).alias("v_x"),
    (pl.col("velocity") * np.sin(pl.col("angle_radians"))).alias("v_y")
])

df = df.with_columns([
    (np.cos((np.abs(pl.col("fb_trunk_lean")) * (np.pi / 180))) * pl.col('velocity')).alias("fb_trunk_lean"),
    (np.cos((np.abs(pl.col("lr_trunk_lean")) * (np.pi / 180))) * pl.col('velocity')).alias("lr_trunk_lean")
])

df = df.with_columns([
    (pl.col("distance") / pl.col("lr_trunk_lean")).alias("distance")
])

plt.figure(figsize=(10, 6))
plt.scatter(df['release_height'], df['distance'], alpha=0.5)
plt.title('Release Height vs. Distance')
plt.xlabel('Release Height (meters)')
plt.ylabel('Distance (meters)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['v_x'], df['distance'], alpha=0.5)
plt.title('Velocity x vs. Distance')
plt.xlabel('Velocity x (meters)')
plt.ylabel('Distance (meters)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['v_y'], df['distance'], alpha=0.5)
plt.title('Velocity y vs. Distance')
plt.xlabel('Velocity y (meters)')
plt.ylabel('Distance (meters)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['velocity'], df['distance'], alpha=0.5, color='red')
plt.title('Velocity vs. Distance')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Distance (meters)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['angle'], df['distance'], alpha=0.5, color='green')
plt.title('Angle vs. Distance')
plt.xlabel('Angle (degrees)')
plt.ylabel('Distance (meters)')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['lr_trunk_lean'], df['distance'], alpha=0.5, color='purple')
plt.title('LR Trunk Lean vs. Distance')
plt.xlabel('LR Trunk Lean (degrees)')
plt.ylabel('Distance (meters)')
plt.show()
