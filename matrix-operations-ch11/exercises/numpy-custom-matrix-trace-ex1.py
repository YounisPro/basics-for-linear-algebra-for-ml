from numpy import array
# importing trace matrix function from numpy
from custom_functions import trace

# creating matrix
A = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
print(array(A))
print("\n")

trace_result = trace(A)
print(array(trace_result))