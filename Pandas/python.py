import pandas as pd
import xlrd

print('*****************EXCEL********************')
## Excel File
df = pd.read_excel('Workbook/Workbook1.xlsx', "Sheet1")
print(df)

print('*************CSV************************')

## Csv File

df2 = pd.read_csv('Workbook/Worksheet1.csv')
print(df2)


print('**************DICTIONARY***********************')
## Dictionary
emp= {
    "empid":[1001,1002,1003,1004],
    "empname":["Akash", "Sunita", "Parul", "Prabha"],
    "sal":[10000,20000,30000,40000]
}
df3 = pd.DataFrame(emp)
print(df3)


print('*****************TUPLES********************')
##Tuples

emp1 = [
    (10,"Bhanu","UK"),
    (11,"anu","Germany"),
    (12,"hanu","Cannada"),
    (13,"nubha","Spain")
]

df4 = pd.DataFrame(emp1,columns=["empid", "empname", "salary"])
print(df4)
