import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12], dtype = "S")
newarr = arr.reshape(4,3)

print(arr)
print(type(arr))
print(arr[0])
print(arr[1:5])
print(arr.dtype)
print(newarr)