from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm

# creating vector
v1 = array([
    [-2, 2],
    [2, -2]
])
print(v1)
print("\n")

# calculating norm l2
# l2 = √( (|v1[0][0]|)^2 + (|v1[0][1]|)^2 + (|v1[1][0]|)^2 + (|v1[1][1]|)^2 )
# l2 = √( (|-2|)^2 + (|2|)^2 + (|2|)^2 + (|-2|)^2 )
# l2 = √( 2^2 + 2^2 + 2^2 + 2^2 )
# l2 = √(16)
# l2 = 4.0 
l2 = norm(v1)
print(l2)