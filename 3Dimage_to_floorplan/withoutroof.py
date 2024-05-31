import os
import numpy as np
import open3d as o3d

def load_point_cloud(file_path):
    try:
        return np.loadtxt(file_path)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def traverse_directory(directory):
    all_point_clouds = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            point_cloud = load_point_cloud(file_path)
            if point_cloud is not None:
                all_point_clouds.append(point_cloud)
    return np.vstack(all_point_clouds)

directory_path = "/Users/janavbhasin/Desktop/internship/Stanford3dDataset_v1.2_Aligned_Version/Area_1/office_2/Annotations"
combined_point_cloud = traverse_directory(directory_path)


lower_half_points = combined_point_cloud[combined_point_cloud[:, 2] < np.mean(combined_point_cloud[:, 2])]

lower_half_pcd = o3d.geometry.PointCloud()
lower_half_pcd.points = o3d.utility.Vector3dVector(lower_half_points[:, :3])

o3d.visualization.draw_geometries([lower_half_pcd])
