from numpy import array
# creating array
arr = array([
    [3, 6, 9, 12],
    [15, 18, 21, 24],
    [27, 30, 33, 36]
])
# printing array
print(arr)
print("\n")

# broadcasting array. it is required to have same number of columns
# of the array which is going to be broadcasted actual array has
# three rows and four columns and the broadcasting array has also same
# number of columns i.e. four columns. If number of columns are not
# same then it will through error at runtime
b = array([1, 2, 3, 4])
print(b)
print("\n")

# broadcasting/subtracting b array to each row of array
# we can broadcast vice versa to like:
# result = b - arr 
result = arr - b
print(result)