import numpy as np
import cv2
image=cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg',cv2.IMREAD_COLOR)
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image1=image
hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * 255 / cdf[-1]
equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
equalized_image = equalized_image.reshape(image.shape)
image=np.uint8(equalized_image)
cv2.imshow('histogram equalize image',image)
cv2.imshow('grayscale image',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()