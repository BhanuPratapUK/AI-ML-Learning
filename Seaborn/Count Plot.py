import matplotlib.pyplot as plt
import seaborn as sns

mpg  = sns.load_dataset("mpg")
sns.countplot(x="cylinders" ,  data =mpg , hue="origin")

plt.xlabel("No of cylinders")
plt.ylabel("No of cars")
plt.legend(loc="lower left")
plt.show()