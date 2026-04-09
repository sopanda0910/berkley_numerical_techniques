import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = 1 + x + x*np.random.random(len(x))

A = np.vstack([x, np.ones(len(x))]).T # Two columns for mx+b
# If there were more variables (x, y, z) --> np.vstack([x, y, z, np.ones(len(x))])
# Each column represents a different parameter

y = y.T

# Pseudo-Inverse Method
'''
Y = A*B (B is a column vector of all the parameters of optimization)
np.dot(Y - Y_real, Y) = 0 (Definition of minimizing error)
(A*B)^T * (A*B - Y_real) = 0
B^T * A^T * (A*B - Y_real) = 0
A^T * A * B = A^T * Y_real
B = (A^T * A)^-1 * A^T * Y_real
(A^T * A)^-1 * A^T is the pseudo-inverse, required to find the optimized parameters
'''

b = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), y)
print(b)

y_pred = b[0] * x + b[1]

# Scipy optimize
import scipy.optimize as opt

def linear(x, a, b):
    return a*x + b

alpha = optimize.curve_fit(linear, xdata=x, ydata=y)

plt.plot(x, y, 'kx')
plt.plot(x, y_pred)
plt.grid(True)
plt.show()

# A similar structure can be used for non-linear regression