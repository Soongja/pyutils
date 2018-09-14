import torch

a = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[6, 6, 6], [7, 7, 7]]])
b = torch.tensor([[1, 0, 1], [0, 0, 1], [1, 0, 0]])
# c = a[b]

# bb = b.view(3, 3, 1).repeat(1, 1, 2)
# print(bb)

# print(a[bb])

c = torch.tensor([[0.01, 0.7, 0.3, 1.1]])

d = torch.clamp(c, min=0, max=1)
print(d)