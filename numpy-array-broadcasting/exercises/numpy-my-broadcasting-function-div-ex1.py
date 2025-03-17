from numpy import array
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating list of items
list = [
    [100, 200, 300],
    [400, 500, 600]
]

# creating array
arr = array(list)
print(arr)
print("\n")

# broadcasting variable
b = 100
# here we get an array filled w.r.t length of actual array to make
# it able to do arithematic ops
bArr = array(broadcasting_list(len(list), len(list[0]), b))
print(bArr)
print("\n")

# broadcasting/dividing b array from actual array
result = arr / bArr
print(result)