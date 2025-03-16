from numpy import genfromtxt

# Define the dtype for structured array
# i4 means int four bytes, U20 means unicode with twenty characters

#dtype = [
#    ('Store_ID', 'i4'), 
#    ('Store_Name', 'U20'),
#    ('Product_ID', 'i4'), 
#    ('Product_Name', 'U20'),
#    ('Day', 'i4'), 
#    ('Sales', 'i4'), 
#    ('Revenue', 'i4')
#]

# fetching data from csv
data = genfromtxt('data.csv', delimiter=',', dtype=str, skip_header=1)
# printing data
print(data)
# printing data shape
print(data.shape)
print("\n")

# printing second product index one row
print(data[1,])
print("\n")

# printing second product index one column zero
print(data[1,1])
print("\n")

# printing negative one index's row
print(data[-1,])
print("\n")

# printing only string names using slicing
print(data[:,[1,2,3]].astype(str))
print("\n")

# printing only integer using slicing
print(data[:,[0,4,5,6]])
print("\n")

# printing only integer using slicing
print(data[:,[0,4,5,6]])
print("\n")