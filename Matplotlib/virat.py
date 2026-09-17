import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

formats = ["Test", "ODI", "T20I"]
matches = [123, 314, 125]
centuries = [30, 54, 1]

x = np.arange(len(formats))
width = 0.35

plt.figure(figsize=(9, 5))

plt.bar(x - width/2, matches, width, label="Matches")
plt.bar(x + width/2, centuries, width, label="Centuries")

plt.xticks(x, formats)

plt.title("Virat Kohli - International Career")
plt.xlabel("Format")
plt.ylabel("Count")
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.show()