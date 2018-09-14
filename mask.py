import cv2
import numpy as np

img = cv2.imread('style.jpg')
rows, cols, channels = img.shape

# masking foreground
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 90, 255, cv2.THRESH_BINARY)
fg_mask = cv2.bitwise_and(img, img, mask=mask)
# cv2.imshow('fg_mask', fg_mask)

# masking background
bg = np.full(img.shape, 255, dtype=np.uint8) # white background
mask_inv = cv2.bitwise_not(mask)
bg_mask = cv2.bitwise_and(bg, bg, mask=mask_inv)

out = cv2.bitwise_or(fg_mask, bg_mask)
# out = cv2.add(fg_mask, bg_mask)


cv2.imshow('out', out)
cv2.imwrite('style_masked.jpg', out)

cv2.waitKey(0)
cv2.destroyAllWindows()