import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.1, 0.3, 0.4, 0.9])
y = np.array([-7.5, -9.25, -8.0, -5.25])

n=len(x)
h=np.diff(x)
A=np.zeros((n,n))
b=np.zeros(n)

A[0, 0] = 1
A[n-1, n-1] = 1

for i in range (1, n-1):
    A[i, i - 1] = h[i - 1]
    A[i, i] = 2 * (h[i - 1] + h[i])
    A[i, i + 1] = h[i]

for i in range(1, n-1):
   b[i] = 3 * ((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])

c = np.linalg.solve(A, b)

d = np.zeros(n-1)
b = np.zeros(n-1)

for i in range(n-1):
    d[i] = (c[i+1] - c[i]) / (3 * h[i])
    b[i] = (y[i+1] - y[i]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3

def cubic_spline(xi, i):
    return y[i] + b[i] * (xi - x[i]) + c[i] * (xi - x[i])**2 + d[i] * (xi - x[i])**3

xi = np.linspace(min(x), max(x), 100)
yi = np.zeros_like(xi)

for i in range(len(xi)):
    for j in range(n-1):
        if xi[i] <= x[j+1]:
            yi[i] = cubic_spline(xi[i], j)
            break


plt.plot(x, y, 'ro', label='Starting points')
plt.plot(xi, yi, label='Cubic spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
