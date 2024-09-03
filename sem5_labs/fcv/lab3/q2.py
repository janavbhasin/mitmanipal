import cv2
import numpy as np
from matplotlib import pyplot as plt
def sobel_filters():
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    sobel_y = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])
    return sobel_x, sobel_y
def compute_gradient(image: np.ndarray) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    sobel_x, sobel_y = sobel_filters()
    grad_x = cv2.filter2D(image, -1, sobel_x)
    grad_y = cv2.filter2D(image, -1, sobel_y)
    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    direction = np.arctan2(grad_y, grad_x) * (180 / np.pi)
    return grad_x, grad_y, magnitude, direction
def display_gradients(image: np.ndarray, grad_x: np.ndarray, grad_y: np.ndarray, magnitude: np.ndarray,
                      direction: np.ndarray):
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 2)
    plt.title('Gradient X')
    plt.imshow(grad_x, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 3)
    plt.title('Gradient Y')
    plt.imshow(grad_y, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 4)
    plt.title('Gradient Magnitude')
    plt.imshow(magnitude, cmap='gray')
    plt.axis('off')
    plt.subplot(2, 3, 5)
    plt.title('Gradient Direction')
    plt.imshow(direction, cmap='hsv')
    plt.axis('off')
    plt.show()
def main():
    image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Image not found.")
        return
    grad_x, grad_y, magnitude, direction = compute_gradient(image)
    display_gradients(image, grad_x, grad_y, magnitude, direction)
if __name__ == "__main__":
    main()