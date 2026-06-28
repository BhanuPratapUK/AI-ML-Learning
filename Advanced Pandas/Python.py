import pandas as pd

# df = pd.DataFrame({"Player Name":["Abhishek","Rahul Dravid", "Sachin Tendulkar"],
#                    "Age":[23,34,44]
                   
#                    })
# print(df)

# print("**********************************")

# df1 = pd.DataFrame({"Player Name":["Abhishek","Rahul Dravid","Akash"],
#                    "Salary":[12,13,15] 
#                     })
# print(df1)

# print("***************INNER*******************")

# df2  = pd.merge(df,df1,on="Player Name" , how="inner")
# print(df2)

# print("***************LEFT*********************")

# df3  = pd.merge(df,df1,on="Player Name" , how="left")
# print(df3)

# print("**************RIGHT********************")

# df4  = pd.merge(df,df1,on="Player Name" , how="right")
# print(df4)

# print("***************OUTER*******************")

# df5  = pd.merge(df,df1,on="Player Name" , how="outer")
# print(df5)


# print("**************************When there is no Common Column *********************************************")

# df6= pd.DataFrame({"Player Name":["Abhishek","Rahul Dravid", "Sachin Tendulkar"],
#                    "Age":[23,34,44]
                   
#                    })
# print(df6)

# print("**********************************")

# df7 = pd.DataFrame({"Sports Person":["Abhishek","Rahul Dravid","Akash"],
#                    "Salary":[12,13,15] 
#                     })
# print(df7)

# print("**********************************")
# df8  = pd.merge(df6,df7,left_on="Player Name", right_on="Sports Person" , how="outer")
# print(df8)


# print("**************** Concatenation of the Tables ******************")
# df9  = pd.concat([df6,df7])
# print(df9)
 

# print("**************** Ignore the Index ******************")

# df10  = pd.concat([df6,df7], ignore_index=True)## to ignore the index
# print(df10)

# df11 = pd.concat([df6,df7],axis=1)# to add the row side by side
# print(df11)


