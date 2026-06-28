
import pandas as pd
import xlrd


df = pd.read_excel("Workbook/Workbook1.xlsx", "Sheet1")
print(df) ### to get ALL THE DATA frothe excel file.

df1 = df.loc[:,["emp"]] ## to view all rows based on the columns.
print(df1)

df2 = df.loc[0:0, ["name"]]
print(df2)

df3 = df.iloc[0:2 , [0,2]] ## iloc is another function to view data on the based of index
print(df3)

df4 = df.iloc[0:1, :]
print(df4)

print("***********************")
df5 = df.iloc[:, :]
print(df5)

print("*****************************************")
df6= df.loc[5:0:-1, :]
print(df6)

print("**************************")
df7 =  df.iloc[5::-1, :]
print(df7)

print("***********")
df8 =  df.iloc[-1]        ## to get the last row
print(df8)

print("***********")
df9 = df.loc[:,'country'] ## to get the last column from loc
print(df9)

print("***********")
df10 =  df.iloc[:,-1]     ## to get the last column from iloc
print(df10)


print("***********")

