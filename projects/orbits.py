import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 10000)

m = 1e24
alpha = (6.67*1e-11)*(1e30)*(1e24)
J_i = 2.6*1e40
E_i = -2.65*(1e30)

energies = [E_i]
momenta = [J_i]

# Create energy range - use E_i * (10**i) instead to make energies less negative
for i in range(1, 3):
    energies.append(E_i * (10**(-i)))  # Gets closer to zero (less negative)
    momenta.append(J_i * (10**(-i)))

plt.figure(figsize=(14,8))

for i in range(3):
    E = energies[i]

    r_0 = (J_i**2)/(alpha*m)

    arg = 1 + 2*E*(J_i**2)/(m*alpha**2)
    print(f"Energy {i}: E = {E:.2e}, arg = {arg:.6f}")

    ecc = np.sqrt(arg)

    r = r_0 / (1 + ecc*np.cos(theta))

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    plt.subplot(2, 3, i+1)
    plt.title(f'E = {E:.2e}\necc = {ecc:.4f}')
    plt.plot(x, y)
    plt.axis('equal')
    plt.grid(True)

for i in range(3):
    J = momenta[i]
    r_0 = (J**2)/(alpha*m)

    arg = 1 + 2*E_i*(J**2)/(m*alpha**2)
    print(f"Momentum {i}: J = {J:.2e}, arg = {arg:.6f}")

    ecc = np.sqrt(arg)

    r = r_0 / (1 + ecc*np.cos(theta))

    x = r*np.cos(theta)
    y = r*np.sin(theta)

    plt.subplot(2, 3, i+4)  # Changed from (5, 3, i+1) to (2, 3, i+4)
    plt.title(f'J = {J:.2e}\necc = {ecc:.4f}')
    plt.plot(x, y)
    plt.axis('equal')
    plt.grid(True)


plt.tight_layout()
plt.show()
