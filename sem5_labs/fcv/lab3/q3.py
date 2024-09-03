import cv2
import numpy as np
from matplotlib import pyplot as plt

def apply_box_filter(image: np.ndarray, ksize: int) -> np.ndarray:
    """Apply a box filter (average filter) to the image."""
    return cv2.blur(image, (ksize, ksize))

def apply_gaussian_blur(image: np.ndarray, ksize: int, sigma: float) -> np.ndarray:
    """Apply Gaussian blur to the image."""
    return cv2.GaussianBlur(image, (ksize, ksize), sigma)

def main():
    # Load the image from file
    image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Error: Image not found.")
        return

    # Apply filters
    box_filtered_image = apply_box_filter(image, ksize=5)
    gaussian_blurred_image = apply_gaussian_blur(image, ksize=5, sigma=1.0)

    # Display results
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Box Filtered Image')
    plt.imshow(box_filtered_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Gaussian Blurred Image')
    plt.imshow(gaussian_blurred_image, cmap='gray')
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
