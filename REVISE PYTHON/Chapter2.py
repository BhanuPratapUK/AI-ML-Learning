# #control Statement ----> it control the flow of the set of the instructions
#  # write the program to find theperson is eligible for voting or not?

# age = int(input("Entet the age of the person--->"))
# if (age >= 18):
#     print("Yes, this Person is eligible for the Voting")

# print("*****************************************************")
# ## 2 
# x = input("Enter the input -->")
# if (x.isalpha()):
#     print("yeah it is aplha")
# if (x.isdigit()):
#     print("yeah it is digit")
# if (x.isspace()):
#     print("yeah it is space")
# 3 fin the text is vowel or not
# text = input("Enter the character -->")
# if text in "AEUIOU":
#     print("Text is in Upper Case and Vowel")
# elif text in "aeiou":
#     print("Text is in Lower case and Vowel")
# else:
#     print("It is not Vowel")

# 4 find the greatest number
# num1= int(input("Enter the First Number --->"))
# num2= int(input("Enter the second Number --->"))
# num3= int(input("Enter the Third Number --->"))
# print("****")
# if(num1> num2):
#     if(num1> num3):
#         print("Num1 is greater than num2 and num3")
#     else:
#         print("Number3 is greater than num1 and num2")
# elif (num2> num3):
#     print("Num2 is greater then num3")
# else:
#     print("Number3 is greatet than num1 and num2")

# 5 Display the day of the week
# num = int(input("Enter the Number of the week fro 0 to 7 ----->"))
# if(num==0 or num==7):
#     print("Sunday")
# elif(num==1):
#     print("Monday")
# elif(num==2):
#     print("Tuesday")
# elif(num==3):
#     print("Wednesday")
# elif(num==4):
#     print("Thursday")
# elif(num==5):
#     print("Friday")
# elif(num==6):
#     print("Saturday")
# else:
#     print("Try again! You aer putting Number")

# 6 check  the character is Uppercase or Lowercase or a Number
# ch = input("Enter the Character--->")
# if (ch >="A") and (ch<="Z"):
#     print("CH is upperCase")
# elif (ch >="a") and (ch<="z"):
#     print("CH is LowerCase")
# elif (ch >="0") and (ch<="9"):
#     print("CH is Numerical")
# else:
#     print(" You Have entered the Wrong the Value")

# # find the Roots
# a = int(input("Enter the Value of the a --->"))
# b = int(input("Enter the Value of the b --->"))
# c = int(input("Enter the Value of the c --->"))

# D=  b**2 - 4*a*c
# deno = 2*a

# if (D>0):
#     print("Real Roots")
#     roots1 = (-b + D**0.5)/deno 
#     roots2 = (-b - D**0.5)/deno
#     print("The roots are -->", roots1, "and the other one is here --->", roots2)
# elif (D==0):
#     print("Equal Roots")
#     roots1 = -b/deno
#     print("Roots are", roots1)
# else:
#     print("These are the  Imaginary Roots")

# While loop --> while povide the mechanismto repeat the one or more statement while a particular statement is true.
# 1 print nuber till 10
# i = 0
# while i <=10:
#     print(i, end=" ")
#     i+=1


# using tab \t
# i = 0
# while i <=10:
#     print(i, end="\t")
#     i+=1

# calculate sum and average of the first 10 numbers

# i = 0
# s= 0
# while (i <=10):
#     s = i + s
#     i+=1
# print("The sum of the 10 Numbers---->",s)

# avg = s/10

# print("The avg f he 10 nnumbers---->",avg)

# print 20 horizontal astrisks
# i = 0
# while (i<=20):
#     print("*", end=" ")
#     i+=1

# program to calculate the sum of numbers from M to N

# m = int(input("Enter the First Number -->"))
# n = int(input("Enter the Second Number -->"))
# s = 0
# while (m <=n):
#     s = s + m
#     m+=1
# print("The sum of numbers from M to N is --->", s)


# program to read the numbers until -1 is encountered. Also count the negative and zeroes entered by the user
# pos = neg = zeros = 0
# while True:
#     num  = int(input("Enter the Number is ---->"))
#     if (num == -1):
#         print("**************End**************")
#         break
#     elif (num>0):
#         pos +=1
#     elif (num == 0):
#         zeros+=1
#     else:
#         neg+=1
# print("The Number of positive Numbers -->", pos)
# print("The Number of negative Numbers -->", neg)
# print("The Number of Zeros Numbers -->", zeros)

# program to read the numbers until -1 is encountered. Find the average if neg and pos numbers entered by he user
# pos = 0
# neg =0
# pos_count = 0
# neg_count = 0

