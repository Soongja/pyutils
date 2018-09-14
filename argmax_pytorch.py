import torch
import torch.nn as nn
import torch.nn.functional as F
# a = torch.rand(2, 3, 3)
# print(a)
# b = torch.argmax(a, 0)
# print(b)
# print(b.shape)


# c = torch.rand(4, 2, 3, 3)
# print(c)
# model = nn.Softmax(dim=1)
# d = model(c)
# e = F.softmax(c, dim=1)
# print(d.shape)
# print(e.shape)

g = torch.tensor([[1, 2, 3, 5], [100 ,200, 500, 900]], dtype=torch.float64)
model = nn.Sigmoid()
gg = model(g)
print(g)
print(gg)