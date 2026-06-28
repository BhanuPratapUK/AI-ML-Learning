import pandas as pd
import xlrd

print('*****************CSV********************')
## Excel File
df = pd.read_csv('Workbook/Worksheet2.csv')
print(df)

print("************************")

df1 = df.sort_values("emp")
print('To sort the data according to the Alphabet--->',df1)

print("************************")

## ********* Handling Missing Values *************

print("************ fillna() *********")
df2 =df.fillna(0)
print(df2)

print("***************fillna() method use to fill the details ***********************")
df3 = df.fillna({'name':'Shubhash', "country": "Dubai"})
print(df3)

print("********************  dropna() to remove all the Blank rows from the data  ***************")
df4 = df.dropna()
print(df4)