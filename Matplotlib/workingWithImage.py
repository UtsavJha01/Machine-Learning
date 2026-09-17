import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('virat.jpg')
plt.imshow(img)
plt.axis('off')
cropped_img = img[600:1000]
plt.imshow(cropped_img)
plt.show()