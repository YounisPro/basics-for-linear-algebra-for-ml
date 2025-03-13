from numpy import array
from numpy import hstack
# creating first array
a1 = array([1,2,3])
print(a1)

# creating second array
a2 = array([4,5,6])
print(a2)

# creating horizontally combined stack
combinedArray = hstack((a1,a2))
print(combinedArray)
# printing shape of combined array
print(combinedArray.shape)
# printing data type of combined array
print(combinedArray.dtype)