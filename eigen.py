# Power method to find the largest/dominant eigenvalue
import numpy as np

def normalize(x):
    fac = abs(x).max() # Finds the maximum abs value
    x_n = x / x.max() # All elements in x between [-1, 1]
    return fac, x_n

x = np.array([1, 1])
a = np.array([[0, 2],
              [2, 3]])

for i in range(8):
    x = np.dot(a, x)
    lambda_1, x = normalize(x)

# Approaches larger eigenvalue and x approaches eigenvector after iterations
print(lambda_1)
print(x)

# Inverse method can be used to find the smallest eigenvalue
x = np.array([1, 1])
a_inv = np.linalg.inv(a)

for i in range(8):
    x = np.dot(a_inv, x)
    lambda_1, x = normalize(x)

print(lambda_1, x)

# Shifted Power Method
# [A - lambda_greatest*I]x can be used to determine the second largest eigenvalue
# This can be repeated to find all eigenvalues
# This is incredibly inefficient

# QR Method of determining Eigenvalues/Eigenvectors
# Factorize into an orthogonal matrix and an upper triangular matrix (diagonal is eigenvalues)

a = np.random.randint(0, 10, (2, 2))

q, r = np.linalg.qr(a)

# Approximate the eigenvalues by using A_k+1 = R_k*Q_k
# After many iterations, the diagonal stabilizes to the eigenvalues
for i in range(10):
    q, r = np.linalg.qr(a)
    a = np.dot(r, q)
    print(a)

# Numpy built in eigenvalue/eigenvector method
values, vectors = np.linalg.eig(a)
print(values)
print(vectors)