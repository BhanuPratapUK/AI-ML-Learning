import matplotlib.pyplot as plt
import pandas as pd
x = [1001,1003,1006,1007]
y = [1000, 2000, 3000,4000]

x1 =[1002,1004,1005,1008]
y1 =[1100,2100,3100,4100]
plt.bar(x, y, label="sales dept" ,  color="green")
plt.bar(x1,y1, label="production dept", color="purple")
plt.xlabel("id")
plt.ylabel("salary")
plt.title("Apple Company")
plt.legend()
plt.show()