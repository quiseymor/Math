x = [1.4, 1.6, 1.8, 2.0]
y = [-4.424, -5.192, -5.800, -6.200]

def divided_differences(x, y):
    n = len(y)
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    return f

divided_diff = divided_differences(x, y)

def newton_interpolation(x, divided_diff, x_val):
    n = len(x)
    p = divided_diff[0][0]  
    for i in range(1, n):
        term = divided_diff[0][i]  
        for j in range(i):
            term *= (x_val - x[j])
        p += term  
    return p

x_val = 1.2

poly_val = round(newton_interpolation(x, divided_diff, x_val),4)  

print(f"The interpolated value at x  = {x_val} is approximately {poly_val}")

# Constant pitch check
step = x[1] - x[0]  
constant_step = True
for i in range(1, len(x) - 1):
    if x[i + 1] - x[i] != step:
        constant_step = False
        break

if constant_step:
    print("The step between x values is constant.")
else:
    print("The step between x values is not constant.")
