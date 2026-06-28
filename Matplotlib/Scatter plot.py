import matplotlib.pyplot as plt

age= [6,8,10,12]
prices = [96,45,67,89]


plt.scatter(age, prices , color="purple")
plt.title("Haryana Prices")
plt.xlabel("Age in Years")
plt.ylabel("price in thousands")
plt.show()