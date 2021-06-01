import numpy as np

# create lidar points x,y,z,intensity
points = np.random.randn(20000,4).astype(np.float32)
print(points)
print(points.shape)     # (20000, 4)

# Save lidar points
points.tofile('points.bin') 


# TEST
# load lidar binary file
lidar_file = 'points.bin'
load_points = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)
print(points)
print(points.shape)
