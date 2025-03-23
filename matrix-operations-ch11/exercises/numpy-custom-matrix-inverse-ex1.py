from numpy import array
# importing invert function inv from linear algebra package numpy
from custom_functions import det
from custom_functions import inv

# creating matrix
A = array([
    [1.0, 2.0],
    [3.0, 4.0]
])
print(A)
print("\n")

# invert matrix
B = inv(A)
print(B)
print("\n")

# multiplying Matrix A and B
I = array(A).dot(array(B))
print(I)