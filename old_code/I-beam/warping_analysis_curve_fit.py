import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import alphashape

# import matplotlib
# from matplotlib.ticker import MaxNLocator
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
# from scipy import array, newaxis

from matplotlib.tri import Triangulation
from matplotlib.collections import LineCollection

import sys

# be careful to make sure that the csv matches to the index
os.chdir(r"E:\temp\I")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\I\analysis.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1","U2","U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)

# be careful to make sure that the csv matches to the index
d = pd.read_csv(r'E:\temp\I\stress.csv', header = 0, usecols = [3, 12,13,14,25])
d.columns=["Part Instance", "x", "y", "z","S33" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = d[d["Part Instance"]==NoValue].index

d.drop(indexNames , inplace=True)

d.drop(labels = "Part Instance", axis=1, inplace = True)

d = d.astype(np.float64)








def plot_2d_space(DF,z):
    df1 = DF.loc[DF["z"]==z]
    x_0 = df1["x"].values
    y_0 = df1["y"].values
    z_0 = df1["z"].values
    warping_displacement = df1["U3"].values
    # find the twist:

    x_1 = x_0 + df1["U1"].values
    y_1 = y_0 + df1["U2"].values
    z_1 = z_0 + df1["U3"].values

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
    twist = ang[2]
    print(twist)
    warping_function = warping_displacement/twist


    # x_0 = np.append(x_0, [0.025,-0.025])
    # y_0 = np.append(y_0, [0,0])

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x_0, y_0, marker=".", c="#DC143C", edgecolors="black", s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.show()

    triang = mtri.Triangulation(x_0, y_0)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
        markeredgecolor="black", markersize=10)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    #delaunay triangulation
    ax.plot_trisurf(triang, warping_function, cmap='jet')
    ax.scatter(x_0,y_0,warping_function, marker='.', s=10, c="black", alpha=0.5)
    ax.view_init(elev=60, azim=-45)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

    points = sorted(list(zip(x_0,y_0)), key=lambda x: x[0])
    alpha = 1#0.95 * alphashape.optimizealpha(points)


    hull = alphashape.alphashape(points, alpha)
    hull_pts = hull.exterior.coords.xy

    fig, ax = plt.subplots()
    ax.scatter(hull_pts[0], hull_pts[1], color='red')
    plt.show()


    for i in range(9):
        alpha = (i+1)*.1
        concave_hull, edge_points = alphashape.alphashape(points,
                                                alpha=alpha)

        #print concave_hull
        lines = LineCollection(edge_points)
        pl.figure(figsize=(10,10))
        pl.title('Alpha={0} Delaunay triangulation'.format(alpha))
        pl.gca().add_collection(lines)
        delaunay_points = np.array([point.coords[0] for point in points])
        pl.plot(delaunay_points[:,0], delaunay_points[:,1],
                'o', hold=1, color='#f16824')

        _ = plot_polygon(concave_hull)
        _ = pl.plot(x,y,'o', color='#f16824')





    # interp_lin = mtri.LinearTriInterpolator(triang, warping_function)

    # xi, yi = np.meshgrid(np.linspace(-0.06, 0.06, 40), np.linspace(-0.09, 0.09, 40))
    # zi_lin = interp_lin(xi, yi)
    # interp_cubic_geom = mtri.CubicTriInterpolator(triang, warping_function, kind='geom')
    # zi_cubic_geom = interp_cubic_geom(xi, yi)

    # interp_cubic_min_E = mtri.CubicTriInterpolator(triang, warping_function, kind='min_E')
    # zi_cubic_min_E = interp_cubic_min_E(xi, yi)
    # # warping_function = interp_cubic_min_E(xi[15], yi[10])
    # # print("a", warping_function)

    # # Set up the figure
    # fig, axs = plt.subplots(nrows=2, ncols=2)
    # axs = axs.flatten()

    # # Plot the triangulation.
    # axs[0].tricontourf(triang, warping_function)
    # axs[0].triplot(triang, 'ko-')
    # axs[0].set_title('Triangular grid')

    # # Plot linear interpolation to quad grid.
    # axs[1].contourf(xi, yi, zi_lin)
    # axs[1].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    # axs[1].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    # axs[1].set_title("Linear interpolation")

    # # Plot cubic interpolation to quad grid, kind=geom
    # axs[2].contourf(xi, yi, zi_cubic_geom)
    # axs[2].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    # axs[2].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    # axs[2].set_title("Cubic interpolation,\nkind='geom'")

    # # Plot cubic interpolation to quad grid, kind=min_E
    # axs[3].contourf(xi, yi, zi_cubic_min_E)
    # axs[3].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    # axs[3].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    # axs[3].set_title("Cubic interpolation,\nkind='min_E'")

    # fig.tight_layout()
    # plt.show()

    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1, projection='3d')
    # #delaunay triangulation
    # # ax.plot_trisurf(triang, warping_function, cmap='jet')
    # ax.scatter(xi, yi, zi_cubic_min_E, marker='.', s=10, c="black", alpha=0.5)
    # ax.view_init(elev=60, azim=-45)

    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    # plt.show()


    # print(interp_lin)

    # #https://www.fabrizioguerrieri.com/blog/surface-graphs-with-irregular-dataset/






    # # fig = plt.figure()
    # # ax = fig.add_subplot(projection='3d')
    # # ax.scatter(x_0, y_0, warping_function)
    # # plt.show()






    # # tri = Triangulation(np.ravel(x_0), np.ravel(y_0))

    # # fig = plt.figure()
    # # ax = fig.add_subplot(111, projection='3d')
    # # ax.scatter(x_0, y_0, warping_function)
    # # surf = ax.plot_trisurf(x_0, y_0, warping_function, cmap='viridis', linewidth=0)
    # # fig.colorbar(surf)

    # # ax.xaxis.set_major_locator(MaxNLocator(5))
    # # ax.yaxis.set_major_locator(MaxNLocator(6))
    # # ax.zaxis.set_major_locator(MaxNLocator(5))

    # # fig.tight_layout()







    # # plt.show()


