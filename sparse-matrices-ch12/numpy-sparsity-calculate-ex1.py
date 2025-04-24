# sparsity calculation
from numpy import array
from scipy.sparse import count_nonzero
# create dense matrix
A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])
print(A)
# 