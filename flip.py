import cv2
import os

a = os.listdir('Satus_GeoConGAN_1000_0807/Real/ir/')
print(a[0])

hey = cv2.imread(str(a[0]), cv2.IMREAD_COLOR)


cv2.imshow('hey', hey)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(1000):
    img = cv2.imread(a[i])
    img = cv2.flip(img, 1)
    name = a[i]
    cv2.imwrite('flips/%s.png' % name, img)
