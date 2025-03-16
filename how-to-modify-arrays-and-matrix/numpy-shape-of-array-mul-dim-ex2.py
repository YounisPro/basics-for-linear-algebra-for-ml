from numpy import array
# list of data
data = [
    [11, 22],
    [33, 44],
    [55, 66]
]

# creating array using data object
arr1 = array(data)
print('Rows %d ' % arr1.shape[0])
print('Columns %d ' % arr1.shape[1])