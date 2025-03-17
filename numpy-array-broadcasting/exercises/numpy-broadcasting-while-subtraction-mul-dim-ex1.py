from numpy import array
# creating matrix
arr = array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])
# printing array 
print(arr)
print("\n")

# defining broadcaster/scaler variable
b = 2

# broadcasting/subtrating scaler b from 
# the mul dimension array 
result = arr - b
# printing result array
print(result)