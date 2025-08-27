import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 





# --bar plot

data = pd.DataFrame({
    'categories': ['A', 'B', 'C', 'D'],
    'values': [4, 7, 2, 9]
})

sb.barplot(x='categories', y='values', data=data)
mp.title("NORMAL BAR CHART")
mp.show()