'''in the plotted image we have not been mentioned any scale therefore we have 
plotted the image on a graph for relative scale'''
import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

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

bottom_threshold = np.percentile(combined_point_cloud[:, 2], 10)
top_threshold = np.percentile(combined_point_cloud[:, 2], 75)
left_threshold = np.percentile(combined_point_cloud[:, 0], 10)
right_threshold = np.percentile(combined_point_cloud[:, 0], 95)
front_threshold = np.percentile(combined_point_cloud[:, 1], 20)
back_threshold = np.percentile(combined_point_cloud[:, 1], 80)

filtered_points = combined_point_cloud[
    (combined_point_cloud[:, 2] > bottom_threshold) & 
    (combined_point_cloud[:, 2] < top_threshold) & 
    (combined_point_cloud[:, 0] > left_threshold) & 
    (combined_point_cloud[:, 0] < right_threshold) &
    (combined_point_cloud[:, 1] > front_threshold) & 
    (combined_point_cloud[:, 1] < back_threshold)
]

filtered_pcd = o3d.geometry.PointCloud()
filtered_pcd.points = o3d.utility.Vector3dVector(filtered_points[:, :3])

eps = 0.1
min_points = 10
labels = np.array(filtered_pcd.cluster_dbscan(eps=eps, min_points=min_points))

colors = plt.cm.tab10(np.linspace(0, 1, np.max(labels) + 1))
colors[0] = [0, 0, 0, 1]
colored_points = colors[labels]
filtered_pcd.colors = o3d.utility.Vector3dVector(colored_points[:, :3])

proj_points = filtered_points[:, :2]

fig, ax = plt.subplots()
scatter = ax.scatter(proj_points[:, 0], proj_points[:, 1], c=labels, cmap='tab10')

handles, labels = scatter.legend_elements()
unique_labels = np.unique(labels)
for label in unique_labels:
    indices = np.where(labels == label)[0]
    if len(indices) > 0:
        cluster_points = filtered_points[indices]
        min_bound = np.min(cluster_points, axis=0)
        max_bound = np.max(cluster_points, axis=0)
        length = max_bound[0] - min_bound[0]
        width = max_bound[1] - min_bound[1]
        ax.text(min_bound[0], min_bound[1], f"Length: {length:.2f}\nWidth: {width:.2f}", ha='center', va='center')

ax.legend(handles, unique_labels, title='Cluster', loc='upper right')
plt.show()
