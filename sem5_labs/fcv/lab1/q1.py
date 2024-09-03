import cv2 as cv
img=cv.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg',cv.IMREAD_COLOR)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()