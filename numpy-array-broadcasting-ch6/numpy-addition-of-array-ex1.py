from numpy import array
# creating data set
a = [1, 2, 3]
b = [1, 2, 3]
# this will not working and instead it will output
# [1, 2, 3, 1, 2, 3]
c = a + b
# output: [1, 2, 3, 1, 2, 3]
print(c)
print("\n")

# creating arrays of above datasets
arr1 = array(a)
arr2 = array(b)
# adding two arrays 
sum = arr1 + arr2
# output
print(sum)