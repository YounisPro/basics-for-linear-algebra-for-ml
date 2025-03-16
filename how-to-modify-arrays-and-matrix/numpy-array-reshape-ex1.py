from numpy import array
# creating array
data = array([11, 22, 33, 44, 55, 66])
print(data.shape)
print(data)
print("\n")

# Reshape
arr1 = data.reshape((data.shape[0],1))
print(arr1.shape)
print(arr1)