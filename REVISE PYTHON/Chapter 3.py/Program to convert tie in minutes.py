def conversion(hrs, minu):
    a = hrs*60
    b = minu
    n = a + b
    return n

hrs = int(input("Enter thr Hours ---->"))
minu = int(input("Enter thr min ---->"))

print("Here's is the total number of the minutes -->;", conversion(hrs, minu))