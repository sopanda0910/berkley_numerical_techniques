import numpy as np
import matplotlib.pyplot as plt

# Method 1: Multiple plots overlaid on the same axes
plt.figure(figsize=(10, 6))

x = np.linspace(0, 6, 100)
plt.plot(x, x**2, 'b-', label='y = x²', linewidth=2)
plt.plot(x, x**3, 'r--', label='y = x³', linewidth=2)
plt.plot(x, np.sqrt(x), 'g:', label='y = √x', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Multiple Functions on Same Plot')
plt.legend()
plt.grid(True)
plt.show()

# Method 2: Subplots (multiple plots in grid layout)
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Multiple Subplots Example')

x = np.linspace(0, 6, 100)

# Top-left subplot
axes[0, 0].plot(x, x**2, 'b-')
axes[0, 0].set_title('Quadratic: y = x²')
axes[0, 0].grid(True)

# Top-right subplot
axes[0, 1].plot(x, np.sin(x), 'r-')
axes[0, 1].set_title('Sine: y = sin(x)')
axes[0, 1].grid(True)

# Bottom-left subplot
axes[1, 0].plot(x, np.exp(x/3), 'g-')
axes[1, 0].set_title('Exponential: y = e^(x/3)')
axes[1, 0].grid(True)

# Bottom-right subplot (scatter plot)
x_scatter = np.array([0, 2, 4, 6])
y_scatter = np.array([0, 4, 16, 36])
axes[1, 1].scatter(x_scatter, y_scatter, color='purple', s=100)
axes[1, 1].set_title('Scatter Plot')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

# Method 3: Side-by-side plots
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)  # 1 row, 3 columns, position 1
x1 = np.linspace(0, 6, 100)
plt.plot(x1, x1**2)
plt.title('Plot 1: x²')
plt.grid(True)

plt.subplot(1, 3, 2)  # 1 row, 3 columns, position 2
x2 = np.linspace(-2, 2, 100)
plt.plot(x2, x2**3)
plt.title('Plot 2: x³')
plt.grid(True)

plt.subplot(1, 3, 3)  # 1 row, 3 columns, position 3
x3 = np.linspace(0, 10, 100)
plt.plot(x3, np.log(x3 + 1))
plt.title('Plot 3: log(x+1)')
plt.grid(True)

plt.tight_layout()
plt.show()
plt.show()

x_points = np.random.randint(0, 10, 10)
y_points = np.random.randint(0, 10, 10) 

# Scatter plot
plt.plot(x_points, y_points, 'o') # Dots rather than a straight line
# Without the 'o', it will connect all of the points by straight lines
plt.grid(True)
plt.show()