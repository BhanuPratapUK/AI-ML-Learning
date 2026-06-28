import math

while(1):
    num = int(input("Enter the Number ---->"))
    if (num == 999):
        break
    elif num < 0:
        print("Square root of negative numbers can not be done ")
        continue
    else:
        print("This is the Answer u  are looking for --->", math.sqrt(num))