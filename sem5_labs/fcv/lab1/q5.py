import cv2
import numpy as np

image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image '{image_path}'")
else:
    pts = np.array([[150, 50], [300, 200], [50, 200]], np.int32)
    pts = pts.reshape((-1, 1, 2))

    color = (255, 0, 0)
    thickness = 2

    image_with_triangle = cv2.polylines(image, [pts], isClosed=True, color=color, thickness=thickness)

    cv2.imshow('Image with Triangle', image_with_triangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
