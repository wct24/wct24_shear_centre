import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import subprocess, sys
import os

os.chdir(r"E:\temp\NACA0025")
file = open("loading_z.txt", "r")
loading_z_str = file.read()
loading_position = int(float(loading_z_str))
file.close()
os.remove("loading_z.txt")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\NACA0025\analysis.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)


AF=1
list_of_z_values = np.flip(np.unique(u["z"].values))


def rigid_transform_3D(z,DF):
    df2 = DF.loc[DF["z"]==z]

    x_0 = df2["x"].values
    y_0 = df2["y"].values
    z_0 = df2["z"].values
    x_1 = x_0 + df2["U1"].values*AF
    y_1 = y_0 + df2["U2"].values*AF
    z_1 = z_0 + df2["U3"].values*AF
    A = np.vstack([x_1,y_1,z_1])
    B = np.vstack([x_0,y_0,z_0])

    assert A.shape == B.shape

    num_rows, num_cols = A.shape
    if num_rows != 3:
        raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")

    num_rows, num_cols = B.shape
    if num_rows != 3:
        raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

    # find mean column wise
    centroid_A = np.mean(A, axis=1)
    centroid_B = np.mean(B, axis=1)

    # ensure centroids are 3x1
    centroid_A = centroid_A.reshape(-1, 1)
    centroid_B = centroid_B.reshape(-1, 1)

    # subtract mean
    Am = A - centroid_A
    Bm = B - centroid_B

    H = Am @ np.transpose(Bm)

    # find rotation
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T


    t = -R @ centroid_A + centroid_B
    XYZ_2  = R @ A + t


    x_2 = XYZ_2[0]
    y_2 = XYZ_2[1]
    z_2 = XYZ_2[2]

    plt.scatter(x_0, y_0)
    plt.scatter(x_2, y_2)
    plt.gca().set_aspect('equal', adjustable='box')

    ang = eul.mat2euler(R, axes='sxyz')
    e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
    rotation = ang[2]
    return rotation

end_rotation = rigid_transform_3D(list_of_z_values[loading_position], u)





print(end_rotation)
