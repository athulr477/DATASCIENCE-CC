import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 

x = np.linspace(10, 0, 50)
y = np.sin(x)
mp.plot(x,y, color='red',linestyle='--' , marker = "o")
mp.title("Line plot")
mp.xlabel("X-axis")
mp.ylabel("Y-axis")
mp.show()















