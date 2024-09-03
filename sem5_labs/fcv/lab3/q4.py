import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def sobel_kernel_x():
    """Generate Sobel kernel for x direction."""
    return np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])


def sobel_kernel_y():
    """Generate Sobel kernel for y direction."""
    return np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])


def apply_kernel(image_array, kernel):
    """Apply convolution with a given kernel."""
    kernel_size = kernel.shape[0]
    pad = kernel_size // 2
    img_padded = np.pad(image_array, pad, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image_array)

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            filtered_image[i, j] = np.sum(
                kernel * img_padded[i:i + kernel_size, j:j + kernel_size]
            )

    return filtered_image


def compute_edges(input_path, output_path):
    """Compute edges using Sobel operator and save the result."""
    # Load image and convert to grayscale
    image = Image.open(input_path).convert('L')
    image_array = np.array(image)

    # Generate Sobel kernels
    kernel_x = sobel_kernel_x()
    kernel_y = sobel_kernel_y()

    # Apply Sobel kernels to the image
    gradient_x = apply_kernel(image_array, kernel_x)
    gradient_y = apply_kernel(image_array, kernel_y)

    # Compute gradient magnitude (edge detection)
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

    # Normalize gradient magnitude to [0, 255]
    gradient_magnitude = np.clip(gradient_magnitude / np.max(gradient_magnitude) * 255, 0, 255).astype(np.uint8)

    # Save result
    Image.fromarray(gradient_magnitude).save(output_path)
    print(f"Edges detected and saved as {output_path}")

    # Display result
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Edge Detection (Sobel Operator)')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # Specify file paths
    input_path = 'image.jpeg'
    output_path = 'edges_detected.jpg'

    compute_edges(input_path, output_path)