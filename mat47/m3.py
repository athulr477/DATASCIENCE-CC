import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 



x = np.random.randn(100)
y = np.random.randn(100)
mp.scatter(x, y, color='blue', marker='x')
mp.title("Scatter plot")
mp.show()