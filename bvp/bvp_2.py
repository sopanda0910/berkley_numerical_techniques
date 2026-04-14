# Finite Difference Method
'''
Split the interval into n parts
dy/dx = (y_i+1 - y_i-1)/2h
d^2y/dx^2 = (y_i-1 -2y_i + y_i+1)/h^2

This creates a (N+1) system of equations to solve

For d^2y/dt^2 = -g, the output looks like
[y_0,
-gh^2,
-gh^2,
...
y_final]
'''
import numpy as np
import matplotlib.pyplot as plt

# y(0) = 0 and y(5) = 35

g = 10
N = 50
h = (5-0)/N
A = np.zeros(((N+1), (N+1)))

A[0][0] = 1
A[N][N] = 1

for i in range(1, N):
    A[i, i-1] = 1
    A[i, i] = -2
    A[i, i+1] = 1

print(A)

b = np.zeros(((N+1), 1))
b[1:-1] = -g*h**2
b[-1] = 35

y = np.linalg.solve(A, b)
t = np.linspace(0, 5, N+1)

plt.figure(figsize=(10, 8))
plt.plot(t, y)
plt.plot(5, 35, 'ro')
plt.grid(True)
plt.show()