import numpy as np
import scipy.interpolate as interp

x = [0, 1, 2]
y = [1, 3, 2]

# Simple linear interpolation using the neighboring points
f = interp.interp1d(x, y)
y_hat = f(1.5)
print(y_hat)

# More complex methods include Lagrange, Newton, and Cubic Spline