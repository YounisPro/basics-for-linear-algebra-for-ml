# create empty array
from numpy import empty

# by data type of empty is float
# a = empty([3,3])
# here setting data type to int
a = empty([3,3],dtype=int)
print(a)
# printing shape of array
print(a.shape)
# printing data type of array
print(a.dtype)