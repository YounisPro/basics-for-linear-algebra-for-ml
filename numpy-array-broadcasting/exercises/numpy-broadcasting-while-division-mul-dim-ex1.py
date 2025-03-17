from numpy import array
# creating array
arr = array([
    [9, 18, 27],
    [36, 45, 54],
    [63, 72, 81]
])
# printing array
print(arr)
print("\n")

# broadcasting variable
b = 9
print(b)
print("\n")

# broadcasting/dividing b variable from each index of array
result = arr / b
print(result)