from PIL import Image
import torch.nn as nn
import torch
import numpy as np
from torchvision import transforms
from torch.autograd import Variable

img = Image.open('jisoo.jpg').convert('LA')
#img.save(‘greyscale.png’)
T=transforms.Compose([transforms.ToTensor()])
P=transforms.Compose([transforms.ToPILImage()])

ten=torch.unbind(T(img))
x=ten[0].unsqueeze(0).unsqueeze(0)

# horizontal gradient
a=np.array([[1, 0, -1],[2,0,-2],[1,0,-1]])
conv1=nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1, bias=False)
conv1.weight=nn.Parameter(torch.from_numpy(a).float().unsqueeze(0).unsqueeze(0))
G_x=conv1(Variable(x)).data.view(1,256,256) # Mx
P_x = P(G_x)
P_x.save('fake_grad_x.png')

# vertical gradient
b=np.array([[1, 2, 1],[0,0,0],[-1,-2,-1]])
conv2=nn.Conv2d(1, 1, kernel_size=3, stride=1, padding=1, bias=False)
conv2.weight=nn.Parameter(torch.from_numpy(b).float().unsqueeze(0).unsqueeze(0))
G_y=conv2(Variable(x)).data.view(1,256,256) # My
P_y = P(G_y)
P_y.save('fake_grad_y.png')

G=torch.sqrt(torch.pow(G_x,2)+ torch.pow(G_y,2)) # gradient magnitude
P = P(G)
P.save('fake_grad.png')