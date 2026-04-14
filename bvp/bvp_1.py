# Temperature Distribution of a Fin
'''
T(0) = T_0
T(L) = T_l

d^2T/dx^2 = alpha_1 (T-T_s) + alpha_2(T^4-T_s^4)
T_s is the surrounding temperature


Shooting Method (convert BVP to IVP)
- Start at one end, guess the unknown intial values (T'(0))
- Correct T'(0) based on the error of T(L)_guess - T(L)
'''

# Take a simple parabola d^2y/dt^2 = -g
'''
Convert to a system of 1st order
[y, v]
[v, a] = [[0, 1], [-g/v]]*[y, v]
'''


import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g = 10
F = lambda t, s: np.array([s[1], -g])

# Given boundary conditions, y(0) = 0, y(5) = 35
# Need to guess y'(0)

t_eval = np.arange(0, 5.1, 0.1)

def objective(v0):
    sol = solve_ivp(F, [0, 5], y0=[0, v0[0]], method='RK45', t_eval=t_eval)
    y = sol.y[0]
    return y[-1] - 35

v0, = fsolve(objective, 10)

sol = solve_ivp(F, [0, 5], y0=[0, v0], method='RK45', t_eval=t_eval)

plt.figure(figsize=(12, 8))
plt.plot(sol.t, sol.y[0])
plt.plot(5, 35, 'ro')
plt.xlabel('t')
plt.ylabel('Height')
plt.grid(True)
plt.show()