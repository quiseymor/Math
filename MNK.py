import numpy as np

# for linear function
x_linear = np.array([3.02, 3.44, 3.6, 4.68, 4.94, 4.97, 5.29, 5.34,5.48, 5.59, 5.72, 5.85, 6.2, 7.24, 7.64, 7.77])
y_linear = np.array([19.6, 22.7, 19.9, 22.1, 20.7, 20.8, 19.9, 18.3,19.1, 18, 18.2, 17.4, 15.4, 9, 7, 4.5])

# for a quadratic function
x_quadratic = np.array([3.02, 3.44, 3.6, 4.68, 4.94, 4.97, 5.29, 5.34,5.48, 5.59, 5.72, 5.85, 6.2, 7.24, 7.64, 7.77])
y_quadratic = np.array([19.6, 22.7, 19.9, 22.1, 20.7, 20.8, 19.9, 18.3,19.1, 18, 18.2, 17.4, 15.4, 9, 7, 4.5])

# for the proposed function (1/x +b)
x_custom = np.array([3.02, 3.44, 3.6, 4.68, 4.94, 4.97, 5.29, 5.34,5.48, 5.59, 5.72, 5.85, 6.2, 7.24, 7.64, 7.77])
y_custom = np.array([19.6, 22.7, 19.9, 22.1, 20.7, 20.8, 19.9, 18.3,19.1, 18, 18.2, 17.4, 15.4, 9, 7, 4.5])

# odds MNK
def linear_least_squares(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    return np.linalg.lstsq(A, y, rcond=None)[0]

def quadratic_least_squares(x, y):
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    return np.linalg.lstsq(A, y, rcond=None)[0]

def custom_least_squares(x, y):
    A = np.vstack([1/x, np.ones(len(x))]).T
    return np.linalg.lstsq(A, y, rcond=None)[0]

# Odds calculation
a_linear, b_linear = linear_least_squares(x_linear, y_linear)
a_quadratic, b_quadratic, c_quadratic = quadratic_least_squares(x_quadratic, y_quadratic)
a_custom, b_custom = custom_least_squares(x_custom, y_custom)

# Calculation of the coefficient of determination value
def r_squared(x, y, a, b, c=None):
    y_pred = a * x + b if c is None else a * x**2 + b * x + c
    y_mean = np.mean(y)
    ss_total = np.sum((y - y_mean)**2)
    ss_residual = np.sum((y - y_pred)**2)
    return 1 - (ss_residual / ss_total)

r_squared_linear = r_squared(x_linear, y_linear, a_linear, b_linear)
r_squared_quadratic = r_squared(x_quadratic, y_quadratic, a_quadratic, b_quadratic, c_quadratic)
r_squared_custom = r_squared(x_custom, y_custom, a_custom, b_custom)

print("Linear function: y = {}x + {}".format(a_linear, b_linear))
print("Quadratic function: y = {}x^2 + {}x + {}".format(a_quadratic, b_quadratic, c_quadratic))
print("Proposed function: y = {} / x + {}".format(a_custom, b_custom))
print("Determination coefficient (linear):", r_squared_linear)
print("Determination coefficient (quadratic):", r_squared_quadratic)
print("Determination coefficient (proposed):", r_squared_custom)
