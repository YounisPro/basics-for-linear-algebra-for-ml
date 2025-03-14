from numpy import random
# creating random matrix of data type float
# of two rows and 3 colums
a1 = random.rand(2,3)
print(a1)

# creating int type of random one to ten numbers matrix having four rows and columns
a2 = random.randint(1,10,(4,4))
print(a2)

# creating 
a3 = random.randn(2,3)
print(a3)