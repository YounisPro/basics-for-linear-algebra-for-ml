from numpy import array
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating list of items
list = [
    [22, 24, 26, 28],
    [30, 32, 34, 36],
    [38, 40, 42, 44]
]

# creating array
arr = array(list)
print(arr)
print("\n")

# broadcasting variable
b = 20
bArr = array(broadcasting_list(len(list), len(list[0]), b))
print(bArr)
print("\n")

# broadcasting/modulas b array from actual array
result = arr % bArr
print(result)