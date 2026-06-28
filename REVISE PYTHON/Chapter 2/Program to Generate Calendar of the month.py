start_day = int(input("Enter the Start Day of teh month------>"))
num_of_days= int(input("Number of the days------>"))

print("Sun Mon Tues Wed Thurs Fri Sat")
for i in range(start_day-1):
    print(end="    ")
i = start_day -1
for j in range(1, num_of_days+1):
    print(str(j)+"  ", end=" ")
    i+=1
    if ( i >6):
        print()
        i =1
        
