# Floating point numbers are stored as a finite-bit base 2 fraction with an exponent and sign
import sys
import numpy as np

print(sys.float_info)
# Anything out of bounds will be overflow or underflow

# The gap from one number and the next, anything in between will be assigned to the same number
print(np.spacing(1e9))

print(1e9)
print(1e9 + np.spacing(1e9)/3) # Same as before

print(sys.float_info.max * 2)

# Arithmetic in floating point numbers is only an approximation, not correct
#
print(4.9 - 4.85 == 0.05)

print(4.9 - 4.85)
print(round(4.9 - 4.85) == round(0.05))