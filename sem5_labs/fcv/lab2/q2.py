import cv2
import numpy as np
def compute_cdf(hist):
    cdf = hist.cumsum()
    cdf_normalized = cdf * (255 / cdf[-1])
    return cdf_normalized
src_img = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab1/messi-world-cup.jpg', cv2.IMREAD_GRAYSCALE)
ref_img = cv2.imread('/home/Student/Desktop/220962049_aiml_a1/venv/lab2/test.png', cv2.IMREAD_GRAYSCALE)
src_hist = cv2.calcHist([src_img], [0], None, [256], [0, 256]).flatten()
ref_hist = cv2.calcHist([ref_img], [0], None, [256], [0, 256]).flatten()
src_cdf = compute_cdf(src_hist)
ref_cdf = compute_cdf(ref_hist)
lookup_table = np.zeros(256, dtype=np.uint8)
src_idx, ref_idx = 0, 0
while src_idx < 256 and ref_idx < 256:
    if src_cdf[src_idx] <= ref_cdf[ref_idx]:
        lookup_table[src_idx] = ref_idx
        src_idx += 1
    else:
        ref_idx += 1
spec_img = cv2.LUT(src_img, lookup_table)
res = np.hstack((src_img, spec_img))
cv2.imshow('Histogram Specification', res)
cv2.waitKey(0)
cv2.destroyAllWindows()