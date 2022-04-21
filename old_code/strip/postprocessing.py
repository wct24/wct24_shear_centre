import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\strip\abaqus.csv', header = 0, usecols = [13,14])
u.columns=["z", "stress"]

u = u.astype(np.float64)


AF=1
list_of_z_values = (np.unique(u["z"].values))



def rigid_transform_3D(z,DF):
    df2 = DF.loc[DF["z"]==z]
    Total = df2["stress"].sum()
    Number_of_nodes = df2.count(axis=0)
    Number_of_nodes = Number_of_nodes["stress"]

    return Total/Number_of_nodes

root = rigid_transform_3D(0,u)
for i in list_of_z_values:
    s = rigid_transform_3D(i,u)
    ratio = s/root
    # print(ratio)
    if ratio < 0.01:
        print(i)
        break
    else:
        pass
