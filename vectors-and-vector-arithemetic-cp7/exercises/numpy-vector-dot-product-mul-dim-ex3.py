from numpy import array
# creating vector one
v1 = array([1, 2, 3])
print(v1)
print("\n")

# creating vector two
v2 = array([
    [1],
    [5],
    [3]
])
print(v2)
print("\n")

# dot product we do like this way
#
# result = [ (v1[0] x v2[0][0]) + (v1[1] x v2[1][0]) + (v1[2] x v2[2][0]) ]
# doing
result = v1.dot(v2)
print(result)