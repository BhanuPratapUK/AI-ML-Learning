import matplotlib.pyplot as plt

slices = [30,40,20,10]
depts= ["Sales","Managers","Drivers","Admin"]
cols= ["green", "red", "purple", "orange"]

plt.pie(slices,labels=depts , colors=cols , startangle=90 , explode=(0, 0.2,0,0), shadow=True , autopct="%.1f%%")
plt.title("Mitie Company")
plt.legend()
plt.show()