# plot_2d_space(u,1.0)























# def domain(u,z):




# def warping_constant(z,DF_U3,DF_S33):
#     df1 = DF_U3.loc[DF_U3["z"]==z]
#     df2 = DF_S33.loc[DF_U3["z"]==z]
#     df2['area'] = 1/df2['S33']

#     area = df2["area"].values
#     x_0 = df1["x"].values
#     y_0 = df1["y"].values
#     z_0 = df1["z"].values
#     x_1 = x_0 + df1["U1"].values
#     y_1 = y_0 + df1["U2"].values
#     z_1 = z_0 + df1["U3"].values

#     A = np.vstack([x_1,y_1,z_1])
#     B = np.vstack([x_0,y_0,z_0])

#     assert A.shape == B.shape

#     num_rows, num_cols = A.shape
#     if num_rows != 3:
#         raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")

#     num_rows, num_cols = B.shape
#     if num_rows != 3:
#         raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

#     # find mean column wise
#     centroid_A = np.mean(A, axis=1)
#     centroid_B = np.mean(B, axis=1)

#     # ensure centroids are 3x1
#     centroid_A = centroid_A.reshape(-1, 1)
#     centroid_B = centroid_B.reshape(-1, 1)

#     # subtract mean
#     Am = A - centroid_A
#     Bm = B - centroid_B

#     H = Am @ np.transpose(Bm)

#     # find rotation
#     U, S, Vt = np.linalg.svd(H)
#     R = Vt.T @ U.T

#     t = -R @ centroid_A + centroid_B
#     XYZ_2  = R @ A + t


#     x_2 = XYZ_2[0]
#     y_2 = XYZ_2[1]
#     z_2 = XYZ_2[2]

#     ang = eul.mat2euler(R, axes='sxyz')
#     e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
#     rotation = ang[2]
#     warping_function = np.square(df1["U3"].values/rotation)
#     gamma = np.dot(area,warping_function )


#     return gamma


# gamma = warping_constant(1.0,u,d)


# print(gamma)
