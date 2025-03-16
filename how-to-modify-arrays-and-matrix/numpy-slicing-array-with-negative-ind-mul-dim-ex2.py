from numpy import array
# creating array
data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

# creating array with only having negative one column data using slicing
arr1 = data[:,-1]
print(arr1)
print("\n")

# creating array with only having negative two column data using slicing
arr2 = data[:,-2]
print(arr2)
print("\n")

# creating array x, y with slicing data two times by comma seperated
# x will contains all data as first range of second index is empty
# and second range is size of array or even if empty will have same 
# results and first index is both sides empty means all data of array. 
# Whereas y have the first index as both sides empty means all rows
# and second index is not sliced and it contains only one column as negative one
x, y = data[:,:], data[:, -1] 
print("x: ")
print(x)
print("\ny:")
print(y)
print("\n")

# creating array x, y with slicing data two times by comma seperated
# x will contains only 2 columns from index zero to one slice and all rows
# and y will contains all rows and second index only contains from negative one
# to three 
x, y = data[:,0:2], data[:, -1:3] 
print("x: ")
print(x)
print("\ny:")
print(y)
print("\n")
