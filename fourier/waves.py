import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 201)
y = np.sin(x)

fig = plt.figure(figsize=(12, 10))

times = np.arange(5)
n = len(times)

for t in times:
    plt.subplot(n, 1, t+1)
    y = np.sin(x+2*t)
    plt.plot(x, y, "b")
    plt.plot(x[25], y[25], 'ro')
    plt.ylim(-1.1, 1.1)

plt.tight_layout()
plt.show()

