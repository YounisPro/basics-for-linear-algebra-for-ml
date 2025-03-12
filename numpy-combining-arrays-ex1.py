# create array with vstack
from numpy import array
from numpy import vstack
# create first array
a1 = array([1,2,3])
# printing first array
print(a1)
# create second array
a2 = array([4,5,6])
print(a2)
# vertical stack
combinedArray = vstack((a1,a2));
print(combinedArray)
