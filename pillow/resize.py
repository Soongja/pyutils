from PIL import Image

img = Image.open('jisoo.jpg')
# 626 446
# img = img.crop((120, 0, 566, 446))
# img = img.resize((256, 256))
img = img.resize((256, 256))
img.save('jisoo.jpg')