import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os
# be careful to make sure that the csv matches to the index
os.chdir(r"E:\temp\I")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\I\stress.csv', header = 0, usecols = [3, 12,13,14,25])
u.columns=["Part Instance", "x", "y", "z","S33" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)

def plot_nodes(z,DF):
    df2 = DF.loc[DF["z"]==z]

    df2['area'] = 1/df2['S33']
   
    area = np.sum(df2["area"].values)
    return area


area = plot_nodes(1.0,u)


