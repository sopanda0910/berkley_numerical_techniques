# Predictor-Corrector Method
# Predicts S(t_j+1), and then finds some correcting order terms
# Midpoint, using F(t_j + h/2, S(t_j + h/2))

# Range-Kutta Method
# Second-Order RK Method
'''
# General form for a 1-step predictor-corrector method
S(t+h) = S(t) + c_1*F(t, S(t))*h + c_2*F(t+ph, S(t)+qhF(t, S(t)))*h
# c_1 is the euler part, and c_2 is the corrector term, where F is evaluated at a future time and state

F'(t) = dF/dt + dF/dS*dS/dt = dF/dt + dF/dS*F

S(t+h) = S(t) + Fh + 1/2(dF/dt + dF/dS*F)h^2

Using steps F(t+ph, S + qhF) = F + ph*dF/dt + qhF*dF/dS

S(t+h) = S(t) + (c_1 + c_2)*Fh + c_2(dF/dt*p + q*dF/dS*F)h^2
(c_1 + c_2) = 1 (since it is a weighted average)
c_2p = 1/2 and c_2q = 1/2 from the Second Order approximation of S(t+h)

k_1 = F(t_j, S(t_j))
k_2 = F(t_j + ph, S(t_j) + qhk_1)

S(t_j+1) = S(t_j) + h/2(k_1 + k_2)
'''

# 4th order RK Method
'''
k_1 = F(t_j, S(t_j))
k_2 = F(t_j + h/2, S(t_j) + h/2*k_1)
k_3 = F(t_j + h/2, S(t_j) + h/2*k_2)
k_4 = F(t_j + h, S(t_j) + k_3*h)

S(t_j+1) = S(t_j) + h/6(k_1 + k_2 + k_3 + k_4)
'''

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Consider F = e^-t(cos(s))
F = lambda t, s: np.exp(-t)*np.cos(s)
h = 0.05
t_eval = np.arange(0, 1.5, h)
sol = solve_ivp(F, [0, 1.5], [0], method='RK45', t_eval=t_eval, rtol=1e-8, atol=1e-9)

S = np.zeros(len(t_eval))
S[0] = 0

for i in range(1, len(t_eval)):
    k_1 = F(t_eval[i], S[i-1])
    k_2 = F(t_eval[i] + h/2, S[i-1] + h/2 * k_1)
    k_3 = F(t_eval[i] + h/2, S[i-1] + h/2 * k_2)
    k_4 = F(t_eval[i] + h, S[i-1] + h*k_3)

    S[i] = S[i-1] + (h/6)*(k_1 + k_2 + k_3 + k_4)

plt.figure(figsize=(12, 10))
plt.plot(t_eval, sol.y.T, 'k--')
plt.plot(t_eval, S, 'b--')
plt.grid(True)
plt.show()