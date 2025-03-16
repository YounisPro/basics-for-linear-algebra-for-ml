from numpy import array
# creating array
data = array([
    [5, 10, 15],
    [6, 12, 18],
    [7, 14, 21],
    [8, 16, 24]
])

# here we will keep two records for training 
# and two record
split = 2
train, test = data[:split,:],data[split:,:]
print(train)
print("\n")

print(test)