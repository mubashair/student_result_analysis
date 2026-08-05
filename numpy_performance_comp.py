import numpy as np
import time

#python list operation
py_list = list(range(1_000_000))
py_result = []
start_time = time.time()
for i in py_list:
    py_result.append(i+5)
end_time = time.time()
print("Python list time :", end_time -start_time)
#Numpy array operation
np_arr = np.arange(1_000_000)
start_time = time.time()
np_result = np_arr + 5 #Vectorized operation
end_time = time.time()
print("Numpy array time", end_time-start_time)