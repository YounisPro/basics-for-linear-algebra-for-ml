from numpy import array
# importing diag method to create diagonal vector and matrix
from custom_functions import diag

# creating matrix
A = [
    [1, 2, 3, 4],
    [1, 1, 3, 4],
    [1, 2, 2, 4],
    [1, 2, 3, 2]
]
print(array(A))
print("\n")

v = diag(A)
print(array(v))
print("\n")

D = diag(v)
print(array(D))

