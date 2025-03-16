from numpy import genfromtxt

# fetching data from csv
data = genfromtxt('data.csv', delimiter=',', dtype=str, skip_header=1)

# creating output and input arrays
# first array contains only string columns 
# and second array contains only ratings column
x, y = data[:,[1,2,3]], data[:,6]
# printing first array(x)
print(x)
print("\n")

# printing second array(y)
print(y)
print("\n")