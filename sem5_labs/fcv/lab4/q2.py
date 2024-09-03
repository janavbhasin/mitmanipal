import cv2
import numpy as np

def detect_lines_hough(image_path):
    # Load the image
    image = cv2.imread('img.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection manually
    edges = cv2.Canny(gray, 50, 150)

    # Define parameters for Hough Line Transform
    height, width = edges.shape
    diagonal_len = int(np.sqrt(height**2 + width**2))
    accumulator = np.zeros((2 * diagonal_len, 180), dtype=np.uint16)

    # Hough Transform parameters
    threshold = 200

    # Perform Hough Transform manually
    for y in range(height):
        for x in range(width):
            if edges[y, x] > 0:  # Edge pixel
                for angle in range(180):
                    theta = np.deg2rad(angle)
                    rho = int(x * np.cos(theta) + y * np.sin(theta)) + diagonal_len
                    accumulator[rho, angle] += 1

    # Find the peaks in the accumulator
    lines = np.argwhere(accumulator > threshold)

    # Draw lines on the image
    for rho, angle in lines:
        theta = np.deg2rad(angle)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * (rho - diagonal_len)
        y0 = b * (rho - diagonal_len)
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Save and display the result
    cv2.imwrite('lines_detected.png', image)
    cv2.imshow('Lines Detected', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_lines_hough('input_image.png')