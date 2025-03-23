# importing custom multiply function for the matrix
from custom_functions import multiply

# Creating first matrix
A = [
    [4, 5],
    [10, 20]
]
print(A)
print("\n")

# creating second matrix
B = [
    [1, 2],
    [2, 4]
]
print(B)
print("\n")

# multiplying both matrices as it has correct order to do multiplication
# A.columns = B.rows
# resultant matrix = A.rows x B.columns
#                  = 2 x 2
# R = [
#       [ (4x1 + 5x2), (4x2 + 5x4) ],
#       [ (10x1 + 20x2), (10x2 + 20x4) ]
#     ]
#
# R = [
#       [ 14, 28 ],
#       [ 50, 100 ]
#     ]
R = multiply(A, B)
print(R)