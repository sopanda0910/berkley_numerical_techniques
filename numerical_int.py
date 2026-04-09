import numpy as np
import scipy.integrate as integration

x = np.linspace(0, np.pi, 11)
f = np.sin(x)

I = integration.trapezoid(f, x)
print(I)