# while True:
#     num = int(input("Enter the number----->"))
#     if (num == -1):
#         break
#     elif(num >0 ):
#         pos_count+=1
#         pos+=num
#     else:
#         neg_count+=1
#         neg+=num
# print("Enter the pos_count-->", pos_count)
# print("Enter the pos-->", pos)
# print("Enter the neg_count-->", neg_count)
# print("Enter the neg-->", neg)


# Armstrong Number
# n = int(input("Enter the Number --->"))
# s = 0
# num = n
# while (n>0): # 153 , 15
#     r = n%10 # 3 , 5
#     s = s +(r**3)#  0+3**3 = 27
#     n = n//10 # 15
# if (s == num):
#     print("This number yuyuyu is Armstrong")
# else:
#     print("This number is not Armstrong")


# Decimal Number into binary Number
# num = int(input("Enter the Number ---->"))
# binary = 0
# i=0
# while (num>0):
#     r = num%2
#     binary = binary + r*(10**i)
#     num = num//2
#     i+=1
# print("Enter the Number ---->", binary)

# Convert binary to decimal number
# num = int(input("Enter the Number ---->"))
# deci = 0
# i =0
# while (num>0):
#     r = num%10
#     deci = deci + r * (2**i)
#     num = num//10
#     i+=1
# print("The NUmber is in decimal NUmber--->", deci)

# Program to enter a number and then calculate the sum of the digit
# sum_of_digit = 0

# num = int(input(" Enter the Number ---->"))
# while (num!=0):
#     r = num%10
#     sum_of_digit = sum_of_digit + r
#     num = num //10
# print("Here is the Sum of the digit-->", sum_of_digit)

# GCD of two numbers
# num1 = int(input("Enter the First Number  --->"))
# num2 = int(input("Enter the First Number  --->"))
# if (num1 > num2):
#     dividend = num1
#     divisor = num2
# else:
#     divisor = num1
#     dividend = num2

# while (divisor !=0):
#     r = dividend % divisor
#     dividend = divisor
#     divisor = r
# print("Here is the Answer", dividend)

# reverse the number
# num = int(input("Ebter the Number--->"))
# while (num>0):#123
#     s = num%10
#     print(s, end=" ")
#     num = num //10

# reverse the counting
# x = int(input("Enter the Number--->"))
# while (x > 0):
#     print(x, end=" ")
#     x = x-1

# ## FOR  ###

# print the number  usin ghte rnage function
# range() it is a function which is used to iterate the over the sequence of numbers


# for i in range(1,5):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# #program to calculate  the average of the  first n natural numbers using hte for loop
# n = int(input("Enter the Number ---->"))
# s =0
# for i in range(1,n+1):
#     s+=i
# avg = s/n
# print("Here is the  sum of the numbers--->",s)
# print("Here is the avg of he NUmbers --->",avg) 

# # print the  Table of multiplication of the n.
# n = int(input("Enter the Number ---->"))
# for i in range(1,11):
#     x = n*i
#     print(n,'X',i,'=' ,x )

# # program using the loop to print all the numbers from m-n thereby classifying them as even as odd
# m = int(input("Enter the Number ---->")) 
# n = int(input("Enter the Number ---->"))
# for i in range(m, n+1):
#     if i %2 ==0:
#         print(i ," this is the Even Number ")
#     else:
#         print(i ," this is the Odd Number ")

# Calculate the  factorial of the Number
# n= int(input("Enter the Number ---=>"))
# if (n==0):
#     fact =1
# fact= 1
# for i in range(1, n+1):
#     fact = fact * i
# print("Here is the factorial of the Number", fact)


# # program to classify a given number as prime or composite
# num = int(input("Enter hte Number --->"))
# x = 0
# for i in range(2, num):
#     if (num%i==0):
#         x=1
#         break
# if (x==1):
#     print("This number is Composite")
# else:
#     print("This number is Prime")

# program to calculate the total nummber of composite number and the Prime Number.
# total_prime = 0
# total_composite  = 0
# while (1):
#     num  = int(input("Enter the Number---->"))
#     if (num == -1):
#         break
#     is_composite=0
#     for i in range(2, num):
#         if (num%i==0):
#             is_composite = 1
#             break
#     if (is_composite):
#         total_composite+=1
#     else:
#         total_prime+=1
# print("here is the total composite number ---->", total_composite)
# print("here is the total prime number ---->", total_prime)

# calculate the Power
# num = int(input("Enter the Number ---->"))
# power = int(input("Enter the Power---->"))
# result = 1
# for i in range(power):
#     result = result*num

# print("Here  is the power of this--->", result)

# thatdisplays the leap year from 1900 - 2100
# for i in range(1900, 2101):
#     if (i%4==0):
#         print(i, end=" ")
