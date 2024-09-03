import cv2

image_path = '/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'

image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image '{image_path}'")
else:
    height, width = image.shape[:2]
    angle = 45
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
