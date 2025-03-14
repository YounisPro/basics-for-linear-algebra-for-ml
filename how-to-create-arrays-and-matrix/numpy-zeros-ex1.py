# create zeros array
from numpy import zeros
# default data type of zeros array is float64
# a = zeros([3,5])
# setting data type to int for zeros array
a = zeros([3,5], dtype=int)
print(a);
# printing shape of array
print(a.shape)
# printing dtype of array
print(a.dtype)