import torch
import torchvision.transforms as transforms
import torchvision.utils as vutils
from PIL import Image

img = Image.open('bin86.png').convert('RGB')

img2 = Image.open('0000.png')

transform = transforms.Compose([
                transforms.Grayscale(),
                transforms.ToTensor(),
                ])

img = transform(img)
img2 = transform(img2)

long = img.long()
long2 = img2.long()
print(img)
print(long)
print(img.shape, long.shape)

vutils.save_image(img, 'float.png', nrow=1)
vutils.save_image(long, 'long.png', nrow=1)
vutils.save_image(long2, 'long2.png', nrow=1)
