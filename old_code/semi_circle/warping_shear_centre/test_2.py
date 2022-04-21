import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import os

import matplotlib as mpl
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
from shapely.geometry import Point, Polygon
from descartes import PolygonPatch

import sys

# be careful to make sure that the csv matches to the index
os.chdir(r"E:\temp\SC")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\SC\analysis.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1","U2","U3" ]

NoValue = "ASSEMBLY"  ## remove the loading point
indexNames = u[u["Part Instance"]==NoValue].index

u.drop(indexNames , inplace=True)

u.drop(labels = "Part Instance", axis=1, inplace = True)

u = u.astype(np.float64)



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

    points = sorted(list(zip(x_0,y_0)), key=lambda x: x[0])
    alpha = 100#* alphashape.optimizealpha(points)

    print(alpha)
    hull = alphashape.alphashape(points, alpha)
    hull_pts = hull.exterior.coords.xy


    fig, ax = plt.subplots()


    ax.scatter(hull_pts[0], hull_pts[1], color='red')
    plt.show()

    hull_points = sorted(list(zip(hull_pts[0],hull_pts[1])))
    patch  = PolygonPatch(hull, fill=True, color='green')
    # print("z",patch.get_xy())
    x = ax.add_patch(patch)

    print("x",np.array(x))
    #print(hull_points)
    plt.show()



    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x_0, y_0, marker=".", c="#DC143C", edgecolors="black", s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.scatter(x_0, warping_function, marker=".", c="#DC143C", edgecolors="black", s=100)
    ax.set_xlabel('X')
    ax.set_ylabel('warping_displacement')

    plt.show()






    triang = mtri.Triangulation(x_0, y_0)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.triplot(triang, 'bo-', lw=0.2)

    max_radius = 2
    triangles = triang.triangles

    # Mask off unwanted triangles.
    xtri = x_0[triangles] #- np.roll(x_0[triangles], 1, axis=1)
    ytri = y_0[triangles] #- np.roll(y_0[triangles], 1, axis=1)

    path = x.get_path()

    poly = Polygon(path.vertices)
    print("centroid",poly.centroid)
    mask = []
    for i in range(np.shape(xtri)[0]):
        print("a",xtri[i],np.sum(xtri[i])/3 )

        p1 = Point([np.sum(xtri[i])/3,np.sum(ytri[i])/3])
        Boolean  = p1.within(poly)

        mask.append(not p1.within(poly))
    triang.set_mask(mask)


    ax.triplot(triang, color="indigo", lw=2.6)




    # ax.triplot(triang, c="#D3D3D3", marker='.', markerfacecolor="#DC143C",
    #     markeredgecolor="black", markersize=10)

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
    interp_lin = mtri.LinearTriInterpolator(triang, warping_function)

    x_max  = np.amax(hull_pts[0])
    x_min  = np.amin(hull_pts[0])
    y_max  = np.amax(hull_pts[1])
    y_min  = np.amin(hull_pts[1])
    print(np.shape(np.linspace(x_min, x_max, 500)))
    xi, yi = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
    print(np.shape(xi))

    zi_lin = interp_lin(xi, yi)
    print("zi", np.shape(zi_lin))
    interp_cubic_geom = mtri.CubicTriInterpolator(triang, warping_function, kind='geom')
    zi_cubic_geom = interp_cubic_geom(xi, yi)

    interp_cubic_min_E = mtri.CubicTriInterpolator(triang, warping_function, kind='min_E')
    zi_cubic_min_E = interp_cubic_min_E(xi, yi)
    # warping_function = interp_cubic_min_E(xi[15], yi[10])
    # print("a", warping_function)

    # Set up the figure
    fig, axs = plt.subplots(nrows=2, ncols=2)
    axs = axs.flatten()

    # Plot the triangulation.
    axs[0].tricontourf(triang, warping_function)
    axs[0].triplot(triang, 'ko-')
    axs[0].set_title('Triangular grid')

    # Plot linear interpolation to quad grid.
    axs[1].contourf(xi, yi, zi_lin)
    axs[1].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    axs[1].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    axs[1].set_title("Linear interpolation")

    # Plot cubic interpolation to quad grid, kind=geom
    axs[2].contourf(xi, yi, zi_cubic_geom)
    axs[2].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    axs[2].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    axs[2].set_title("Cubic interpolation,\nkind='geom'")

    # Plot cubic interpolation to quad grid, kind=min_E
    axs[3].contourf(xi, yi, zi_cubic_min_E)
    axs[3].plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
    axs[3].plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
    axs[3].set_title("Cubic interpolation,\nkind='min_E'")

    fig.tight_layout()
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    #delaunay triangulation
    # ax.plot_trisurf(triang, warping_function, cmap='jet')
    ax.scatter(xi, yi, zi_cubic_min_E, marker='.', s=10, c="black", alpha=0.5)
    ax.view_init(elev=60, azim=-45)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    area = ((x_max-x_min)/500) * ((y_max-y_min)/500)





    inside_points = []
    I_xx = 0.0
    I_yy = 0.0
    I_xy = 0.0
    I_wy = 0.0
    I_wx = 0.0
    Q_x = 0.0
    Q_y = 0.0

    Gamma = 0.0
    x_centre = 0.0
    y_centre = 0.0
    w_mean =0.0
    for i in range(len(xi)):
        for j in range(len(xi)):
            p1 = Point(xi[i][j],yi[i][j])
            Boolean  = p1.within(poly)
            if Boolean == True:
                x_centre += xi[i][j]
                y_centre += yi[i][j]
                w_mean += zi_cubic_geom[i][j]
                inside_points.append([xi[i][j],yi[i][j],zi_cubic_geom[i][j]])
                # I_xx += area*(yi[i][j])**2
                # I_yy += area*(xi[i][j])**2
                # Q_y += area*(xi[i][j])
                # Q_x += area*(yi[i][j])
                # I_xy += area*(xi[i][j])*(yi[i][j])
                # Gamma += area*(zi_cubic_geom[i][j])**2
            else:
                pass
    x_centre = x_centre/len(inside_points)
    y_centre = y_centre/len(inside_points)
    w_mean = w_mean/len(inside_points)

    print(x_centre,y_centre)

    A = area*len(inside_points)

    print(inside_points[327])
    for xy in inside_points:
        xy[0] = xy[0]-x_centre
        xy[1] = xy[1]-y_centre
        xy[2] = xy[2]+w_mean
    print(inside_points[327])
    print("w_mean", w_mean)
    def Q_xy(y,x,points,dA):
        Q_x = 0.0
        Q_y = 0.0
        for xy in points:
            if xy[1] >= y:
                Q_x += xy[1]*dA
            if xy[0] >= x:
                Q_y += xy[0]*dA
            else:
                pass
        return [Q_x, Q_y]

    # A = area*len(inside_points)

    for xy in inside_points:
        I_yy += area*(xy[0])**2
        I_xx += area*(xy[1])**2
        I_xy += area*xy[0]*xy[1]
        Gamma += area*(xy[2])**2
        Q = Q_xy(xy[1],xy[0],inside_points,area)
        I_wx += xy[1]*(xy[2])*area
        I_wy += xy[1]*(xy[2])*area



    print(A)
    print("I_xx : ", I_xx)
    print("I_yy : ", I_yy)
    print("Gamma : ", Gamma)
    print("Q_y : ", Q_y)
    print("Q_x : ", Q_x)


    e_x= -2*(I_yy*I_wx-I_xy*I_wy)/(I_xx*I_yy-I_xy**2)
    print(e_x)
    e_y = -2*(I_xx*I_wy-I_xy*I_wx)/(I_xx*I_yy-I_xy**2)
    print(e_y)

plot_2d_space(u,1.0)

