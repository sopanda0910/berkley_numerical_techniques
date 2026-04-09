import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))

# Define the vector components (U, V)
u = -y
v = x

plt.figure(figsize=(7, 7))
plt.quiver(x, y, u, v, color='teal')
# Also can show fluid flow by plt.streamplot()
plt.title("2D Vector Field (Quiver Plot)")
plt.show()

# Calculate vector magnitudes (lengths)
magnitudes = np.sqrt(u**2 + v**2)

print("Vector Field Statistics:")
print(f"Grid shape: {magnitudes.shape}")
print(".3f")
print(".3f")
print(".3f")

# Visualize magnitudes as colors
plt.figure(figsize=(8, 6))
plt.quiver(x, y, u, v, magnitudes, cmap='viridis', scale=15)
plt.colorbar(label='Vector Magnitude')
plt.title("Vector Field (Colored by Magnitude)")
plt.axis('equal')
plt.show()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

x,y,z = np.meshgrid(np.arange(-0.8, 1, 0.5), 
                    np.arange(-0.8, 1, 0.2),
                    np.arange(-0.8, 1, 0.2))

u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
plt.show()