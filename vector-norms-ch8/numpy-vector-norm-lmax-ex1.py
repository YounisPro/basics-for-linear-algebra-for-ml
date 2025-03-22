from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# importing infinity from math library
from math import inf

# creating vector
v1 = array([-100, 20, 30, 40, -50])
print(v1)
print("\n")

# max norm
# max_norm = max(v1)
# max_norm = 50
max_norm = norm(v1, inf)
print(max_norm)