from numpy import array
# creating data list
data = [
    [11, 22],
    [33, 44],
    [55, 66]
]

# array of data
arr1 = array(data)
print(arr1.shape)

# Reshaping 2D to 3D
arr1 = arr1.reshape((arr1.shape[0], arr1.shape[1], 1))
print(arr1)