from numpy import array

def matrix_rank(A):
    rows = len(A)
    cols = len(A[0])
    matrix_rank_map = {}
    matrix_map = {}
    all_cols_0 = {}

    for i in range(rows):
        key = ":".join(map(str,A[i]))
        zeros_key = ":".join(["0"] * len(A[i]))
        
        if key in matrix_rank_map:
            matrix_rank_map[key] = 1
        elif zeros_key != key:
            matrix_rank_map[key] = 1
            matrix_map[key] = A[i]
            all_cols_0[A[i][0]] = A[i]
    
    for key in matrix_map:
        for k in matrix_map:
            if k != key:
                arr1 = matrix_map[key]
                arr2 = matrix_map[k]
            
                divident_map = {}
                for i in range(len(arr1)):
                    # print(arr2[i]," % ",arr1[i])
                    if arr2[i] % arr1[i] == 0:
                        # print(arr2[i]," / ",arr1[i])
                        divident = arr2[i] / arr1[i]
                        
                        if divident in divident_map:
                            divident_map[divident] = divident_map[divident]+1
                        else: 
                            divident_map[divident] = 1
                
                if len(divident_map) == 1 and list(divident_map.values())[0] == float(len(arr1)):
                    matrix_rank_map[key] = matrix_rank_map[key]-1 
    
    return sum(matrix_rank_map.values())

# this method is used to sum matrix diangonally from top left to bottom right
def trace(A):
    rows = len(A)
    cols = len(A[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum += A[i][j]
    return sum

# this method is used to inverse matrix
def inv(A):
    determinant = det(A)
    
    if determinant != 0:
        adjugate = adj(A)
        
        T = transpose(adjugate)
        rows = len(T)
        cols = len(T[0])
        arr = []
        for i in range(rows):
            tmpArr = []
            for j in range(cols):
                tmpArr.append(adjugate[i][j]/determinant)
            arr.append(tmpArr)
        return arr
    else:
        return A

# this method is used to get adjugate of matrix
def adj(A):
    if len(A) == 2:
        return [
            [A[1][1], -A[0][1]],
            [-A[1][0], A[0][0]]
        ]
    else:
        return detArr(A, 1)
    
# this method is used to get determinants array
def detArr(A, multiplier):
    rows = len(A)

    arr = []
    if rows>2:
        for i in range(rows):
            pArr = []
            for j in range(rows):
                tmpArr = []
                for k in range(rows):
                    if k != i and j != 0:
                        tmpArr.append(A[j][k])
                
                if len(tmpArr)>0:
                    pArr.append(tmpArr)
            pArr = detArr(pArr, A[0][i])
            arr.append(pArr)
    else:
        sum = multiplier*((A[0][0] * A[1][1]) - (A[0][1] * A[1][0]))
        arr = sum
    
    return arr

# this method is used to get determinant value of matrix
def det(A):
    arr = detArr(A, 1)
    if isinstance(arr,int) or isinstance(arr,float):
        return arr
    
    rows = 1 if isinstance(arr[0],int) else len(arr)
    cols = len(arr) if isinstance(arr[0],int) else len(arr[0])
    
    if isinstance(arr[0],int):
        arr = [arr]
    determinants = 0
    for i in range(rows):
        sum = 0
        for j in range(cols):
            # print( arr[i][j])
            sum = (sum - arr[i][j] if j%2 != 0 else sum + arr[i][j])
        determinants = (determinants - A[0][i] * sum) if i%2 != 0 else (determinants + A[0][i] * sum)
    return determinants

def diag(A):
    isSingleRow = True if isinstance(A[0], int) else False
    arr = []
    if isSingleRow:
        rows = len(A)
        cols = len(A)

        for i in range(rows):
            tmpArr = []
            for j in range(cols):
                if i==j:
                    tmpArr.append(A[i])
                else:
                    tmpArr.append(0)
            arr.append(tmpArr)
    else:
        rows = len(A)
        cols = len(A[0])
        
        for i in range(rows):
            for j in range(cols):
                if i==j:
                    arr.append(A[i][j])
    return arr

# to create identity marix
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