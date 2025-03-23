from numpy import array
# importing diagonal matrix function
from numpy import diag

# creating square matrix
M = array([
    [1, 2, 3],
    [1, 10, 3],
    [1, 2, 100]
])
print(M)
print("\n")

# creating diagonal vector
d = diag(M)
print(d)
print("\n")

# creating diagonal matrix from vector
D = diag(d)
print(D)