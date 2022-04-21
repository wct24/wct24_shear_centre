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
warping_unrestrained = pd.read_csv(r'E:\data-sets\box\warping_unrestrained.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
warping_unrestrained.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = warping_unrestrained[warping_unrestrained["Part Instance"]==NoValue].index

warping_unrestrained.drop(indexNames , inplace=True)

warping_unrestrained.drop(labels = "Part Instance", axis=1, inplace = True)

warping_unrestrained  = warping_unrestrained.astype(np.float64)

AF=1
list_of_z_values = np.flip(np.unique(unrestrained["z"].values))

list_of_y_values = np.flip(np.unique(unrestrained["y"].values))

print(list_of_y_values)


def rigid_transform_3D(z,y,DF):
    df2 = DF[DF["z"]==z]

    df2 = df2[df2["y"]==y]
    # print(df2)
    x_0 = df2["x"].values
    y_0 = df2["y"].values
    z_0 = df2["z"].values

    x_1 = x_0 + df2["U1"].values*AF
    y_1 = y_0 + df2["U2"].values*AF
    z_1 = df2["U3"].values*1000
    plot_list = sorted(list(zip(x_1,z_1)), key=lambda x: x[0])
    return plot_list

plt.title(" comparison between a SHS 1x1x0.125 and RHS 1x0.5x0.125")

# x,y = zip(*rigid_transform_3D(3, 0.5, u))
# plt.plot(x,y)


# list_1 = rigid_transform_3D(3, 0.4375, u)
# print(list_1)
# new_xy = [(a,b) for a, b in list_1 if abs(a)<=.4376]
# x,y = zip(*new_xy)

# plt.plot(x,y)

# list_1 = rigid_transform_3D(3, 0.375, u)

# new_xy = [(a,b) for a, b in list_1 if abs(a)<=.376]
# x,y = zip(*new_xy)

# plt.plot(x,y)


list_1 = rigid_transform_3D(3, .25, unrestrained)
new_xy = [(a,b) for a, b in list_1 if abs(a)<=.5+0.001]
x,y = zip(*new_xy)
plt.plot(x,y)

list_2 = rigid_transform_3D(3, .5, warping_unrestrained)
new_xy = [(a,b) for a, b in list_2 if abs(a)<=.5+0.001]
x,y = zip(*new_xy)
plt.plot(x,y)





plt.xlabel("x - distance along flange m")
plt.ylabel("u_z mm")
plt.grid()
plt.show()



























# unrestrained_rotation_list = []
# for z in list_of_z_values:
#     unrestrained_rotation_list.append(z_rotation(z,unrestrained))

# restrained_rotation_list = []
# for z in list_of_z_values:
#     restrained_rotation_list.append(z_rotation(z,restrained))


# plt.plot(list_of_z_values, unrestrained_rotation_list)
# plt.plot(list_of_z_values, restrained_rotation_list)




# plt.xlabel("x - distance along flange m")
# plt.ylabel("u_z mm")
# plt.grid()
# plt.show()
