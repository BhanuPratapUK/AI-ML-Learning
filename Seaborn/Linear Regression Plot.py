import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")
sns.regplot(x="horsepower", y ="acceleration" , data=mpg)
plt.show()