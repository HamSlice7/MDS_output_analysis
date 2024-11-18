import pandas as pd
import matplotlib.pyplot as plt

# sep='\s+' defines separator as being one single white space or more
df = pd.read_csv('potential.xvg', sep='\s+', header=None, names=['step','energy'])


df.plot('step')

plt.show()