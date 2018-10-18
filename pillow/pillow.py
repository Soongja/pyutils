from PIL import Image
import numpy as np

img = Image.open('content.jpg')

npimg = np.array(img)

print(npimg.shape)