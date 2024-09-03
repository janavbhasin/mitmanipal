import cv2
import numpy as np

def log_transform(img):
    """Apply log transformation to the image."""
    img_float = img.astype(np.float32)
    img_normalized = img_float / 255.0
    c = 255 / np.log(1 + np.max(img_normalized))
    log_transformed = c * np.log(1 + img_normalized)
    img_log = np.array(log_transformed, dtype=np.uint8)
    return img_log

def gamma_transform(img, gamma):
    """Apply gamma (power-law) transformation to the image."""
    img_float = img.astype(np.float32)
    img_normalized = img_float / 255.0
    c = 255 / np.power(np.max(img_normalized), gamma)
    gamma_transformed = c * np.power(img_normalized, gamma)
    img_gamma = np.array(gamma_transformed, dtype=np.uint8)
    return img_gamma

# Load the image in grayscale
img = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg', cv2.IMREAD_GRAYSCALE)

# Apply log transformation
log_img = log_transform(img)

# Apply gamma transformations for various gamma values
gamma_values = [0.1, 0.5, 1.2, 2.2]
gamma_images = [gamma_transform(img, gamma) for gamma in gamma_values]

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Log Transformed Image', log_img)
for i, gamma in enumerate(gamma_values):
    cv2.imshow(f'Gamma Transformed Image (Gamma={gamma})', gamma_images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
