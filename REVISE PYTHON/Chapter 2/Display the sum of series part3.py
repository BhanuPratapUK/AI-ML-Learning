n = int(input("Enter the Number ---->"))
s = 0
for i  in range(1,n+1):
    a = i/(i+1)
    s=  s + a
print("The Sum of the Series ----->", s)
