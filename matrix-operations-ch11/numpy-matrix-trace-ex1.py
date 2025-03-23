from numpy import array
# importing trace matrix function from numpy
from numpy import trace

# creating matrix
A = array([
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
])
print(A)
print("\n")

trace_result = trace(A)
print(trace_result)