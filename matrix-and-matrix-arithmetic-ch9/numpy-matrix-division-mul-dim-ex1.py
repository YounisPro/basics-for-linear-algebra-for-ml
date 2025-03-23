from numpy import array
# creating first matrix
A = array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
print(A)
print("\n")

# creating second matrix
B = array([
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
])
print(B)
print("\n")

C = A / B
print(C)