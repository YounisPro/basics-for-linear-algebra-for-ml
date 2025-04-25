from custom_functions import compress_sparse
from custom_functions import todense
from numpy import array

# creating matrix
A = [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
]
print(A)

# Compressing nonzero values only
compressed_sparse = compress_sparse(A)
print(compressed_sparse)

# Converting back to dense matrix
dense_matrix = todense(compressed_sparse)
print(array(dense_matrix))