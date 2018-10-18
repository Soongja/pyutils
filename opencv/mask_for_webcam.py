import cv2
import numpy as np

img = cv2.imread('86.png')
mask = cv2.imread('bin86.png')
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
print(mask)

# a = cv2.resize(mask, (240, 240))

ret, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)
np.savetxt('test.out', mask, delimiter=',')


# 손만 둥둥 떠다니는 놈
fg_mask = cv2.bitwise_and(img, img, mask=mask)

# cv2.imshow('fg_mask', fg_mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 손 빨갛게 칠하는 놈
mask_inv = cv2.bitwise_not((mask))
print(mask_inv)
bg_mask = cv2.bitwise_and(img, img, mask=mask_inv)
bg_mask[np.where((bg_mask == [0,0,0]).all(axis=2))] = [0,0,255]

# print(img.shape)
# print(mask_inv.shape)

cv2.imshow('bg_mask', bg_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()



# masking background
# bg = np.full(img.shape, 255, dtype=np.uint8) # white background
# mask_inv = cv2.bitwise_not(mask)
# bg_mask = cv2.bitwise_and(bg, bg, mask=mask_inv)
#
# out = cv2.bitwise_or(fg_mask, bg_mask)
# out = cv2.add(fg_mask, bg_mask)
#
#
# cv2.imshow('out', out)
# cv2.imwrite('style_masked.jpg', out)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()