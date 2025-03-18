from numpy import array
# creating array
arr = array([
    [11, 12, 13],
    [14, 15, 17],
    [18, 19, 20]
])
# printing array
print(arr)
print("\n")

# broadcasting variable
b = 10
print(b)

# broadcasting/Modulus using b variable to all indices of array
result = arr % b
print(result)