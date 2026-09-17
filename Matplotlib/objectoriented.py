import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)
y= x**2
print(y)

fig = plt.figure(dpi=100)
axis1=fig.add_axes([0.1,0.1,1,1])
axis1.plot(x,y)
axis2=fig.add_axes([0.3,0.4,0.3,0.3])
axis2.plot(x,y)
plt.show()