from numpy import array
# creating vector one

v1 = array([
    [1],
    [4],
    [8],
    [10]
])
print(v1)
print("\n")

# creating vector two
v2 = array([
    [1, 2, 3]
])
print(v2)
print("\n")

# dot product we do like this way
#          [ (v1[0][0] x v2[0]), (v1[0][0] x v2[1]), (v1[0][0] x v2[2]) ]
#          [ (v1[1][0] x v2[0]), (v1[1][1] x v2[1]), (v1[1][0] x v2[2]) ]
# result = [ (v1[2][0] x v2[0]), (v1[2][2] x v2[1]), (v1[2][0] x v2[2]) ]
#
#          [ 1, 2, 4 ]
#          [ 4, 8, 12]
# result = [ 8, 16, 24]
result = v1.dot(v2)
print(result)