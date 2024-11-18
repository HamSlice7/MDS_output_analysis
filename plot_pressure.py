import pandas as pd
import matplotlib.pyplot as plt

# sep='\s+' defines separator as being one single white space or more
df = pd.read_csv('pressure.xvg', sep='\s+', header=None, names=['time','pressure'])


df.plot('time')

plt.show()