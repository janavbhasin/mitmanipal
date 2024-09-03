import cv2
import numpy as np
def gaussian_kernel(size: int, sigma: float) -> np.ndarray:
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma ** 2)) * np.exp(
            -(((x - (size - 1) / 2) ** 2 + (y - (size - 1) / 2) ** 2) / (2 * sigma ** 2))
        ),
        (size, size)
    )
    return kernel / np.sum(kernel)
def unsharp_masking(image: np.ndarray, sigma: float = 1.0, strength: float = 1.5) -> np.ndarray:
    if len(image.shape) == 3:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image_gray = image
    kernel_size = int(6 * sigma + 1) | 1
    gaussian_kernel_ = gaussian_kernel(kernel_size, sigma)
    blurred = cv2.filter2D(image_gray, -1, gaussian_kernel_)
    sharpened = cv2.addWeighted(image_gray, 1 + strength, blurred, -strength, 0)
    return sharpened
def display_images(original: np.ndarray, sharpened: np.ndarray):
    cv2.imshow('Original', original)
    cv2.imshow('Sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return
    sharpened_image = unsharp_masking(image)
    display_images(image, sharpened_image)
if __name__== "__main__":
    main()