from PIL import Image

a = Image.open('didoo.jpg')
b = Image.open('jisoo.jpg')
a.paste(b, (0,0))

a.save('pasted.jpg')