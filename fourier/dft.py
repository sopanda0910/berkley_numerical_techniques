# Discrete Fourier Transform
import matplotlib.pyplot as plt
import numpy as np

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

plt.figure(figsize = (8, 6))
plt.plot(t, x, "r")
plt.ylabel("Amplitude")
# plt.show()

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x) # Does the sum/integral for each X_k and vectorizes
    return X

X = DFT(x)

def inv_DFT(X):
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    # k*n is an NxN Matrix
    e = np.exp(2j*np.pi*k*n/N) # Exponentiating Component Wise
    # e becomes the inv DFT Kernel Matrix, of all of the complex exponentials
    x = (1/N)*np.dot(e, X)

    return x

N = len(X)
n = np.arange(N)
T = N/sr # Total Time (Numbers of Points / Sampling Rate)
freq = n/T # Converts the bins to frequencies

x_inv = inv_DFT(X)

plt.figure(figsize = (8, 6))
plt.stem(freq, abs(X), "b", markerfmt=" ")
plt.xlabel("Freq (Hz)")
plt.ylabel("DFT Amplitude |X(freq)|")

plt.figure(figsize=(8, 6))
plt.plot(t, x_inv)
plt.grid(True)
plt.show()
# This result is symmetric about half the sampling rate (Nyquist Frequency)