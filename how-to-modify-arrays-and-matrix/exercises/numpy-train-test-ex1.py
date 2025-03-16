from numpy import genfromtxt

# fetching data from csv 
data = genfromtxt('data.csv', delimiter=',', dtype=str, skip_header=1)

# creating train and test arrays
# we are creating train data of fifteen rows
# and five rows for test
split = 15
train, test = data[:split,:], data[split:,:]
# printing train array
print(train)
print("\n")

# printing test array
print(test)