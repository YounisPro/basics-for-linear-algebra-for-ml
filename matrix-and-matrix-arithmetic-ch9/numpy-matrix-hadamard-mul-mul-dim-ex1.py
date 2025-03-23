from numpy import array
# creating first matrix
A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# creating second matrix
B = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# hadamard product/multiplying both matrices
C = A * B
print(C)