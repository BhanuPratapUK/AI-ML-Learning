from numpy import *
a = array([1,2,3,4,5])
b = array(a)
c = a

print('This is the Original array',a,' its id is --->',id(a))
print('This is the array making new array',b,' its id is --->',id(b)) # because over here I am using array() function.
print('This is the copy of Original array',a,' its id is --->',id(c)) # Over here I am making of the original array do that is why the id will come same always.
