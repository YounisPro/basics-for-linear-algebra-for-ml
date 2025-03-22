from custom_functions import dot_product

# creating vector one
v1 = [1, 2, 3]
print(v1)
print("\n")

# creating vector two
v2 = [
    [1],
    [2],
    [3]
]
print(v2)
print("\n")

# dot product we do like this way
#
# result = [ (v1[0] x v2[0][0]) + (v1[1] x v2[1][0]) + (v1[2] x v2[2][0]) ]
# result = [14]
result = dot_product(v1, v2)
print(result)