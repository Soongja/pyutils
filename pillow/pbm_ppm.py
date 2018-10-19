import numpy as np
from PIL import Image

img = Image.open('Frame00010-gt.pbm')

# img = img.resize((224, 224))
# img = img.convert('L')
img.save('fuck.png')

# np_img = np.array(img)
# print(np_img[60][120])