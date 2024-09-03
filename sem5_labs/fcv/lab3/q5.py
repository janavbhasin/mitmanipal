from collections import deque
import cv2
import numpy as np
def compute_gradients(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.hypot(grad_x, grad_y)
    direction = np.arctan2(grad_y, grad_x) * (180.0 / np.pi) % 180
    magnitude = np.uint8(255 * magnitude / np.max(magnitude))  # Normalize to [0, 255]
    return magnitude, direction
def non_max_suppression(magnitude, direction):
    rows, cols = magnitude.shape
    output = np.zeros((rows, cols), dtype=np.float32)
    direction = direction / 180.0 * np.pi
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = direction[i, j]
            q, r = 0, 0
            if (0 <= angle < np.pi / 8) or (7 * np.pi / 8 <= angle <= np.pi):
                q, r = magnitude[i, j + 1], magnitude[i, j - 1]
            elif (np.pi / 8 <= angle < 3 * np.pi / 8):
                q, r = magnitude[i + 1, j - 1], magnitude[i - 1, j + 1]
            elif (3 * np.pi / 8 <= angle < 5 * np.pi / 8):
                q, r = magnitude[i + 1, j], magnitude[i - 1, j]
            elif (5 * np.pi / 8 <= angle < 7 * np.pi / 8):
                q, r = magnitude[i - 1, j - 1], magnitude[i + 1, j + 1]
            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                output[i, j] = magnitude[i, j]
    return output
def link_edges(image, labels, weak_edges, x, y):
    rows, cols = image.shape
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        if labels[cx, cy] == 255:
            continue
        if weak_edges[cx, cy]:
            labels[cx, cy] = 255
            for dx in [-1, 0, 1, 2]:
                for dy in [-1, 0, 1, 2]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if labels[nx, ny] != 255 and weak_edges[nx, ny]:
                            queue.append((nx, ny))
    return labels
def hysteresis_thresholding(image, low_threshold, high_threshold):
    strong_edges = (image >= high_threshold)
    weak_edges = (image >= low_threshold) & (image < high_threshold)
    labels = np.zeros_like(image, dtype=np.uint8)
    labels[strong_edges] = 255
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            if labels[i, j] == 255:
                continue
            if weak_edges[i, j]:
                labels = link_edges(image, labels, weak_edges, i, j)
    return labels
def canny_edge_detection_custom(image_path, highThresholdRatio=0.28, lowThresholdRatio=0.5):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(image, (7, 7), 1.4)
    magnitude, direction = compute_gradients(blurred_image)
    highThreshold = np.max(magnitude) * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    non_max_suppressed = non_max_suppression(magnitude, direction)
    edges = hysteresis_thresholding(non_max_suppressed, lowThreshold, highThreshold)
    return edges
def canny_edge_detection_builtin(image_path, low_threshold=50, high_threshold=150):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image = cv2.GaussianBlur(image, (7, 7), 1.4)
    edges = cv2.Canny(blurred_image, low_threshold, high_threshold)
    return edges
def show_results(edges_custom, edges_builtin):
    cv2.imshow('Canny Edges (Custom)', edges_custom)
    cv2.imshow('Canny Edges (OpenCV Built-in)', edges_builtin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main(image_path):
    edges_custom = canny_edge_detection_custom(image_path)
    edges_builtin = canny_edge_detection_builtin(image_path)
    show_results(edges_custom, edges_builtin)
image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'  # Replace with your image path
main(image_path)
