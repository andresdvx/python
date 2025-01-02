import numpy as np
import pandas as pd
from numpy.random import randn

print(randn(5,4))

df = pd.DataFrame(randn(5,4), ['A','B','C','D', 'E'], ['W','X','Y','Z']) # crear un data frame

print(df)

print("-----------------------")


print(df.W)