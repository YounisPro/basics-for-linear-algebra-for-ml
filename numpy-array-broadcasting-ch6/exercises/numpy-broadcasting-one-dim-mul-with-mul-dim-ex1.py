from numpy import array
# creating array
arr = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# printing array
print(arr)
print("\n")

# broadcasting array. it is required to have same number of columns
# of the array which is going to be broadcasted actual array has
# three rows and three columns and the broadcasting array has also same
# number of columns i.e. three columns. If number of columns are not
# same then it will through error at runtime
b = array([7, 7, 7])
print(b)
print("\n")

# broadcasting/multiplying b array to each row of array
result = arr * b
print(result)