# importing custom multiply function for the matrix
from custom_functions import multiply

# Creating first matrix
A = [4, 5, 6]

print(A)
print("\n")

# creating second matrix
B = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(B)
print("\n")

# multiplying both matrices as it has correct order to do multiplication
# A.columns = B.rows
# resultant matrix = A.rows x B.columns
#                  = 1 x 2
# R = [
#       [ (4x1 + 5x3 + 6x5), (4x2 + 5x4 + 6x6) ]
#     ]
#
# R = [
#       [ 49, 28 ]
#     ]
R = multiply(A, B)
print(R)