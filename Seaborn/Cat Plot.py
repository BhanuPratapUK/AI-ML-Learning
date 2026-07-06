


import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
sns.catplot(x="species" , y="sepal_length" , data =iris)
plt.show()