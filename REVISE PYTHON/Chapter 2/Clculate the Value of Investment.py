initia_val = int(input("Enter the Number--->"))
Years = int(input("Enter the Years--->"))
Interest = int(input("Enter the Number--->"))

future = initia_val
for i in range(1,Years +1):
    future = future *((100 + Interest)/100)
    print(i , "Gives ---> %.2f " % future)


print("%.2f"% 23.4233)