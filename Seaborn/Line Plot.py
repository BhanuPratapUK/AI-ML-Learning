import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")

sns.lineplot(data= mpg , x="horsepower" , y = "acceleration")
# plt.legend(loc="upper left")
plt.show()