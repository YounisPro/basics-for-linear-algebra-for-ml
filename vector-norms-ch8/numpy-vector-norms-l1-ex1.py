from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# creating vector
v1 = array([1, 2, 3])
print(v1)
print("\n")

# calculate norm l1
# l1 = |v1[0]| + |v1[1]| + |v1[0]|
# l1 = |1| + |2| + |3|
# l1 = 6.0 
l1 = norm(v1, 1)
print(l1)