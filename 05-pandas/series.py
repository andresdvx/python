import pandas as pd
import numpy as np


labels  = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)

d = {'a' : 10, 'b': 20, 'c': 30}

series = pd.Series(my_data, labels)

print(series["b"])


ser1 = pd.Series(data=[2,4,6], index=["a","b","c"])

ser2 = pd.Series(data=[4,8,10], index=["a","b","c"])

print(ser1 + ser2) # sumar series