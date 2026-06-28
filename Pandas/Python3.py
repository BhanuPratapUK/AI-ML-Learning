import pandas as pd
import xlrd


df = pd.read_csv("Workbook/Worksheet1.csv")
print("This will be the original data of the file--> ",df) ### to get ALL THE DATA frothe excel file.

print("*******************************")

" Performing the Queries on Data "

"1"
print(df[df.emp>103])

print("*******************************")
"2"
print(df[df.emp == df.emp.max()])

print("*******************************")
"3"
print(df[["name","country" , "emp"]][df.emp>102])

print("*******************************")
"4"
"To get the information about the all index"
print(df.index)

print("***********")
"5"
df1 = df.set_index("name", inplace=True)## the Column with the Unique values set as a index Column
print(df)
df2 = df.loc["Bhanu"]
print(df2) 
df3 = df.reset_index(inplace=True)
print("Now Reset the data ---> ",df)
print("***********")





