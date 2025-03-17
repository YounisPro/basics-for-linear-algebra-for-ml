from numpy import array
# creating array
arr = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr)
print("\n")

# broadcasting variable
b = 8
print(b)
print("\n")

# broadcasting/multiplying b variable to each index
result = arr * b
print(result)