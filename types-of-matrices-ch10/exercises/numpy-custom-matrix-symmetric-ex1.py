# importing transpose method from custom functions
from custom_functions import transpose

A = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

# A = [
#     [1, 2, 3],
#     [2, 1, 2],
#     [3, 2, 1]
# ]
print(A)
print("\n")

# transposing matrix using custom method
T = transpose(A)
print(T)
print("\n")