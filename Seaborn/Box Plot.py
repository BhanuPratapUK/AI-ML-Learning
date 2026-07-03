import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")
sns.boxplot(data = mpg , x="origin" , y="acceleration")
plt.show() 