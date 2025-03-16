from numpy import array
# creating array
data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])
# slicing array with first and second having zero with slice to 
# empty will results same the orignal array
print(data[0:,0:])
print("\n")

# slicing array with first range to zero to one 
# and second having zero with slice to empty
print(data[0:1,0:])
print("\n")

# slicing array with first range to zero to three 
# and second having zero to one range
print(data[0:3,0:1])
print("\n")

# slicing array with first range to zero to three 
# and second having one to three
print(data[0:3,1:3])