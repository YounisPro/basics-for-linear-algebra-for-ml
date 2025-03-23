def identity(size):
    rows = size
    cols = size

    arr = []
    for i in range(rows):
        tmpArr = []
        for j in range(cols):
            if i==j:
                tmpArr.append(1)
            else: 
                tmpArr.append(0)
        arr.append(tmpArr)
    return arr

# to create transpose matrix
def transpose(A):
    rows = len(A)
    cols = len(A[0])

    arr = []
    for i in range(rows):
        tmpArr = []
        for j in range(cols):
            tmpArr.append(A[j][i])
        arr.append(tmpArr)

    return arr

# to create upper triangular matrix 
def triu(A):
    return tri(A, True)

# to create lower triangular matrix 
def tril(A):
    return tri(A, False)

def tri(A, upper):
    rows = len(A)
    cols = len(A[0])
    arr = []
    for i in range(rows):
        tmpArr = []
        for j in range(cols):
            if (upper and j>(i-1)) or (not upper and j<(i+1)):
                tmpArr.append(A[i][j])
            else:
                tmpArr.append(0)
        arr.append(tmpArr)
    return arr