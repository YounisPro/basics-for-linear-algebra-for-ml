from numpy import array
# importing cuustom triangular lower matrix function
from custom_functions import tril
# importing cuustom triangular upper matrix function
from custom_functions import triu

# Creating matrix to find triangular matrix
M = [
    [1, 2, 3, 5, 6],
    [2, 1, 2, 5, 6],
    [3, 2, 1, 5, 6],
    [3, 2, 1, 5, 6],
    [3, 2, 1, 5, 6]
]


lower_tri_matrix = tril(M)
print(array(lower_tri_matrix))
print("\n")

# upper triangular matrix
upper_tri_matrix = triu(M)
print(array(upper_tri_matrix))