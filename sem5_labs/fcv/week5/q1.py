import cv2 as cv
import numpy as np
img=cv.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(7,7),0.5)
s_x = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]], dtype=np.float32)
s_y = np.array([[-1, -2, -1],
                [ 0,  0,  0],
                [ 1,  2,  1]], dtype=np.float32)
ix = cv.filter2D(blur, -1, s_x)
iy = cv.filter2D(blur, -1, s_y)
ix2=ix*ix
iy2=iy*iy
ixiy=ix*iy
sigma = 1.0
ix2 = cv.GaussianBlur(ix2, (3, 3), sigma)
iy2 = cv.GaussianBlur(iy2, (3, 3), sigma)
ixiy = cv.GaussianBlur(ixiy, (3, 3), sigma)
det = (ix2 * iy2) - (ixiy * ixiy)
trace = ix2 + iy2
R = det - 0.04 * (trace * trace)
R_normalized = cv.normalize(R, None, 0, 255, cv.NORM_MINMAX)
R_normalized = np.uint8(R_normalized)
cv.imshow('Harris Response', R_normalized)
cv.waitKey(0)
cv.destroyAllWindows()
