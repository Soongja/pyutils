import torch

a = torch.rand((16, 1024, 14, 24))
b = torch.rand((16, 1024, 14, 24))

c = torch.cat([a, b], dim=1)

print(c.shape)