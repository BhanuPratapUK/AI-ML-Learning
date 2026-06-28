n = int(input("Enter the Number ---->"))
s = 0
for i  in range(1,n+1):
    if (i %2 ==0):
        a = i ** 2
        s +=a
print("The Sum of the Cubes ----->", s)
