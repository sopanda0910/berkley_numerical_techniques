# Explicit Euler Method
# S(t_j+1) = S(t_j) + h*F(t_j, S(t_j))
# F is the differential equation

# For df/dt = exp(-t)
import numpy as np
import matplotlib.pyplot as plt

f = lambda t: np.exp(-t)
h = 0.1
h_imp = 0.01
t = np.arange(0, 1, h)
t_imp = np.arange(0, 1, h_imp)
# Initial Condition
s_0 = -1

s = np.zeros(len(t))
s_imp = np.zeros(len(t_imp))
s[0] = s_0
s_imp[0] = s_0

for i in range(len(t) - 1):
    s[i+1] = s[i] + h*f(t[i])

for i in range(len(t_imp) - 1):
    s_imp[i+1] = s_imp[i] + h_imp*f(t_imp[i])

plt.figure(figsize=(14, 8))
plt.plot(t, s, "b--", label="Approximate")
plt.plot(t_imp, s_imp, "k--", label="Better Approximate")
plt.plot(t, -np.exp(-t), "g", label="Exact")
plt.xlabel('t')
plt.ylabel('f')
plt.grid(True)
plt.legend()
plt.show()

