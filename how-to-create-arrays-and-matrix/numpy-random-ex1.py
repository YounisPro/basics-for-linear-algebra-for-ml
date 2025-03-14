from numpy import random
# Creating random uniform distribution matrix of data type float
# of two rows and three columns
a1 = random.rand(2,3)
print(a1)
# printing shape of array
print(a1.shape)
# printing dtype of array
print(a1.dtype)
print("\n")

# Creating int type of random one to ten numbers matrix 
# having four rows and columns
a2 = random.randint(1,10,(4,4))
print(a2)
# printing shape of array
print(a2.shape)
# printing dtype of array
print(a2.dtype)
print("\n")

# Creating random normal distribution matrix of data type float
# of two rows and three columns
a3 = random.randn(2,3)
print(a3)
# printing shape of array
print(a3.shape)
# printing dtype of array
print(a3.dtype)
print("\n")