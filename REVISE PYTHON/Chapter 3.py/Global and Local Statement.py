var = "good"
def show():
    var1=  "Morning"
    print("This will come --->", var)
    print("This will come --->", var1)
show()
print("This will come --->", var)


"Using the  global variable"

text = "Bhanu"
def shine():
    global text1
    text1=  "Pratap"
    print("This will be the Answer",text)
    print("This will be the Answer",text1)
shine()
print("This will be the Answer",text1)