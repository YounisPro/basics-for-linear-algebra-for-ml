from numpy import array
# creating matrix 
A = array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print("\n")

# creating vector
v = array([0.5, 1])
print(v)
print("\n")

# multiplying matrix with vector
#
# R = [
#       (1x0.5 + 2x1),
#       (3x0.5 + 4x1),
#       (5x0.5 + 6x1)
#     ]
#
# R = [2.5, 5.5, 8.5]
R = A.dot(v)
print(R)