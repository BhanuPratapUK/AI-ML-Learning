import matplotlib.pyplot as plt
import pandas as pd
emp_ages =[10,11,12,13,14,15,16,17,18,19,22,25]
bins=[0,10,20,30]
plt.hist(emp_ages , bins , histtype="step", rwidth=0.6 , color="red")
plt.xlabel("Employee ages")
plt.ylabel("no of Employee")
plt.title("Apple Company")
plt.legend()
plt.show()