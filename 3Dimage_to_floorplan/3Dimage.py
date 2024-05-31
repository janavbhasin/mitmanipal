import os
import numpy as np
import open3d as o3d
directory_path = "/Users/janavbhasin/Desktop/internship/Stanford3dDataset_v1.2_Aligned_Version/Area_1/office_2/Annotations"
def load_point_cloud(file_path):
    try:
        return np.loadtxt(file_path)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None
all_point_clouds = []
def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            point_cloud = load_point_cloud(file_path)
            if point_cloud is not None:
                all_point_clouds.append(point_cloud)
traverse_directory(directory_path)
combined_point_cloud = np.vstack(all_point_clouds)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(combined_point_cloud[:, :3])
o3d.visualization.draw_geometries([pcd])
