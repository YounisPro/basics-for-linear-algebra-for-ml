from numpy import array
# creating first matrix of one row
A = array([
    [1, 2, 3]
])

# creating second matrix of three rows and three columns
B = array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

# multiplying both matrices as it has correct order to do multiplication
# A.columns = B.rows 
#
# A.columns = 3
# B.rows = 3
# resultant matrix = A.rows x B.columns
#                  = 1 x 3
# R = [ 
#       (1x2 + 2x8 + 3x14),
#       (1x4 + 2x10 + 3x16),
#       (1x6 + 2x12 + 3x18)
#     ]
# R = [[60, 72, 84]]
R = A @ B
print(R)