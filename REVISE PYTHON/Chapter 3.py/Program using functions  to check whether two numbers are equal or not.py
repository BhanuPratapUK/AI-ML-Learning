def check(a,b):
    if (a==b):
        return 0
    else:
        return -1
a = int(input("Enter the First Number----> "))
b = int(input("Enter the Second Number----> "))
result = check(a,b)
if result == 0:
    print("Both Numbers are Equal")
else:
    print("Numbers are not Equal Try again")