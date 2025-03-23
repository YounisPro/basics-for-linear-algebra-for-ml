from numpy import array
# creating first matrix
A = array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A)
print("\n")

# creating secondd matrix
B = array([
    [0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5]
])

# subtracting both matrices
C = A - B
print(C)