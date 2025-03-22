from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# creating vector
v1 = array([
    [1, 2, 3],
    [-4, 5, -5]
])
print(v1)
print("\n")

# calculating norm l1
# to do sum of all values we have to use flating method
# called array.flatten to achieve ordinary l1 norm
# li = |v1[0][0]| + |v1[0][1]| + |v1[0][2]| + |v1[1][0]| + |v1[1][1]| + |v1[1][2]|
# li = |1| + |2| + |3| + |-4| + |5| + |-5|
# li = 20.0
l1 = norm(v1.flatten(),1)
print(l1)