from custom_functions import dot_product
# creating vector one
v1 = [
    [1, 2, 3],
    [4, 5, 6]
]
print(v1)
print("\n")

# creating vector two
v2 = [1, 2, 3]
print(v2)
print("\n")

# dot product we do like this way
#          [ (v1[0][0] x v2[0]) + (v1[0][1] x v2[1]) + (v1[0][2] x v2[2]) ]
# result = [ (v1[1][0] x v2[0]) + (v1[1][1] x v2[1]) + (v1[1][2] x v2[2]) ]
result = dot_product(v1, v2)
print(result)