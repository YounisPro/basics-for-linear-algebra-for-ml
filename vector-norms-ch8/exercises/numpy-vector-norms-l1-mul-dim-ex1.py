from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# creating vector
v1 = array([
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, -115],
    [1, 2, 3, 4, 80]
])

# calculating norm l1
# but this will not sum all values as we see before for 
# the vector norm l1 instead it will return sum on all max values
# of vector see:
# l1 = |getmax(v1[0])| + |getmax(v1[1])| + |getmax(v1[2])|
# l1 = |5| + |-115| + |80|
# l1 = 200.0
l1 = norm(v1,1)
print(l1)