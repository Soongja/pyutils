from PIL import Image
import numpy as np

img = Image.open('0000.jpg')
img_np = np.array(img)
print(img_np)
print(img_np.shape)