import pandas as pd

print("************* WHERE **************")
student = {"Name":["Bhanu", "Rachel", "White", "Stephanie"],
           "Roll No":[14,15,16,17],
           "Salary":[45000,56900,12000,34000],
           "Test1":[15,45,60,76],
           "Test2":[45,56,78,80],
           "Test3":[89,90,45,40]
           }

df = pd.DataFrame(student) ## Convert in DataFrame
print(df)
df = df.set_index("Name")## set column as ID
print(df)


#Question1
df1 = df.where(df<60, "Here")
print(df1)

#Question2
df2 = df.where(df>=60,"Here")
print(df2)

#Question3
df3 = df.where(df["Test1"]<60, "Here")
print(df3)

#Question4
df4 = df.where(lambda x : x+5 < 80 , "Excellent")
print(df4)
