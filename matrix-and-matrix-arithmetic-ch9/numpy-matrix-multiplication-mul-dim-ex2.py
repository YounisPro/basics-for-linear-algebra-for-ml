from numpy import array
# creating first matrix
A = array([1, 2, 3])
print(A)
print("\n")

# creating second matrix
B = array([
    [1],
    [2],
    [3]
])
print(B)
print("\n")

# multiplying both matrices as it has correct order to do multiplication
# A.columns = B.rows
#
# A.columns = 3
# B.rows = 3
# resultant matrix = A.rows x B.columns
#                  = 1 x 1
# R = [ 1x1 + 2x2 + 3x3 ]
# R = [14]
R = A @ B
print(R)