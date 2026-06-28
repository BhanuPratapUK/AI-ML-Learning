prime_count= 0
comp_count= 0
n = int(input("Enter the Number --->"))
while (n !=-1):
    flag=0
    for i in range(2, n):
        if (n % i ==0):
            flag = 1
            break
    if (flag ==0):
        prime_count+=1
    else:
        comp_count+=1
    n = int(input("Enter the Number --->"))
print("Total NUmber of the Prime---> ", prime_count)
print("Total NUmber of the Prime---> ", comp_count)