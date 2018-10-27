x_old = 0
x_new = 6
step_size = 0.01
precision = 0.00001

def objective(x):
    return x**4 - 3 * x**3 + 2

def f_prime(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - step_size * f_prime(x_old)
    print('x_old:', x_old, 'x_new', x_new, 'objective function:', objective(x_new))

print("local minimum occurs at ", x_new)