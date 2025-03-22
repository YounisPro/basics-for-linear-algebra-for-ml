from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# creating vector
v1 = array([-5,5,-5,5])
print(v1)
print("\n")

# calculate norm l1
# l1 = |v1[0]| + |v1[1]| + |v1[2]| + |v1[3]|
# l1 = |-5| + |5| + |-5| + |5|
# l1 = 20
l1 = norm(v1,1)
print(l1)