from numpy import array
# importing linear algebra libary from numpy
from numpy.linalg import inv

# creating orthogonal matrix
Q = array([
[1, 0],
[0, -1]])
print(Q)
print("\n")

# inverse equivalence
V = inv(Q)
print(Q.T)
print("\n")

print(V)
print("\n")

# identity equivalence
I = Q.dot(Q.T)
print(I)