from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# printing array data with slicing with no indices will remain all data
print(data[:])
# printing array data with slicing with indices zero to two will print two values from array given the range
print(data[0:2])