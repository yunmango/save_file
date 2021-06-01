import numpy as np

lidar_file = 'test/raw_67015.bin'
load_points = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)
print(load_points)
print(load_points.shape)
print(load_points[0])

import pcl
import glob
lidar_dir = './test/*.bin'
file_list = glob.glob(lidar_dir)
print(file_list)
for i, lidar_file in enumerate(file_list):
    load_points = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)
    pc_intensity = pcl.PointCloud_PointXYZI()
    pc_intensity.from_array(load_points)
    pcd_file = 'test%d.pcd'%(i)
    pcl.save(pc_intensity, pcd_file)
    

