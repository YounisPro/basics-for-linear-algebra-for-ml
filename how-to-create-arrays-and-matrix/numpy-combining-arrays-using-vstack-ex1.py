# create array with vstack
from numpy import array
from numpy import vstack
# create first array
a1 = array([1,2,3])
# printing first array
print(a1)
# printing shape of first array
print(a1.shape);
# printing data type of first array
print(a1.dtype)

# create second array
a2 = array([4,5,6])
print(a2)
# printing shape of second array
print(a2.shape)
# printing data type of second array
print(a2.dtype)

# creating combined using vertical stack
combinedArray = vstack((a1,a2));
print(combinedArray)
# printing shape of combined array
print(combinedArray.shape)
# printing dtype of combined array
print(combinedArray.dtype)