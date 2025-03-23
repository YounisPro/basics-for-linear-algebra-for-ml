from numpy import array
# importing determinant function det from numpy package
from numpy.linalg import det

# creating matrix
A = array([
   [ 1,   2,  3],
    [ 5,   6,  7],
    [ 8,  10, 11]
])
print(A)
print("\n")

# generating determinant of above matrix
#
# D = A[0][0]x( A[1][1]xA[2][2] - A[1][2]xA[2][1] ) - A[0][1]x( A[1][0]xA[2][2] - A[1][2]xA[2][0] ) + A[0][2]x( A[1][0]xA[2][1] - A[1][1]xA[2][1] ))
#
# D = 1x( 6x11 - 7x10 ) - 2x( 5x11 - 7x8 ) + 3x( 5x10 - 6x8 ))
#     
# D = (66 - 70) - 2x(55 - 56) + 3x(50 - 48)
# D = -4 - 2x(-1) + 3x(2)
# D = -4 +2 +6
# D = 4
D = det(A)
print(D)