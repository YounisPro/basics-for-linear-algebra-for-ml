from numpy import array
from numpy import random
import time
# importing my custom function for broadcasting
from custom_functions import broadcasting_list

# creating size for the one dimension array ten power two value 
size_1D = 10**3
# creating size for the two dimension array
size_2D = (1000, 1000)

# creating random single dimension array
arr_rand_1D = random.rand(size_1D)
print(arr_rand_1D)
print("\n")

# creating random two dimension array
arr_rand_2D = random.rand(*size_2D)
print(arr_rand_2D)
print("\n")

# start time
start = time.time()
sum1 = arr_rand_2D + arr_rand_1D
# time taken in numpy broadcasting
numpy_broadcasting_time_taken = time.time() - start

# start time
start = time.time()
# broadcasting variable
b = 10
# creating custom broadcasting array
arr_rand_custom_1D = broadcasting_list(size_1D, size_1D,b)
sum2 = arr_rand_2D + arr_rand_custom_1D
custom_broadcasting_time_taken = time.time() - start

print(f"NumPy broadcasting time: {numpy_broadcasting_time_taken:.6f} sec")
print(f"Custom broadcasting time: {custom_broadcasting_time_taken:.6f} sec")

# NumPy broadcasting time: 0.003479 sec
# Custom broadcasting time: 0.141590 sec