# Implicit Formula: S(t_j+1) = S(t_j) + h*F(t_j+1, S(t_j+1))
# Sometimes possible to solve for S(t_j+1) like this

# For higher order DE, simplify into a system of 1st order DE

# Trapezoid Formula
# S(t_j+1) = S(t_j) + h/2 (F(t_j, S(t_j)), F(t_j+1, S(t_j+1)))
# Typically, if F is linear, it is possibl to solve for S(t_j)
# Linearized Oscillator (2nd order --> 2 1st order)

# S = (theta(t), w(t))
# dS/dt = ((0, 1), (-g/l, 0))*S(t)
# A = ((0, 1), (-g/l, 0))

# (I-h/2*A)S(t_j+1) = (I+h/2*A)S(t_j)

import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt

g = 10
l = 1

A = np.array([[0, 1], [-g/l, 0]])
S_0 = np.array([0.5, 0.5])

h = 0.0005
t = np.arange(0, 5, h)

S = np.zeros((len(t), 2))
S[0] = S_0

for i in range(1, len(t)):
    I = np.eye(len(A))
    S[i] = np.dot(np.dot(linalg.inv(I - (h/2)*A), (I + (h/2)*A)), S[i-1])

theta_vals = S[:, 0]
# print(theta_vals)

plt.figure(figsize=(14, 8))
plt.plot(t, theta_vals)
plt.grid(True)
plt.show()