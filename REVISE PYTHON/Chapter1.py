# ## General Questions of the Python

# print(float(16/3))
# print(format(float(16/3),".3f"))

# ## The format() gve the Numeric string of the floating point value.It can be used to insert the comma(" , ")
# print(format(12425,","))

# ## //Floor Division and % modulous Operator
# print("This is the Floor Division--->",13//5)## it will give the Quotient
# print("This is the Modulous Operator--->",13%5)## it will give the remainder
# print('Hey Bhanu How\'s you') #Escape Sequence --> It is combination of characters that is Translated into another Character.

# # \t --> it means it will give u the space of one tab
# # \n --> it means it will give u the new lines

# print("Hey what's up \t what is goin on?")
# print("Hey Buddy \n everything is ok?")

# # left Justify
# print(format("Bhanu","<30"))
# # Right Justify
# print(format("Bhanu",">30"))
# #align Justify
# print(format("Bhanu","-^30"))

# #name = input("What is your name-->")
# #age = input("what is your age-->")
# #print(name, 'you born in 1994 so your age is this -->' , age)
# #Comments--> To Describe the flow of the code.
# #identation it means Whitespaces at the beginning of the code.
# ## == equal operator & != not equal Operator 
# ## a+=b ---> it means a = a * b

# str1 = "Good  "
# str2 = "Morning"
# str1+=str2
# print('Addition of the String ---> ',str1)


# ## Membership Operator
# a = '2'
# b = "2"
# print('Checking in Operator -->',a in b)
# print('Checking not in operator -->',a not in b)
# print("is operator --> ",a is b)


# c= (1+2)*2
# print("This is the PEMDAS in Python--->",c)
# ##PEMDAS--> ()* X / + -


# # Concatenation --> The process of combinning of two strings  eg:

# x = "Hey! How are u ? " + "5"
# y = "I am good! How are u"
# # z= x + y
# # print(z)


# # #Perform addition and Multipplication
# # str1 = "Hello "
# # print("Addition -->",str1 + '5')
# # print("Multipplication -->",str1 * 5)


# # ##Conversion
# # # text1 = input("Enter the First Number --> ")
# # # text2 = input("Enter the Second Number--> ")
# # # print("See --->",text1 + text2)

# # # part1 = int(input("Enter the First Number --> "))
# # # part2 = int(input("Enter the Second Number--> "))
# # # print("See --->",part1 * part2)

# # text1 = int(input("Enter the Number--> "))
# # print("Hex",hex(text1))
# # print("Oct-->",oct(text1))
# # print("Square root -->",(text1**0.5))

# num1 = int(input("Enter the NUmber--->"))
# amt =  float(input("Enter the Number-->"))
# pi= float(input("Enter the pi-->"))
# code =  str(input("Enter thr code --->"))
# population = int(input("Enter the population of the India --->"))
# msg = str(input("Enter the NUmber--->"))
# print(num1)
# print(amt)
# print(pi)
# print(code)
# print(population)
# print(msg)

# # Area of the triangle by using the Heron's formula
# a = float(int(input("Enter the A --->")))
# b = float(int(input("Enter the B --->")))
# c = float(int(input("Enter the C --->")))
# s = (a+b+c)/2
# area = (s*((s-a)*(s-b)*(s-c)))**0.5
# print("The area of the triangle using the Heron's Formula---->",area)

## Calculate the distance between two points
# x1  =  float(int(input("Enter the x1 --->")))
# x2  =  float(int(input("Enter the x2 --->")))
# y1  =  float(int(input("Enter the y1 --->")))
# y2  =  float(int(input("Enter the y2 --->")))

# d = ((x2-x1)**2 + (y2-y1)**2)**0.5
# # print("The distance between the two points--->",d)

# #Area of the Circle
# r =  float(int(input("Enter the radius --->")))
# result = 3.14*r**2
# circumference = 2 *3.14* r
# print("The result of the areaof the circle--->",result)
# print("The circu,ference of the circle--->",circumference)


##PRogram to print the digit at one place of the Number
# num = int(input("Enter the Number--->"))
# result = num %10
# print("The result is -->",result)

# Converting the Floating Number into the Integer Point
num = float(input("Enter the Number --->"))
print("The Number is " +str(num) + ("--->")+ str(int(num)))

num2 =int(input("Enter the Number --->"))
print("The Number is " +str(num2) + ("--->")+ str(float(num2)))