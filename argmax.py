import numpy as np

# (2, 3, 3)
a = np.array(
    [
     [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]],

     [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]
     ]
)

argmax = np.argmax(a, axis=0)
print(argmax)