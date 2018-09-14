import os
from PIL import Image

files = os.listdir('mask_binary')

for i in files:
    img = Image.open('mask_binary/' + i)
    img = img.crop((0, 70, 320, 250))
    img = img.resize((384, 216))
    img.save('mask/' + i)