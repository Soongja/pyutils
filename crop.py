from PIL import Image

img = Image.open('86.png').convert('RGB')
img = img.crop((0, 100, 320, 320))
#img = img.resize((256, 256))
img.save('86.jpg')