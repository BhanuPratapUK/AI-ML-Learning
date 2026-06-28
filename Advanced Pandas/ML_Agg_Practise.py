import pandas as pd
import xlrd


import os

ml = pd.read_csv("Advanced Pandas/WorkBook/AdvancedSheet1.csv")

df = ml[ml.age== 12]
df1 = ml[ml.age== 12].name
df2 = ml[ml.age== 12][["name", "weight" , "country"]]
df3 = ml[(ml.age==13) & (ml.salary ==23)]
df4 = ml[(ml.age==13) & (ml.salary == 23)][["name", "age", "salary"]]
df5 = len(ml) # length of the data
df6 = ml.shape # give u the rows and the columns
df7 = ml["salary"].unique() # remove the duplicate number 
df8 = ml[ml.gender == "M"].sort_values("weight", ascending=False)
df9 = ml.groupby(["gender", "age"]).size()
df10 = ml.groupby(["gender", "age"]).size().to_frame("Counting")
df11 = ml.groupby(["gender", "age"]).size().to_frame("Counting").reset_index()
df11 = ml.groupby(["gender", "age", "weight"]).size().to_frame("Counting").reset_index().sort_values("weight",ascending=False )
print(df11)

