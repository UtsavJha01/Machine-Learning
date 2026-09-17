import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips.head()

#Strip Plot

sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()
#Count Plot
sns.countplot(x="smoker", data=tips,hue='sex')
plt.show()
#Bar Plot
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
# Violin Plot
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
# Box Plot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()