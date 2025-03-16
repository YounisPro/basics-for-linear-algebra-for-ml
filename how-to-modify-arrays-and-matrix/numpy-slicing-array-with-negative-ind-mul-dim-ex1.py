from numpy import array
# creating array
data = array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])
# slicing array with first index range negative three to empty
print(data[-3:])
print("\n")

# slicing array with first index range negative three to three
print(data[-3:3])
print("\n")

# slicing array with first index range negative three to three 
# and second index range negative three
print(data[-3:3,-3:])
print("\n")

# slicing array with first index range negative three to three
# and second index range to negative two to two
print(data[-3:3,-2:2])
print("\n")

# slicing array with first index range negative three to three
# and second index range to negative two to three
print(data[-3:3,-2:3])