from numpy import array
# creating matrix
A = array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print("\n")

# creating scaler value
b = 0.5
print(b)
print("\n")

# multiplying scaler to matrix
#
# R = [
#       [ 1x0.5, 2x0.5 ],
#       [ 3x0.5, 4x0.5 ],
#       [ 5x0.5, 6x0.5 ]
#     ]
R = A * b
print(R)