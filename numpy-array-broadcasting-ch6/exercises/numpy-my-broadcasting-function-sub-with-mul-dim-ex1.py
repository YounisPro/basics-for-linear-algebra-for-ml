from numpy import array
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating list of items
list = [
    [5, 10, 15],
    [20, 25, 30]
]

# creating array
arr = array(list)
print(arr)
print("\n")

# broadcasting variable
b = [4, 9, 14]
# here we get an filled w.r.t length of actual array to make
# it able to do arithematic ops
bArr = array(broadcasting_list(len(list), len(list[0]), b))
print(bArr)
print("\n")

# broadcasting/subtracting b array to actual array
result = arr - bArr
print(result)