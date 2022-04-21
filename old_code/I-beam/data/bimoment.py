import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os
# be careful to make sure that the csv matches to the index
os.chdir(r"E:\temp\I")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\I\analysis.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)


AF=1
list_of_z_values = np.flip(np.unique(u["z"].values))

def rigid_transform_3D(z,y,DF):
    df2 = DF[DF["z"]==z]
    print(df2)
    df2 = df2[df2["y"]==y]
    # print(df2)
    x_0 = df2["x"].values
    y_0 = df2["y"].values
    z_0 = df2["z"].values
    print(x_0)
    x_1 = x_0 + df2["U1"].values*AF
    y_1 = y_0 + df2["U2"].values*AF
    z_1 = df2["U3"].values*1000

    plt.plot(x_0, z_1)



plt.title("I-beam warping- comparison of the top flange at loading and at BC")

rigid_transform_3D(1, 0.5, u)
rigid_transform_3D(0, 0.5, u)
plt.legend(["loading","BC"])
plt.xlabel("x - distance along flange m")
plt.ylabel("u_z mm")

plt.show()

plt.title("I-beam warping- comparison of the top and bottom flange at loading")

rigid_transform_3D(1, 0.5, u)
rigid_transform_3D(1, -0.5, u)
plt.legend(["top","bottom"])
plt.xlabel("x - distance along flange m")
plt.ylabel("u_z mm")

plt.show()

plt.title("I-beam warping- comparison of the top and bottom flange at boundary condition")

rigid_transform_3D(0, 0.5, u)
rigid_transform_3D(0, -0.5, u)
plt.legend(["top","bottom"])
plt.xlabel("x - distance along flange m")
plt.ylabel("u_z mm")

plt.show()










# def plot_residual(DF):
#   list_of_z_values = np.flip(np.unique(u["z"].values))
#   list_of_z_values = np.delete(list_of_z_values, np.where(list_of_z_values == 0.0))
#   error_list = []
#   angle_list = []
#   for z in list_of_z_values:
#     R, t, ang, e =  rigid_transform_3D(z,DF)
#     plt.close()
#     error_list.append(e)
#     angle_list.append(ang[0])
#   # print(angle_list)
#   # print(list(list_of_z_values))
#   plt.subplot(1,2,1)
#   plt.title("residual")
#   plt.plot(list_of_z_values, error_list)
#   plt.subplot(1,2,2)
#   plt.title("rotation AF = {}".format(AF))
#   plt.figure(figsize=(13, 10))
#   print(angle_list)
#   plt.plot(list_of_z_values, angle_list)
#   plt.show()



# plot_residual(u)
