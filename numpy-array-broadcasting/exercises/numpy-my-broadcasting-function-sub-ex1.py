from numpy import array
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating list of items
list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# creating array
arr = array(list)
print(arr)
print("\n")

# broadcasting variable
b = 15
# here we get an array filled to the length of actual array to make 
# it able to do arithematic ops
bArr = array(broadcasting_list(len(list), len(list[0]), b))
print(bArr)
print("\n")

# broadcasting/subtracting b array from actual array
result = arr - bArr
print(result)