# converting matrix to csr
def compress_sparse(A):
    rows = len(A) if isinstance(A[0], list) else 1
    cols = len(A[0]) if isinstance(A[0], list) else len(A)
    A = A if isinstance(A[0], list) else [A]

    map = {}
    for row in range(rows):
        for col in range(cols):
            if A[row][col] != 0:
                key = "("+str(row)+","+str(col)+")"
                map[key] = A[row][col]
    return map

# to calculate number of nonzero values in a matrix
def count_nonzero(A):
    rows = len(A) if isinstance(A[0], list) else 1 
    cols = len(A[0]) if isinstance(A[0], list) else len(A)
    A = A if isinstance(A[0], list) else [A]
    nonzero = 0

    for row in range(rows):
        for col in range(cols):
            nonzero += 1 if(A[row][col] != 0) else 0

    return nonzero

# getting size of matrix
def size(A):
    rows = len(A) if isinstance(A[0], list) else 1
    cols = len(A[0]) if isinstance(A[0], list) else len(A)

    return rows*cols