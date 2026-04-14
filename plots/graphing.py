import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

theta = np.linspace(-4*np.pi, 4*np.pi, 100)
z = np.linspace(0, 5, 100)
r = np.sqrt(z) + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='3D Parametric Curve', color='purple')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()

plt.show()