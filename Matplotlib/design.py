import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xaxis = np.linspace(0, 5, 11)
y = xaxis ** 2

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    xaxis,
    y,
    color="pink",
    linewidth=3,
    linestyle="-",
    marker="o",
    markersize=9,
    markerfacecolor="white",
    markeredgecolor="deeppink"
)

ax.plot(xaxis, xaxis + 1, color="red", linewidth=0.8, linestyle="--")
ax.plot(xaxis, xaxis + 2, color="green", linewidth=1.2, linestyle="-.")
ax.plot(xaxis, xaxis + 3, color="blue", linewidth=1.5, linestyle=":")

# Labels
ax.set_title("Graph", fontsize=20)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y = x²", fontsize=14)

ax.grid(True, linestyle=":", alpha=0.4)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()