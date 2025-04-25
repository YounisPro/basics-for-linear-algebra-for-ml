# sparsity calculation
from numpy import array
from numpy import count_nonzero

# create dense matrix
A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])
print(A)

# nonzero values and size of matrix
nonzero_values = count_nonzero(A) 
size_of_matrix = A.size

# calculating sparsity
sparsity = 1.0 - nonzero_values / size_of_matrix
print("\nSparsity of Matrix A: ",sparsity)