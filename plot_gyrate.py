import pandas as pd
import matplotlib.pyplot as plt

# sep='\s+' defines separator as being one single white space or more
df = pd.read_csv('gyrate.xvg', sep='\s+', header=None, names=['time','Rg', 'Rg/sX/N', 'Rg/sY/N', 'Rg/sZ/N'])

plt.plot(df[['time']], df[['Rg']])

plt.show()