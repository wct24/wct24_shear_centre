import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os
# be careful to make sure that the csv matches to the index
os.chdir(r"E:\data-sets\box")

# be careful to make sure that the csv matches to the index
unrestrained = pd.read_csv(r'E:\data-sets\box\rectangle_unrestrained.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
unrestrained.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = unrestrained[unrestrained["Part Instance"]==NoValue].index

unrestrained.drop(indexNames , inplace=True)

unrestrained.drop(labels = "Part Instance", axis=1, inplace = True)

unrestrained  = unrestrained.astype(np.float64)



# be careful to make sure that the csv matches to the index
restrained = pd.read_csv(r'E:\data-sets\box\rectangle_restrained.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
restrained.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = restrained[restrained["Part Instance"]==NoValue].index

restrained.drop(indexNames , inplace=True)

restrained.drop(labels = "Part Instance", axis=1, inplace = True)

restrained  = restrained.astype(np.float64)

AF=1
list_of_z_values = np.flip(np.unique(unrestrained["z"].values))

list_of_y_values = np.flip(np.unique(unrestrained["y"].values))

print(list_of_y_values)


def z_rotation(z,DF):
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

    ang = eul.mat2euler(R, axes='sxyz')
    e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
    rotation = ang[2] *180/np.pi
    return rotation



unrestrained_rotation_list = []
for z in list_of_z_values:
    unrestrained_rotation_list.append(z_rotation(z,unrestrained))

restrained_rotation_list = []
for z in list_of_z_values:
    restrained_rotation_list.append(z_rotation(z,restrained))


plt.plot(list_of_z_values, unrestrained_rotation_list)
plt.plot(list_of_z_values, restrained_rotation_list)

plt.legend(["unrestrained warping", "restrained warping"])


plt.xlabel("x - distance along flange m")
plt.ylabel("rotation / degrees")
plt.grid()
plt.show()
