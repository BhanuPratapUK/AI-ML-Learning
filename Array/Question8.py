from numpy import *

arr = logspace(1,4,5)
print(arr)

n = len(arr)


for i in range(n):
    print('%.1f'% arr[i], end='  ')
