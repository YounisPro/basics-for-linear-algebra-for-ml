# v1 = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# v2 = [1, 2, 3]
# this function will do dot product of two vectors
def dot_product(v1, v2):
    v1IsSingle = True if isinstance(v1[0],int) else False
    v1Size = len(v1)
    v1InnerSize = len(v1) if isinstance(v1[0],int) else len(v1[0])

    v2IsSingle = True if isinstance(v2[0],int) else False
    v2Size = 1 if isinstance(v2[0],int) else len(v2[0]) if v1IsSingle else len(v2)
    v2InnerSize = len(v2) if isinstance(v2[0],int) else len(v2[0])
    v1Andv2IsEqual = v1InnerSize == v2InnerSize

    print('v1Size: ',v1Size,', v1InnerSize: ',v1InnerSize)
    print('v2Size: ',v2Size,', v2InnerSize: ',v2InnerSize)
    tmpArr = []
    for i in range(v2Size):
        arr = []
        sum = 0
        if v1Andv2IsEqual and v2IsSingle and v1IsSingle:
            for j in range(v1InnerSize):
                sum += v1[j]*v2[j]
            arr.append(sum)
            sum = 0
            tmpArr.append(arr)
        elif v1IsSingle:
            for j in range(v1InnerSize):
                sum += v1[j]*v2[j][i]
            arr.append(sum)
            sum = 0
            tmpArr.append(arr)
        elif not v1IsSingle and not v2IsSingle and v1InnerSize == 1:
            for j in range(v1Size):
                arr =[]
                for k in range(v2InnerSize):
                    sum += v1[j][0] * v2[0][k]
                    arr.append(sum)
                    sum = 0
                tmpArr.append(arr)
        else:
            for j in range(v1Size):
                for k in range(v1InnerSize):
                    sum += v1[j][k] * v2[k]
                arr.append(sum)
                sum = 0
            tmpArr.append(arr)
    return tmpArr