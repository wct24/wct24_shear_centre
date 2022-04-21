import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os
# be careful to make sure that the csv matches to the index
os.chdir(r"E:\temp\box")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r"E:\temp\box\analysis.csv", header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)


def rigid_transform_3D(z,DF):
    df2 = DF[DF["z"]==z]
    z_1 = df2["U3"].values*1000
    num_z = z_1.size
    mag_z = np.linalg.norm(z_1)
    return mag_z/num_z

print(rigid_transform_3D(3.0,u))


