from numpy import array
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating list of items
list = [
    [1, 2, 3],
    [4, 5, 6]
]

# creating array
arr = array(list)
print(arr)
print("\n")

# broadcasting variable
b = 8 
# here we get an array filled to the length of actual array to make 
# it able to do arithematic ops
bArr = array(broadcasting_list(len(list), len(list[0]), b))
print(bArr)
print("\n")

# broadcasting/adding b array to actual array
result = arr + bArr
print(result)