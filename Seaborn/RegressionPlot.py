import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
dataset = sns.load_dataset('tips')

# Display first 5 rows
print(dataset.head())

# Set plot style
sns.set_style('whitegrid')

# Basic regression plot
sns.lmplot(
    x='total_bill',
    y='tip',
    data=dataset
)

plt.show()

# Regression plot categorized by sex
sns.lmplot(
    x='total_bill',
    y='tip',
    data=dataset,
    hue='sex',
    markers=['o', 'v']
)

plt.show()