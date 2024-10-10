import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/left(1).jpg')
img2 = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/right(1).jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
matches = bf.knnMatch(descriptors1, descriptors2, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 2)
if len(src_pts) >= 4 and len(dst_pts) >= 4:
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
    height, width, channels = img2.shape
    img1_warped = cv2.warpPerspective(img1, H, (width, height))
    stitched_image = np.maximum(img1_warped, img2)
    plt.imshow(cv2.cvtColor(stitched_image, cv2.COLOR_BGR2RGB))
    plt.title('Stitched Image')
    plt.axis('off')
    plt.show()
