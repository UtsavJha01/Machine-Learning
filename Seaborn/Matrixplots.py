import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr_matrix = tips.corr(numeric_only=True)

plt.figure(figsize=(6,4))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

sns.clustermap(
    corr_matrix,
    cmap="coolwarm",
    annot=True
)

plt.show()