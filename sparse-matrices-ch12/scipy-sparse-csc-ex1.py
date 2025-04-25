# importing array
from numpy import array
# importing csc_matrix compression from scipy.sparse
from scipy.sparse import csc_matrix
from scipy.sparse import csr_matrix

A = array([
    [1, 0, 0, 2, 0, 0],
    [0, 0, 3, 0, 0, 4],
    [0, 0, 0, 5, 0, 0]
])
# print(A)

S = csc_matrix(A)
print(S)


B = S.todense()
print(B)