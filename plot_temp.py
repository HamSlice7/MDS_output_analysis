import pandas as pd
import matplotlib.pyplot as plt

# sep='\s+' defines separator as being one single white space or more
df = pd.read_csv('temperature.xvg', sep='\s+', header=None, names=['time','temperature'])


df.plot('time')

plt.show()