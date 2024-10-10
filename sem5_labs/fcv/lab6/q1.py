import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Function to compute SIFT descriptors
def compute_sift_descriptors(img, keypoints, size=16, bin_size=4, num_bins=8):
    descriptors = []
    for kp in keypoints:
        x, y = int(kp.pt[0]), int(kp.pt[1])
        size = int(kp.size)

        # Extract a patch around the keypoint
        patch = img[y-size:y+size, x-size:x+size]
        if patch.shape[0] != patch.shape[1] or patch.shape[0] != 2*size:
            continue

        # Compute gradients in x and y directions
        gx, gy = np.gradient(patch.astype(float))
        magnitude = np.sqrt(gx**2 + gy**2)
        orientation = np.arctan2(gy, gx) * 180 / np.pi

        # Divide patch into cells and compute histogram for each cell
        descriptor = np.zeros((bin_size, bin_size, num_bins))
        for i in range(bin_size):
            for j in range(bin_size):
                cell_mag = magnitude[i*size//bin_size:(i+1)*size//bin_size,
                                     j*size//bin_size:(j+1)*size//bin_size]
                cell_ori = orientation[i*size//bin_size:(i+1)*size//bin_size,
                                       j*size//bin_size:(j+1)*size//bin_size]
                hist, _ = np.histogram(cell_ori, bins=num_bins, range=(-180, 180), weights=cell_mag)
                descriptor[i, j, :] = hist

        # Flatten descriptor and normalize
        descriptor = descriptor.flatten()
        norm = np.linalg.norm(descriptor)
        if norm > 0:
            descriptor /= norm

        descriptors.append(descriptor)
 
    return np.array(descriptors)

# Function to draw keypoints on the image
def draw_keypoints(img, keypoints, color=(255, 0, 0)):
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, color=color, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return img_with_keypoints

# Function to compare and display SIFT descriptors
def compare_sift_descriptors(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    # Initialize OpenCV SIFT
    sift = cv2.SIFT_create()
    keypoints, opencv_descriptors = sift.detectAndCompute(img, None)

    # Compute custom SIFT descriptors
    custom_descriptors = compute_sift_descriptors(img, keypoints)

    # Draw keypoints on images
    img_with_opencv_keypoints = draw_keypoints(img_rgb, keypoints, color=(255, 0, 0))
    img_with_custom_keypoints = draw_keypoints(img_rgb, keypoints, color=(0, 255, 0))

    # Display images with keypoints
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("OpenCV Keypoints")
    plt.imshow(cv2.cvtColor(img_with_opencv_keypoints, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Custom Keypoints")
    plt.imshow(cv2.cvtColor(img_with_custom_keypoints, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

    # Compare descriptors
    if opencv_descriptors is not None and custom_descriptors.size > 0:
        # Compute Euclidean distances between descriptors
        distances = np.linalg.norm(opencv_descriptors[:, None] - custom_descriptors, axis=2)
        min_distances = np.min(distances, axis=1)
        avg_distance = np.mean(min_distances)
        print(f"Average Euclidean Distance between descriptors: {avg_distance:.2f}")
    else:
        print("Descriptors not computed correctly")

# Test the comparison
img_path = '/home/Student/Desktop/220962049_aiml_a1/venv/img_1.png'
compare_sift_descriptors(img_path)
