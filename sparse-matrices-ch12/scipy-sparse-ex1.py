# sparse matrix example
from numpy import array
# importing csr_matrix from scipy.sparse
from scipy.sparse import csr_matrix

A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])
print(A)
# converting to sparse matrix (CSR method)
S = csr_matrix(A)
print(S)

# reconstruct dense matrix
B = S.todense()
print(B)