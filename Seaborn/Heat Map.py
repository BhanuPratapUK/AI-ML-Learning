import matplotlib.pyplot as plt
import seaborn as sns

iris  = sns.load_dataset("iris")
iris1 = iris.iloc[:10, 0:4]
sns.heatmap(iris1 ,cmap="BrBG",  annot=True)
plt.show()