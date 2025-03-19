from numpy import array
# creating vector one
v1 = array([1, 2, 3])
print(v1)
print("\n")

# creating vector two
v2 = array([1, 2, 3])
print(v2)
print("\n")

# dot prodct we do like this way
# result = [(v1[0] x v2[0]) + (v1[1] x v2[1]) + (v1[2] x v2[2])]
# doing dot product
result = v1.dot(v2)
print(result)