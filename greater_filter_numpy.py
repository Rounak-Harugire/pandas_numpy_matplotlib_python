import numpy as np
arr = np.array([1, 2, 3, 4])
filter_arr = arr > 2
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)