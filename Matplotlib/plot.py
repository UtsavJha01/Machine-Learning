import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
print(x)
y= x**2
print(y)

plt.plot(x,y)
plt.title("Virat")
plt.xlabel("Matches")
plt.ylabel("Century")
plt.show()
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,4)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(x**2,x**2)
plt.subplot(2,2,3)
plt.plot(y,x)
plt.show()