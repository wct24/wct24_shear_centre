import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os
# be careful to make sure that the csv matches to the index
os.chdir(r"E:\data-sets\box")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\data-sets\box\rectangle_unrestrained.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)


AF=1
list_of_z_values = np.flip(np.unique(u["z"].values))

list_of_y_values = np.flip(np.unique(u["y"].values))

print("a", list_of_y_values)

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



plt.title("RHS 0.5x0.25x0.125")

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

list_of_y = []

for i in range(9):
    y_c = list_of_y_values[i]
    list_1 = rigid_transform_3D(3, y_c, u)
    new_xy = [(a,b) for a, b in list_1 if abs(a)<=y_c+0.25]
    x,y = zip(*new_xy)
    plt.plot(x,y)
    list_of_y.append(str(y_c))

plt.legend(list_of_y)
plt.xlabel("x - distance along flange m")
plt.ylabel("u_z mm")
plt.grid()
plt.show()




# plt.title("I-beam warping- comparison of the top and bottom flange at loading")

# rigid_transform_3D(1, 0.5, u)
# rigid_transform_3D(1, -0.5, u)
# plt.legend(["top","bottom"])
# plt.xlabel("x - distance along flange m")
# plt.ylabel("u_z mm")

# plt.show()

# plt.title("I-beam warping- comparison of the top and bottom flange at boundary condition")

# rigid_transform_3D(0, 0.5, u)
# rigid_transform_3D(0, -0.5, u)
# plt.legend(["top","bottom"])
# plt.xlabel("x - distance along flange m")
# plt.ylabel("u_z mm")

# plt.show()
