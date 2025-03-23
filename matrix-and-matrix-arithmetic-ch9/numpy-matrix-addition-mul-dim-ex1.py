from numpy import array
# creating first matrix
A = array([
    [1, 2, 3],
    [4, 5, 6]
])
print(A)
print("\n")

# creating second matrix
B = array([
    [1, 2, 3],
    [4, 5, 5]
])
print(B)
print("\n")

# adding both matrices
C = A + B
print(C)