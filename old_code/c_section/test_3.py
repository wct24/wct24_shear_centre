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
os.chdir(r"E:\temp\c_section")


inside_points = pd.read_csv(r'E:\temp\c_section\out.csv', header = 0,usecols = [1, 2, 3])

inside_points = inside_points.astype(np.float64)

print(inside_points)

number_of_rows = len(inside_points.index)

xy = inside_points.iloc[[3]].to_numpy()[0]

x_max = 0.40997
y_max = 0.41
x_min = 0.0
y_min = -0.41

n_grid_points = 299





def shear_centre(point, df):
    x = point[0]
    y = point[1]
    dx = (x_max-x_min)/n_grid_points
    dy = ((y_max-y_min)/n_grid_points)

    index = df.index
    # find y coordinte
    condition = (abs(df['x']-x)<= 2*dx+0.000001) & (df['y'] == y)
    b = index[condition].tolist()
    df_x = df.iloc[b]
    #get the min and max value of x
    max_x = df_x['x'].idxmax()
    min_x = df_x['x'].idxmin()



    ds = df_x["x"][max_x]-df_x["x"][min_x]
    dw = df_x["w"][max_x]-df_x["w"][min_x]
    if ds<0.000001:
        rs = 0
    else:
        rs=dw/ds

    y_sc = y +rs





     # find x coordinte
    condition = (abs(df['y']-y)<= 2*dx+0.000001) & (df['x'] == x)
    b = index[condition].tolist()
    df_y = df.iloc[b]

    #get the min and max value of x
    max_y = df_y['y'].idxmax()
    min_y = df_y['y'].idxmin()


    ds = df_y["y"][max_y]-df_y["y"][min_y]
    dw = df_y["w"][max_y]-df_y["w"][min_y]
    if ds<0.000001:
        rs = 0
    else:
        rs=-dw/ds


    x_sc = x +rs

    return [x_sc,y_sc]


sc_array = []

print(np.shape(sc_array))

for i in range(number_of_rows):
    print(1)
    xy = inside_points.iloc[[i]].to_numpy()[0]
    sc_array.append(shear_centre(xy,inside_points))


print(np.shape(sc_array))
print(sc_array)
x_0 = inside_points["x"].values
y_0 = inside_points["y"].values

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(x_0, y_0, marker=".", c="#DC143C", edgecolors="black", s=100)
ax.scatter(*zip(*list(sc_array)))
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()


