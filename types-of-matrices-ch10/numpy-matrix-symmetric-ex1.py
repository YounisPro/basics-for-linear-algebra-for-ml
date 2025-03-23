from numpy import array

# creating symmetric matrix, we will verify using transposing matrix and will compare 
# if both if result is same or not
matrix = array([
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 4],
    [3, 2, 1, 2, 3],
    [4, 3, 2, 1, 2],
    [5, 4, 3, 2, 1]
])
print(matrix)
print("\n")

# Transposing matrix to verify it is symmetric or not
matrix_transpose = matrix.transpose()
print(matrix_transpose)
print("\n")

print(matrix == matrix_transpose)