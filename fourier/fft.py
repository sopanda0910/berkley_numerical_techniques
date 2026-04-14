# Exploiting the symmetries of DFT
# By the formula of DFT, X_(k+N) = X_k, since exp(2pi*j*n) = 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Sampling Rate
sr = 100

# Sampling Interval
ts = 1.0/sr

t = np.arange(0, 2, ts)


# Creating the combination signal
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7
x += 0.5* np.sin(2*np.pi*freq*t)

X = np.fft.fft(x)
X_sci = fft(x)

N = len(X)
n = np.arange(N)
T = N*ts
freq = n/T

freq = n/T

plt.figure(figsize=(10, 8))
plt.plot(t, x)

plt.figure(figsize=(10, 8))
plt.stem(freq, abs(X), markerfmt=' ', basefmt='-b')
plt.grid(True)

plt.figure(figsize=(10, 8))
plt.stem(freq, abs(X_sci), markerfmt=' ', basefmt='-b')
plt.grid(True)

plt.show()