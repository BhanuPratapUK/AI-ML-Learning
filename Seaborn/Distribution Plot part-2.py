import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")
sns.displot(data = mpg ,x="cylinders" ,y="mpg")
plt.xlabel("No. of Cylinders")
plt.ylabel("Mileage")
plt.show()