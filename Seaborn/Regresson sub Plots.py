import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.scatterplot(x="horsepower",y="acceleration",data=mpg)
plt.subplot(2,2,2)
sns.scatterplot(x="horsepower",y="acceleration",data=mpg)
plt.subplot(2,2,3)
sns.boxplot(x="origin",y="acceleration",data=mpg)
plt.show()
