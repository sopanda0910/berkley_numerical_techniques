import numpy as np
from scipy import optimize

f = lambda x : np.cos(x) - x
r = optimize.fsolve(f, -2) # Finds a root near -2
print(r)
print(f(r))

# Bisection method
'''
Repeated use of intermediate value theorem
a, b such that f(a) > 0 and f(b) < 0
new guesses are (b+a)/2
'''

# Newton Raphson Method
'''
Repeated linearly approximate a function and use the x-intercept
of the line as the next guess
'''