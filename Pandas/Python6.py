import pandas as pd
import numpy as np

print("********* Creating the series from the Numpy **********")

arr = np.array([11,12,13,14,15,16,17,18,19,20])
arr1 = pd.Series(arr)
print(arr1)

print("********* Converting series into Numpy **********")
arr2 = arr1.values
print(arr2)


print("********* Creating series from the Dictionary **********")

my_dict = {
    'name':['a','b','c','d','e'],
    'country':['India','UK','Spain','NewZealand','Italy'],
    'height':[122,145,167,178,189]
}

df = pd.Series(my_dict)
print(df)



print("********* Accessing Elements fromt the Series **********")
df1 = df['name']
print(df1)
df1 = df['name'][2]
print('Accessing th eelements from the serries [name][2]-->',df1)