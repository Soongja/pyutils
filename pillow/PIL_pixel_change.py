import numpy as np
from PIL import Image

img = Image.open('mask.png')
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] == (255, 0, 0):
            pixels[i, j] = (255, 255, 255)
        else:
            pixels[i, j] = (0, 0, 0)

img = img.resize((224, 224))
img = img.convert('L')
img.save('mask_converted.png')

np_img = np.array(img)
print(np_img)