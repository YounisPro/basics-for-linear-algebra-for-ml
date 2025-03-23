from numpy import array
# importing custom function to transponse matrix
from custom_functions import transpose

# creating matrix
A = array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(A)
print("\n")

# transposing matrix
T = array(transpose(A))
print(T)