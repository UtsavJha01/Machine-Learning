import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)
y= x**3
print(y)

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.savefig("save plot")
plt.show()