import cv2
import numpy as np

def manual_color_segmentation(image_path, lower_bound, upper_bound, output_path):
    # Load the image
    image = cv2.imread('Untitled.jpg')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Convert bounds to numpy arrays
    lower_bound = np.array(lower_bound, dtype=np.uint8)
    upper_bound = np.array(upper_bound, dtype=np.uint8)

    # Create the binary mask manually
    height, width, _ = hsv.shape
    mask = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            pixel = hsv[y, x]
            if (lower_bound <= pixel).all() and (pixel <= upper_bound).all():
                mask[y, x] = 255

    # Apply the mask manually
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    # Save and display the result
    cv2.imwrite(output_path, segmented_image)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage: segment for red color
manual_color_segmentation('input_image.png', [0, 50, 50], [10, 255, 255], 'segmented_image.png')