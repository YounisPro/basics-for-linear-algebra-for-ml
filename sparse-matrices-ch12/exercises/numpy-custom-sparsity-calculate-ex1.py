from custom_functions import size
from custom_functions import count_nonzero

# create dense matrix
A = [
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
]
print(A)

sizeof_matrix = size(A)
nonzero_values = count_nonzero(A)
sparsity = 1.0 - nonzero_values/sizeof_matrix

print("Size of matrix A: ", sizeof_matrix)
print("Nonzero values in matrix A: ", nonzero_values)
print("Sparsity of matrix A: ", sparsity)