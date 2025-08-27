
import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 







df = sb.load_dataset('tips')
sb.histplot(df["total_bill"],bins=20,kde=True,color='skyblue')
mp.title("Histogram")
mp.show()