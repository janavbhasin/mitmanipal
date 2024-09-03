import cv2 as cv
image_path='/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg'
image = cv.imread(image_path)

if image is None:
    print(f"Error: Unable to load image '{image_path}'")
else:
    x1, y1 = 100, 100
    x2, y2 = 300, 400
    color = (0, 255, 0)
    thickness = 2

    image_with_rectangle = cv.rectangle(image, (x1, y1), (x2, y2), color, thickness)

    cv.imshow('Image with Rectangle', image_with_rectangle)
    cv.waitKey(0)
    cv.destroyAllWindows()
