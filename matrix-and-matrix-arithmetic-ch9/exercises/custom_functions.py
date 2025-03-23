def multiply(A, B):
    matrixOneIsSingle = True if isinstance(A[0], int) else False
    matrixOneRows = 1 if isinstance(A[0],int) else len(A)
    matrixOneCols = len(A) if isinstance(A[0], int) else len(A[0])

    matrixTwoIsSingle = True if isinstance(B[0], int) else False
    matrixTwoRows = 1 if isinstance(B[0], int) else len(B)
    matrixTwoCols = len(B) if isinstance(B[0], int) else len(B[0])

    resultMatrixRows = matrixOneRows
    resultMatrixCols = matrixTwoCols

    print("A.rows:",matrixOneRows,", A.columns:",matrixOneCols,
        "\nB.rows:",matrixTwoRows,", B.columns:",matrixTwoCols,
        "\nR.rows:",resultMatrixRows,", R.columns:",resultMatrixCols)

    R = []
    if matrixOneCols == matrixTwoRows:
        print("Matrix one columns equal to matrix two rows.\ni.e. A.cols = B.rows,",matrixOneCols,"=",matrixTwoRows)
        for i in range(resultMatrixRows):
            tmpArr = []
            for j in range(matrixTwoCols):
                sum = 0
                for k in range(matrixTwoRows):
                    if matrixOneIsSingle:
                        sum += A[k] * B[k][j]
                    else:
                        sum += A[i][k] * B[k][j]
                tmpArr.append(sum)
            R.append(tmpArr)
    else:
        print("Matrix one columns are not equal to matrix two rows. \ni.e. A.cols = B.rows,",matrixOneCols,"=",matrixTwoRows)

    return R