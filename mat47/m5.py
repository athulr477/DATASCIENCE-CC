import matplotlib.pyplot as mp
import seaborn as sb
import numpy as np 
import pandas as pd 




days = [1, 2, 3, 4, 5]
sleeping = [7, 6, 5, 8, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
mp.stackplot(days, sleeping, eating, working, playing, labels=['Sleeping', 'Eating', 'Working', 'Playing'])
mp.legend(loc='upper left')
mp.title("Stacked Area Plot")
mp.show()