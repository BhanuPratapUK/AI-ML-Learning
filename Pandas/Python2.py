import pandas as pd
import xlrd


df = pd.read_csv("Workbook/Worksheet1.csv")
print("This will be the original data of the file--> ",df) ### to get ALL THE DATA frothe excel file.



print("***********************")

print("To the know the number of rows and the columns in csv file -->",df.shape)
r,c  = df.shape
print("The nnumber of the rows --->",r)
print("The number of the columns--->",c)

print("***********************")


print("The Method to give the first 5 rows",df.head())
print("The Method to give the last 5 rows",df.tail())
print("The Method to give the rows by passing the parameter in the head     -->",df.head(2))
print("The Method to give the rows by passing the parameter in the tail from the last     -->",df.tail(2))


print("*************************")

print("The number of the rows ----> ", df[2:4])
print("The number of the rows ----> ", df[0::2])
print("The number of the rows ----> ", df[5:0:-1])### won't get the last one
print("The number of the rows ----> ", df[5::-1])### will get the last one index

print("*************************")
print("To retrive all the columns Name ---->",df.columns)


print("*************************")

print("To retrive the specific Column from the data --->",df.emp)
print("To retrive the specific Column from the data --->",df.name)

print("*************************")

print("To retrive the multiple column fromt the data ---->", df[["emp", "country"]])

print("*****************************")

print("To retrive the highest integer from the csv file", df["emp"].max())
print("To retrive the lowest integer from the csv file", df["emp"].min())

print("**********************")

print("To Display the very Important information of the data like the number of " \
"values, mean,sandard deviation--->", df.describe())
