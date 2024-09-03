import cv2
img = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg')
new_size = (100, 100)
resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
start_x, start_y = 50, 50
width, height = 100, 100
cropped_img = img[start_y:start_y + height, start_x:start_x + width]
cv2.imshow('Resized Image', resized_img)
cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()