import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_sift_descriptors(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    sift = cv2.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(img, None)
    return keypoints, descriptors

def compute_distances_manual(desc1, desc2):
    # Initialize distance matrix
    distances = np.zeros((desc1.shape[0], desc2.shape[0]))

    # Compute Euclidean distance manually
    for i in range(desc1.shape[0]):
        for j in range(desc2.shape[0]):
            diff = desc1[i] - desc2[j]
            distances[i, j] = np.sqrt(np.sum(diff ** 2))

    return distances

def find_nearest_neighbors(distances):
    # Find the index of the minimum distance for each descriptor in desc1
    nearest_indices = np.argmin(distances, axis=1)
    return nearest_indices

def draw_matches(img1, keypoints1, img2, keypoints2, indices):
    matches = []
    for i, idx in enumerate(indices):
        if idx < len(keypoints2):
            matches.append(cv2.DMatch(i, idx, 0))
    img_matches = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    return img_matches

def main(img1_path, img2_path):
    # Extract descriptors
    kp1, desc1 = extract_sift_descriptors(img1_path)
    kp2, desc2 = extract_sift_descriptors(img2_path)

    # Compute distances manually
    distances = compute_distances_manual(desc1, desc2)

    # Find nearest neighbors
    indices = find_nearest_neighbors(distances)

    # Load images for visualization
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # Draw matches
    img_matches = draw_matches(img1, kp1, img2, kp2, indices)

    # Display matches
    plt.figure(figsize=(12, 6))
    plt.imshow(cv2.cvtColor(img_matches, cv2.COLOR_BGR2RGB))
    plt.title('SIFT Matches')
    plt.axis('off')
    plt.show()

# Example usage
img1_path = '/home/Student/Desktop/220962049_aiml_a1/venv/img_1.png'
img2_path = '/home/Student/Desktop/220962049_aiml_a1/venv/img_4.png'
main(img1_path, img2_path)
