def fact(n):
    f=1
    if (n==0) or (n==1):
        return 1
    else:
        for i in range(1, n+1):
            f=f*i
        return f
n = int(input("Enter the  value ---->"))
r = int(input("Enter the other value ---->"))
result= fact(n)/fact(r)
print("Here is the Answer--->",result)
