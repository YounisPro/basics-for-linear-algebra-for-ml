from numpy import array
# imporitng matrix_rank method from linear algebra package to check matrix ranking
from custom_functions import matrix_rank

# creating matrix for rank 0
MO = array([
    [0, 0],
    [0, 0]
])
print(MO)
mrO = matrix_rank(MO)
# explaination: it has rank zero due to it has zeros in all rows
print("rank:", mrO,"\n")

# creating matrix for rank 1
M1 = array([
    [1, 2],
    [1, 2]
])
print(M1)
mr1 = matrix_rank(M1)
# explaination: it has rank one due to it has identical rows
print("rank:",mr1,"\n")

# creating matrix for rank 2
M2 = array([
    [1, 2],
    [3, 4],
    [2, 4]
])
print(M2)
mr2 = matrix_rank(M2)
print("rank:",mr2,"\n")
# explaination: it has rank two due to it has not the double, same, or any zeros rows
# print("rank:",mr2)