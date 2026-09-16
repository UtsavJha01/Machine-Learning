import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
my_dict = {
    "Utsav":10,
    "Minakshi":20,
    "Virat":30
}
#Creating Series with using List:
print("Creating series with the help of list:")
#With default Indexing(start with 0,1,2....):
print("With default Indexing: ")
print(pd.Series(my_list))
#with index what we decleared in Labels:
print("With index what we decleared in Labels:")
print(pd.Series(my_list,index=labels))

#Creating series with the help of Numpy Array (1-D):   If we try to create the series using 2-D array it will show error due to the series is 1D array.
print("Creating series with the help of Numpy Array (1-D):")
#With default Indexing(start with 0,1,2....):
print("With default Indexing: ")
print(pd.Series(arr))
#with index what we decleared in Labels:
print("With index what we decleared in Labels:")
print(pd.Series(arr,index=labels))

print("Creating series with the help of Dictionary:")
print(pd.Series(my_dict)) #in dictionary it has default indexing which is Key in Dictionary