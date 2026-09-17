import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

x = np.linspace(0,5,11)
print(x)
y= x**2
print(y)

#Scatter Plot...

plt.scatter(x,y)
plt.show()

#histogram 
data = sample(range(1,1000),100)
plt.hist(data)
plt.show()

#boxplot

plt.boxplot(x)
plt.show()