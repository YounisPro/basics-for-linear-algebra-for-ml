from numpy import array
# importing triangular lower from numpy
from numpy import tril
# importing triangular upper from numpy
from numpy import triu

# creating triangular matrix
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])
print(M)
print("\n")

# lower triangular matrix
lower_tri_matrix = tril(M)
print(lower_tri_matrix)
print("\n")

# upper triangular matrix
upper_tri_matrix = triu(M)
print(upper_tri_matrix)