import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

F = lambda t, s: np.cos(t)
t_eval = np.arange(0, np.pi, 0.01)

sol = solve_ivp(F, [0, np.pi], [0], method='RK45', t_eval=t_eval, rtol=1e-8, atol=1e-9)
# rtol and atol control relative (absolute) error

plt.figure(figsize = (12, 4))
plt.subplot(121)
plt.plot(sol.t, sol.y[0])
plt.xlabel("t")
plt.ylabel("S(t)")
plt.subplot(122)
plt.plot(sol.t, sol.y[0] - np.sin(sol.t)) # Error Term
plt.xlabel("t")
plt.ylabel("S(t) - sin(t)")
plt.tight_layout()
plt.show()

# Systems of ODE
F = lambda t, s: np.dot(np.array([[0, t**2], [-t**2, 0]]), s)

t_eval = np.arange(0, 5, 0.0001)
sol = solve_ivp(F, [0, 10], [0, 1], t_eval=t_eval)

plt.figure(figsize=(10, 8))
plt.plot(sol.y.T[:, 0], sol.y.T[:, 1])
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()