import pandas as pd
import matplotlib.pyplot as plt

# sep='\s+' defines separator as being one single white space or more
df = pd.read_csv('rmsd_xtal.xvg', sep='\s+', header=None, names=['time_crystal','RMSD_crystal'])

df_2 = pd.read_csv('rmsd.xvg', sep='\s+', header=None, names=['time_equilibriated', 'RMSD_equilibriated'])


plt.plot(df[['time_crystal']], df[['RMSD_crystal']], label = "Crystal")
plt.plot(df_2[['time_equilibriated']], df_2[['RMSD_equilibriated']], label = "Equilibriated")

plt.legend(loc='lower right')  
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (nm)')
plt.title('RMSD')

plt.show()
