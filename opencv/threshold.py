import cv2
import os

dir = './evaluation/mask/'
files = os.listdir(dir)
save_dir = './evaluation/mask_binary/'
os.makedirs(save_dir, exist_ok=True)

for file in files:
    img = cv2.imread(dir + file)
    ret, thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
    cv2.imwrite(save_dir + 'bin_' + file, thresh)