import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
print(df)
df.head()

#displot/histplot
'''A Dist Plot displays the distribution of a single variable using a histogram.

Shows how values are distributed.
Helps identify common value ranges.
Useful for understanding data spread.'''

sns.set_style("whitegrid")
sns.displot(df['total_bill'],
             kde=False,
             color='red',
             bins=30)

plt.show()
# Dis Plot with KDE
"""Displays the probability density of the data.
Provides a smoother representation than a histogram.
Helps identify peaks and patterns in the distribution."""

sns.displot(df['total_bill'],
             kde=True,
             color='blue')

plt.show()

#Joint Plot
"""Examines relationships between variables.
Displays both univariate and bivariate distributions.
Helps identify trends and correlations."""
sns.jointplot(
    x='total_bill',
    y='tip',
    data=df,
    kind='reg'
)

plt.show()
#Pair Plot
'''A Pair Plot creates scatter plots for every pair of numerical variables.

Shows relationships between multiple variables.
Displays distributions along the diagonal.
Useful for exploratory data analysis.'''

sns.pairplot(df,hue='size',palette='rainbow')
plt.show()

'''Rug Plot:
A Rug Plot displays each observation as a small mark on an axis.

Shows the exact location of data points.
Helps understand data density.
Often used together with KDE plots.'''

sns.rugplot(df['total_bill'])
plt.show()