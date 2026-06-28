import pandas as pd

# Here is the Data 

climate = [("Delhi", 33,8),
           ("Delhi", 23,5),
           ("Pune", 43,6),
           ("Pune", 53,10),
           ("Haryana", 36,12),
           ("Haryana", 37,19),
           ]
df = pd.DataFrame(climate, columns=["city", "Temp", "Wind"],)## giving the Columns Name
print(df)


#Question1 Applying groupby
print("Question1")
df1  = df.groupby("city")
print(df1) ## it will show the address try for loop

for x, y in df1:## x = is the city and the y will be the City temp and wind 
    print("----",x, "----")
    print(y)

print("Question2")
df2 = df1.get_group("Delhi")## it will give the group of the city 
print(df2)

print("Question3")
df3 = df1.get_group("Haryana").max() # it will return the max of that particular city
print(df3)

print("Question4")
df4 = df1.max()##  it will return the each city max temp and wind
print(df4)


## Aggregate Function  by using this we can get in return max, min, return, mean, describe, count 
print("Qustion5")
df5 = df1.agg('mean')
print(df5)

df6 = df1.agg(['max','min','mean','count', 'describe']) ## all aggregate functions appliedd by using this method
print(df6)

