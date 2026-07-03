import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg")

sns.jointplot(data= mpg , x="horsepower" , y = "acceleration" , hue="origin" )
# plt.legend(loc="upper left")
plt.show()