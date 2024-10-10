import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = arr % 2 == 0
new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)