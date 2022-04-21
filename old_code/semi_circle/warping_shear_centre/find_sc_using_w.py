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
import math

# import matplotlib
# from matplotlib.ticker import MaxNLocator
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
# from scipy import array, newaxis

from matplotlib.tri import Triangulation
from matplotlib.collections import LineCollection
from shapely.geometry import Point, Polygon
from descartes import PolygonPatch
from pathlib import Path

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

    # x_1 = x_0 + df1["U1"].values
    # y_1 = y_0 + df1["U2"].values
    # z_1 = z_0 + df1["U3"].values

    # A = np.vstack([x_1,y_1,z_1])
    # B = np.vstack([x_0,y_0,z_0])

    # assert A.shape == B.shape

    # num_rows, num_cols = A.shape
    # if num_rows != 3:
    #     raise Exception(f"matrix A is not 3xN, it is {num_rows}x{num_cols}")

    # num_rows, num_cols = B.shape
    # if num_rows != 3:
    #     raise Exception(f"matrix B is not 3xN, it is {num_rows}x{num_cols}")

    # # find mean column wise
    # centroid_A = np.mean(A, axis=1)
    # centroid_B = np.mean(B, axis=1)
    # # ensure centroids are 3x1
    # centroid_A = centroid_A.reshape(-1, 1)
    # centroid_B = centroid_B.reshape(-1, 1)
    # # subtract mean
    # Am = A - centroid_A
    # Bm = B - centroid_B
    # H = Am @ np.transpose(Bm)

    # # find rotation
    # U, S, Vt = np.linalg.svd(H)
    # R = Vt.T @ U.T
    # t = -R @ centroid_A + centroid_B
    # XYZ_2  = R @ A + t
    # x_2 = XYZ_2[0]
    # y_2 = XYZ_2[1]
    # z_2 = XYZ_2[2]

    # ang = eul.mat2euler(R, axes='sxyz')
    # e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
    # twist = ang[2]
    # print("twist : ", twist)
    twist = 3.0779520744228755e-05
    a_number = twist
    significant_digits = 6
    rounded_number =  round(a_number, significant_digits - int(math.floor(math.log10(abs(a_number)))) - 1)
    warping_function = warping_displacement/rounded_number

    points = sorted(list(zip(x_0,y_0)), key=lambda x: x[0])


    alpha = 100#* alphashape.optimizealpha(points)
    hull = alphashape.alphashape(points, alpha)
    hull_pts = hull.exterior.coords.xy

    print("Does graph accurately show the outline of the shape?")
    fig, ax = plt.subplots()
    ax.scatter(hull_pts[0], hull_pts[1], color='red')
    plt.show()

    hull_points = sorted(list(zip(hull_pts[0],hull_pts[1])))
    patch  = PolygonPatch(hull, fill=True, color='green')
    x = ax.add_patch(patch)
    plt.show()






    ### plots of the data
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
    xtri = x_0[triangles]
    ytri = y_0[triangles]

    path = x.get_path()
    poly = Polygon(path.vertices)
    mask = []
    for i in range(np.shape(xtri)[0]):
        p1 = Point([np.sum(xtri[i])/3,np.sum(ytri[i])/3])
        Boolean  = p1.within(poly)
        mask.append(not p1.within(poly))


    #this verifies that the right triangles are masked off
    triang.set_mask(mask)
    ax.triplot(triang, color="indigo", lw=2.6)
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

    print("f", x_max, y_max, x_min, y_min)


    n_grid_points = 300
    xi, yi = np.meshgrid(np.linspace(x_min, x_max, n_grid_points), np.linspace(y_min, y_max, n_grid_points))

    interp_cubic_geom = mtri.CubicTriInterpolator(triang, warping_function, kind='geom')
    zi_cubic_geom = interp_cubic_geom(xi, yi)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    #delaunay triangulation
    area = ((x_max-x_min)/n_grid_points) * ((y_max-y_min)/n_grid_points)


    #empty dataframe:
    column_names = ["x", "y", "w"]

    inside_points = pd.DataFrame(columns = column_names)

    for i in range(len(xi)):
        for j in range(len(xi)):
            p1 = Point(xi[i][j],yi[i][j])
            Boolean  = p1.within(poly)
            if Boolean == True:
                point = pd.DataFrame([[xi[i][j], yi[i][j], zi_cubic_geom[i][j]]], columns=["x","y","w"])
                inside_points = inside_points.append(point, ignore_index=True)

            else:
                pass
    inside_points = inside_points.astype(np.float64)
    filepath = Path('out.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    inside_points.to_csv(filepath)

    # inside_points = pd.read_csv(r'E:\temp\SC\out.csv', header = 0, usecols = [3, 12,13,14,16,17,18])

    # def find_adjacent_points(point, df):
    #     x = point[0]
    #     y = point[1]
    #     dx = (x_max-x_min)/n_grid_points
    #     dy = ((y_max-y_min)/n_grid_points)

    #     b = (df[(df['x']  == x) & (df['y'] == y+dy)].index.tolist())
    #     print(b)
    #     return df[b]


    # print(find_adjacent_points([0.032863,0.408357],inside_points))



plot_2d_space(u,1.0)

