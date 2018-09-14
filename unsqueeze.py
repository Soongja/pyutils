import numpy as np

a = np.array([[20], [20]])
b = np.array([30, 30])
c = np.array([40, 40])

x = np.expand_dims(a, axis = 0)

d = np.concatenate((x, x, x), axis=0)
print(d)
# print(d)
# print(d.shape)