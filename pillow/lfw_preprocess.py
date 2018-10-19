import os
from PIL import Image
from tqdm import tqdm

image_files = os.listdir('raw/images')
mask_files = os.listdir('raw/masks')
mask_names = [f[:-4] for f in mask_files]
print(image_files)
print(mask_files)
print(mask_names)

os.makedirs('lfw-png', exist_ok=True)
os.makedirs('lfw-png/images', exist_ok=True)
os.makedirs('lfw-png/masks', exist_ok=True)

for name in tqdm(mask_names):
    # Image files: resize and copy
    img = Image.open('raw/images/%s.jpg' % name)
    img = img.resize((224, 224))
    img.save('lfw-png/images/%s.png' % name)

    # Mask files: change pixel colors, convert to grayscale image, resize, and copy
    msk = Image.open('raw/masks/%s.ppm' % name)
    pixels = msk.load()

    for i in range(msk.size[0]):
        for j in range(msk.size[1]):
            if pixels[i, j] == (255, 0, 0):
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)

    msk = msk.resize((224, 224)).convert('L')
    msk.save('lfw-png/masks/%s.png' % name)


'''
# check alpha blended

mask = cv2.imread('mask.png')
img1 = cv2.imread('lfw.jpg')
img2 = cv2.imread('data.jpg')

blend1 = (0.5 * mask + 0.5 * img1).astype(np.uint8)
blend2 = (0.5 * mask + 0.5 * img2).astype(np.uint8)

cv2.imshow('lfw', blend1)
cv2.imshow('data', blend2)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''