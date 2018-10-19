import os
import numpy as np
from tqdm import tqdm
from PIL import Image

image_files = os.listdir('raw/images')
mask_files = os.listdir('raw/masks')
names = [f[:-8] for f in image_files]
print(image_files)
print(mask_files)
print(names)

image_suffix = '-org'
mask_suffix = '-gt'

# mask = Image.open('raw/masks/Frame00001-gt.pbm').convert('L')
# print(np.array(mask)[256,256])
# mask.save('sample.png')


for name in tqdm(names):
    # Image files: resize and copy
    img = Image.open('raw/images/%s%s.jpg' % (name, image_suffix))

    width, height = img.size
    shorter = min(width, height)

    img = img.crop(((width - shorter) / 2,
                    (height - shorter) / 2,
                    (width + shorter) / 2,
                    (height + shorter) / 2))
    img = img.resize((224, 224))
    img.save('Figaro1k-png/images/%s.png' % name)


    # Mask files: change pixel colors, convert to grayscale image, resize, and copy
    msk = Image.open('raw/masks/%s%s.pbm' % (name, mask_suffix)).convert('L')

    msk = msk.crop(((width - shorter) / 2,
                    (height - shorter) / 2,
                    (width + shorter) / 2,
                    (height + shorter) / 2))
    msk = msk.resize((224, 224))
    msk.save('Figaro1k-png/masks/%s.png' % name)
