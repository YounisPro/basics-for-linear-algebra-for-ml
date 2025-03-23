from numpy import array

# creating first matrix
A = array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print("\n")

# creating second matrix
B = array([
    [1, 2],
    [3, 4]
])
print(B)
print("\n")

# multiplying both matrices as it has correct order to do multiplication
# A.columns = B.rows 
#
# A.columns = 2
# B.rows = 2
# resultant matrix = A.rows x B.columns
#                  = 3 x 2
# R = [ 
#       [ (1x1 + 2x3), (1x2 + 2x4) ],
#       [ (3x1 + 4x3), (3x2 +4x4) ],
#       [ (5x1 + 6x3), (5x2 + 6x4) ]
#     ]
#
# R = [
#       [ 7, 10 ],
#       [ 15, 22 ],
#       [ 23, 34]
#     ]
R = A.dot(B)
print(R)