import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 





sizes = [20,30,25,25]
labels = ['A', 'B', 'C', 'D']
mp.pie(sizes, labels=labels, colors=["yellow","orange","green","blue"], autopct='%1.1f%%', startangle=90)
mp.title("Pie Chart")
mp.show()