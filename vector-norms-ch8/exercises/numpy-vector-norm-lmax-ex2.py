from numpy import array
# importing norm from linear algebra package
from numpy.linalg import norm
# importing infinity from math library
from math import inf

# creating vector
v1 = array([
    [-100, 200, 300],
    [1, -2, 3],
    [10, 20, -30]
])

# calculating max norm
# max_norm = max([ 
#               (|v1[0][0]| + |v1[0][1]| + |v1[0][2]|),
#               (|v1[1][0]| + |v1[1][1]| + |v1[1][2]|),
#               (|v1[2][0]| + |v1[2][1]| + |v1[2][2]|)
#               ])
# max_norm = max([ 
#               (|-100| + |200| + |300|),
#               (|1| + |-2| + |3|),
#               (|10| + |20| + |-30|)
#               ])
# max_norm = max([ 600, 6, 60 ])
# max_norm = 600.0
max_norm = norm(v1, inf)
print(max_norm)