import cv2
import numpy as np
import matplotlib.pyplot as plt
def simple_thresholding(image, threshold):
    return np.where(image > threshold, 255, 0).astype(np.uint8)
def adaptive_thresholding(image, block_size, C):
    rows, cols = image.shape
    half_block = block_size // 2
    padded_image = np.pad(image, pad_width=half_block, mode='constant', constant_values=0)
    binary_image = np.zeros_like(image, dtype=np.uint8)
    for i in range(rows):
        for j in range(cols):
            block = padded_image[i:i + block_size, j:j + block_size]
            binary_image[i, j] = 255 if image[i, j] > np.mean(block) - C else 0
    return binary_image
def show_results(image, binary_simple_custom, binary_adaptive_custom, binary_simple_cv, binary_adaptive_cv):
    plt.figure(figsize=(12, 10))
    plt.subplot(2, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image'), plt.axis('off')
    plt.subplot(2, 3, 2), plt.imshow(binary_simple_custom, cmap='gray'), plt.title('Simple Thresholding (Custom)'), plt.axis('off')
    plt.subplot(2, 3, 3), plt.imshow(binary_adaptive_custom, cmap='gray'), plt.title('Adaptive Thresholding (Custom)'), plt.axis('off')
    plt.subplot(2, 3, 4), plt.imshow(binary_simple_cv, cmap='gray'), plt.title('Simple Thresholding (OpenCV)'), plt.axis('off')
    plt.subplot(2, 3, 5), plt.imshow(binary_adaptive_cv, cmap='gray'), plt.title('Adaptive Thresholding (OpenCV)'), plt.axis('off')
    plt.show()
def main(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    binary_simple_custom = simple_thresholding(image, 127)
    binary_adaptive_custom = adaptive_thresholding(image, 22, 2)
    _, binary_simple_cv = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    binary_adaptive_cv = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 23, 2)
    show_results(image, binary_simple_custom, binary_adaptive_custom, binary_simple_cv, binary_adaptive_cv)
image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'  # Replace with your image path
main(image_path)
