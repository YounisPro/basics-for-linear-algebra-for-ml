# converting matrix to dense matrix
def todense(A):
    rows = A[0][0]
    cols = A[0][1]

    map = A[1]
    matrix = []
    for row in range(rows):
        dense_row = []
        for col in range(cols):
            key = f"({row},{col})"
            dense_row.append(map.get(key, 0) if key in map else 0)
        matrix.append(dense_row)
    
    return matrix

# converting matrix to compressed sparse matrix
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
    
    size = [rows, cols]
    return [size, map]

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