from numpy import array
# importing tranpose method to transpose matrix
from custom_functions import transpose

# creating orthogonal matrix
Q = [
    [0, 1],
    [-1, 0]
]
print(array(Q))
print("\n")

# inverse equivalence
T = transpose(Q)
print(array(T))
print("\n")

I = array(Q) @ array(T)
print(I)