from numpy import *
arr = array([[13,15,17,19], 
               [1,2,3,4]])

print(arr)
print(len(arr))
print(type(arr))
print("The ndim tell the dimensions of the array---> ",arr.ndim)
print("The shape attribute in  the row nd the column -->",arr.shape)
print("It tells the total number of elements ii the array--> ",arr.size)
print('It tells the memory size of the array elements in bytes--->', arr.itemsize)
print('It tells the datatype of the elements in the array--->',arr.dtype)
print("It tells the total of the bytes occupied by the array--->",arr.nbytes)