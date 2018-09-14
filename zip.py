a = ['a', 'b', 'c']
b = ['x', 'y', 'z']

for i, (m, n) in enumerate(zip(a, b)):
    print(i, m, n)