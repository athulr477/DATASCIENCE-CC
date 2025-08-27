import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 



data = np.random.normal(100,200,100)
mp.boxplot(data)
mp.title("Box Plot")
mp.show()
