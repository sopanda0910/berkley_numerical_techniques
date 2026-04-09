import numpy as np

A = np.array([
    [4, 3, -5],
    [-2, -4, 5],
    [8, 8, 0]
])

A_inv = np.linalg.inv(A)

y = np.array([2, -5, 3])

x = np.linalg.solve(A, y)
x_a = np.dot(A_inv, y)
print(x)
print(x_a)

from scipy.linalg import lu

p, l, u = lu(A)
print(p)
print(l)
print(u)

print(np.dot(p, A))