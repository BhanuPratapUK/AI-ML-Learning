import pandas as pd
import xlrd

df = pd.read_csv("Workbook/Worksheet3.csv")
print(df)

print(" Creating the series from the Dataframe ")
df1 = pd.Series(df["name"])
df2 = pd.Series(df['age'])
print(df1)
print(df2)
df4 = df[['name','age']]## creating the series formthe dataframe
print(df4)
print("***************************************")
df3 = pd.concat([df1,df2],axis=1)## you can see both methods are same
print(df3)
print("***************************************")
df3.columns=["empname","empage"]
print(df3)
print("***************************************")
