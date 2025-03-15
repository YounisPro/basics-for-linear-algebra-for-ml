from numpy import array
# creating array
data = array([
    [11, 22],
    [33, 44],
    [55, 66]
])
# fetching with negative indexing ex1
print(data[-1][0])
# fetching with negative indexing ex2
print(data[0][-2])