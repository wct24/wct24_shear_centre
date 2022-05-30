import pandas as pd
import os
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt

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

from matplotlib.widgets import Slider, Button

import sys

# import the necessary packages
from scipy.spatial import distance as dist
import numpy as np
import cv2
import math
from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# ## for Palatino and other serif fonts use:
# #rc('font',**{'family':'serif','serif':['Palatino']})
# rc('text', usetex=True)
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

import matplotlib.pyplot as plt


# # be careful to make sure that the csv matches to the index
# os.chdir(r"E:\temp\SC")

# # be careful to make sure that the csv matches to the index
# u = pd.read_csv(r'E:\temp\SC\displacement.csv', header = 0, usecols = [3, 4,12,13,14,16,17,18])
# u.columns=["Part Instance","Node", "x", "y", "z","U1","U2","U3" ]

# NoValue = "ASSEMBLY"  ## remove the loading point
# indexNames = u[u["Part Instance"]==NoValue].index

# u.drop(indexNames , inplace=True)

# u.drop(labels = "Part Instance", axis=1, inplace = True)

# u = u.astype(np.float64)


# # be careful to make sure that the csv matches to the index
# s = pd.read_csv(r'E:\temp\SC\stress.csv', header = 0, usecols = [4,5,6,7,8])
# s.columns=["Element", "Node","x", "y" ,"z"]

# s = s.astype(np.float64)



# def order_points(pts):
#     # sort the points based on their x-coordinates
#     xSorted = pts[np.argsort(pts[:, 0]), :]
#     # grab the left-most and right-most points from the sorted
#     # x-roodinate points
#     leftMost = xSorted[:2, :]
#     rightMost = xSorted[2:, :]
#     # now, sort the left-most coordinates according to their
#     # y-coordinates so we can grab the top-left and bottom-left
#     # points, respectively
#     leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
#     (tl, bl) = leftMost
#     # now that we have the top-left coordinate, use it as an
#     # anchor to calculate the Euclidean distance between the
#     # top-left and right-most points; by the Pythagorean
#     # theorem, the point with the largest distance will be
#     # our bottom-right point
#     D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
#     (br, tr) = rightMost[np.argsort(D)[::-1], :]
#     # return the coordinates in top-left, top-right,
#     # bottom-right, and bottom-left order
#     return np.array([tl, tr, br, bl], dtype="float64")


# def connected_nodes(DF,x,y,z):
#     """ returns a list of connected nodes
#         1. find the element the node belongs to
#         2. find the coordinates of all the nodes in the element"""
#     DF = s.loc[DF["z"]==z]
#     DF.drop(labels = "z", axis=1, inplace = True)
#     condition = (DF['x'] ==x) & (DF['y'] == y)
#     b = DF.index[condition].tolist()
#     element = DF.loc[b]["Element"].values[0]
#     condition = (DF['Element'] ==element)
#     b = DF.index[condition].tolist()
#     xy = DF.loc[b]
#     x = xy["x"].values.T
#     y = xy["y"].values.T

#     xy = np.array(list(zip(x,y)))

#     xSorted = xy[xy[:, 0].argsort()]
#     y_sorted = xy[xy[:, 1].argsort()]
#     leftMost = xSorted[:2, :]
#     rightMost = xSorted[2:, :]

#     leftMost = leftMost[leftMost[:, 1].argsort()]
#     (tl, bl) = leftMost

#     rightMost = rightMost[rightMost[:, 1].argsort()]
#     (tr, br) = rightMost

#     # element = order_points(element)
#     return np.array([tl, tr, br, bl], dtype="float64")


# def get_z_values(DF):
#     """returns a the z values of the sections in descending order"""
#     list_of_z_values = np.flip(np.unique(DF["z"].values))
#     return list_of_z_values

# def angle(DF,z):
#     """returns the angle which section rotates
#     in the z direction given a certain distance along the beam"""

#     df1 = DF.loc[DF["z"]==z]
#     x_0 = df1["x"].values
#     y_0 = df1["y"].values
#     z_0 = df1["z"].values
#     warping_displacement = df1["U3"].values

#     # find the rotation:

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
#     U, S, Vt = np.linalg.svd(H)
#     R = Vt.T @ U.T

#     t = -R @ centroid_A + centroid_B
#     XYZ_2  = R @ A + t

#     x_2 = XYZ_2[0]
#     y_2 = XYZ_2[1]
#     z_2 = XYZ_2[2]
#     ang = eul.mat2euler(R, axes='sxyz')
#     return ang[2]

# def get_sc_from_w(DF,z,n):
#     df1 = DF.loc[DF["z"]==z]
#     x_0 = df1["x"].values
#     y_0 = df1["y"].values

#     x_1 = x_0 + df1["U1"].values
#     y_1 = y_0 + df1["U2"].values

#     x = np.linspace(0, 1, 100)

#     m_array= np.zeros(len(x_0))
#     c_array = np.zeros(len(x_0))

#     for i in range(len(x_0)):
#         v1 = np.array([x_1[i]-x_0[i],y_1[i]-y_0[i]])
#         v1_unit = v1/np.linalg.norm(v1)
#         v1_perpendicular = np.matmul(np.array([[0,-1],[1,0]]),v1)
#         m= v1_perpendicular[1]/v1_perpendicular[0]
#         c = -m*x_0[i]+y_0[i]
#         m_array[i] = m
#         c_array[i] = c

#     A = np.vstack([-m_array, np.ones(len(m_array))]).T
#     x_rc, y_rc= np.linalg.lstsq(A, c_array, rcond=None)[0]

#     twist = (angle(DF,list_of_z_values[n]) - angle(DF,list_of_z_values[n+1]))/(list_of_z_values[n]-list_of_z_values[n+1])
#     a_number = twist
#     significant_digits = 6
#     twist =  round(a_number, significant_digits - int(math.floor(math.log10(abs(a_number)))) - 1)


#     element_ids = []
#     element_df = pd.DataFrame(columns = ["X0", "Y0", "X1", "Y1", "X2", "Y2", "X3", "Y3", "W0", "W1", "W2", "W3"])

#     for i in range(len(x_0)):
#         [[X0,Y0], [X1,Y1], [X2,Y2], [X3,Y3]] = connected_nodes(s,x_0[i],y_0[i],z)

#         condition = (df1['x'] == X0) & (df1['y'] == Y0)
#         b = df1.index[condition].tolist()
#         W0 = df1.loc[b]["U3"].values[0]/twist

#         condition = (df1['x'] == X1) & (df1['y'] == Y1)
#         b = df1.index[condition].tolist()
#         W1 = df1.loc[b]["U3"].values[0]/twist

#         condition = (df1['x'] == X2) & (df1['y'] == Y2)
#         b = df1.index[condition].tolist()
#         W2 = df1.loc[b]["U3"].values[0]/twist

#         condition = (df1['x'] == X3) & (df1['y'] == Y3)
#         b = df1.index[condition].tolist()
#         W3 = df1.loc[b]["U3"].values[0]/twist

#         element_id = X0*Y0*X1*Y1*X2*Y2*X3*Y3*W0*W1*W2*W3

#         if element_id not in element_ids:
#             df2 = pd.DataFrame([[X0, Y0, X1, Y1, X2, Y2, X3, Y3, W0, W1, W2, W3]], columns = ["X0", "Y0", "X1", "Y1", "X2", "Y2", "X3", "Y3", "W0", "W1", "W2", "W3"])
#             # print(df2)
#             element_df = element_df.append(df2, ignore_index = True)
#             element_ids.append(element_id)
#     sc_list = []

#     for i in range(len(element_ids)):

#         ele = element_df.iloc[[i]]
#         # po = [[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]]
#         po = np.array([[0,2],[1,3]])
#         c_vector= np.zeros([len(po)])
#         ab = np.zeros(np.shape(po))
#         for i in range(len(po)):
#             v1 = np.array([(ele["X{}".format(po[i][1])]-ele["X{}".format(po[i][0])]), (ele["Y{}".format(po[i][1])]-ele["Y{}".format(po[i][0])])])

#             ds_1 = np.linalg.norm(v1)
#             dw_1 = ele["W{}".format(po[i][1])].values[0]-ele["W{}".format(po[i][0])].values[0]
#             rs_1 = dw_1/ds_1
#             v1_perpendicular = rs_1/ds_1*np.matmul(np.array([[0,-1],[1,0]]),v1)



#             X1 = ele["X{}".format(po[i][1])].values[0]
#             Y1 = ele["Y{}".format(po[i][1])].values[0]
#             X0 = ele["X{}".format(po[i][0])].values[0]
#             Y0 = ele["Y{}".format(po[i][0])].values[0]

#             po_1 = np.array([X1,Y1]) + np.transpose(v1_perpendicular)
#             po_0 = np.array([X0,Y0]) + np.transpose(v1_perpendicular)
#             # print("a",po_1,po_0)
#             points = np.vstack([po_1,po_0])


#             a = points[1][1]-points[0][1]
#             b = points[0][0]-points[1][0]
#             c = a*points[0][0]+b*points[0][1]

#             ab[i,:] = np.array([a,b])
#             c_vector[i] = c
#         sc = np.matmul(np.linalg.inv(ab),c_vector)
#         sc_list.append(sc)
#     sc_list = np.array(sc_list)
#     a = np.array(sc_list)
#     sc = np.mean(a, axis=0)
#     x_sc = sc[0]
#     y_sc = sc[1]
#     spread = np.std(a, axis=0, dtype=np.float64)
#     print("shear_centre : ",sc, " /  std : ", spread, "z : ", z)
#     return x_sc,y_sc,x_rc,y_rc





# def rotation_center(DF,z):
#     df1 = DF.loc[DF["z"]==z]
#     x_0 = df1["x"].values
#     y_0 = df1["y"].values
#     # find the rotation:
#     x_1 = x_0 + df1["U1"].values
#     y_1 = y_0 + df1["U2"].values

#     x = np.linspace(-1, 1, 100)

#     m_array= np.zeros(len(x_0))
#     c_array = np.zeros(len(x_0))

#     for i in range(len(x_0)):
#         v1 = np.array([x_1[i]-x_0[i],y_1[i]-y_0[i]])
#         v1_unit = v1/np.linalg.norm(v1)
#         v1_perpendicular = np.matmul(np.array([[0,-1],[1,0]]),v1)
#         print(v1_perpendicular)
#         m= v1_perpendicular[1]/v1_perpendicular[0]
#         c = -m*x_0[i]+y_0[i]

#         m_array[i] = m
#         c_array[i] = c
#         y=m*x+c
#         plt.plot(x, y)



#     A = np.vstack([-m_array, np.ones(len(m_array))]).T
#     x_sc, y_sc = np.linalg.lstsq(A, c_array, rcond=None)[0]
#     plt.scatter(x_sc, y_sc)
#     plt.title("hodograph")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.show()

# # rotation_center(u,1.0)


# list_of_z_values = get_z_values(u)

# x_sc_list = []
# y_sc_list = []
# x_rc_list = []
# y_rc_list = []


# for i in range(len(list_of_z_values)-1):
#     x_sc,y_sc,x_rc,y_rc = get_sc_from_w(u,list_of_z_values[i],i)
#     x_sc_list.append(x_sc)
#     y_sc_list.append(y_sc)
#     x_rc_list.append(x_rc)
#     y_rc_list.append(y_rc)


# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)

# ax.scatter(x_sc_list,list_of_z_values[0:-1])
# ax.scatter(x_rc_list,list_of_z_values[0:-1])
# plt.show()


# # # rotation_center(u, list_of_z_values[15])




def z_rotation_at_z(SectionPosition,abaqus_output_file_location):
    ''''takes a z coordinate and an abaqus output file directory
    and returns the axial rotation'''

    u = pd.read_csv(abaqus_output_file_location, header = 0, usecols = [3, 12,13,14,16,17,18])
    u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

    NoValue = "ASSEMBLY"  ## remove the loading point
    indexNames = u[u["Part Instance"]==NoValue].index

    u.drop(indexNames , inplace=True)

    u.drop(labels = "Part Instance", axis=1, inplace = True)

    u = u.astype(np.float64)

    AF = 1
    z_list = np.flip(np.unique(u["z"].values))
    z = z_list[SectionPosition]
    df2 = u.loc[u["z"]==z]

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

    # plt.scatter(x_0, y_0)
    # plt.scatter(x_2, y_2)
    # plt.gca().set_aspect('equal', adjustable='box')
    ang = eul.mat2euler(R, axes='sxyz')
    e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
    return ang[2]

def z_rotation_plot_along_beam(abaqus_output_file_location):
    ''''takes an abaqus output file directory
    and returns graph of rotations along the beam'''
    u = pd.read_csv(abaqus_output_file_location, header = 0, usecols = [3, 12,13,14,16,17,18])
    u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

    NoValue = "ASSEMBLY"  ## remove the loading point
    indexNames = u[u["Part Instance"]==NoValue].index

    u.drop(indexNames , inplace=True)

    u.drop(labels = "Part Instance", axis=1, inplace = True)

    u = u.astype(np.float64)

    AF = 1

    z_list = np.flip(np.unique(u["z"].values))
    rotation = []
    for z in z_list:
        df2 = u.loc[u["z"]==z]

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

        # plt.scatter(x_0, y_0)
        # plt.scatter(x_2, y_2)
        # plt.gca().set_aspect('equal', adjustable='box')
        ang = eul.mat2euler(R, axes='sxyz')
        e = np.sqrt(np.sum((x_2-x_0)**2)+np.sum((y_2-y_0)**2)+np.sum((z_2-z_0)**2))
        rotation.append(ang[2])


    plt.plot(z_list, rotation)



def plot_rotation_with_x_sweep(sweep_directory):
    ''' takes a directory with the data of a sweep and plots the rotation'''
    os.chdir(sweep_directory)
    #get the xs directly from the names of the folders
    x_list = sorted([float(name) for name in os.listdir(".") if os.path.isdir(name)])
    rotation_list = []
    for x in x_list:
        csv_path = sweep_directory + r"/{}/displacement.csv".format(str(x))
        R_z = z_rotation_at_z(99,csv_path)*180/np.pi
        rotation_list.append(R_z)


    x_list = [x /10 for x in x_list]
    plt.plot(x_list, rotation_list)





def plot_rotation(sweep_directory):
    ''' takes a directory with the data of a sweep and plots the rotation'''
    os.chdir(sweep_directory)
    #get the xs directly from the names of the folders
    x_list = sorted([float(name) for name in os.listdir(".") if os.path.isdir(name)])
    rotation_list = []
    for x in x_list:
        csv_path = sweep_directory + r"/{}/displacement.csv".format(str(x))
        z_rotation_plot_along_beam(csv_path)
    plt.show()














plot_rotation_with_x_sweep(r"E:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\TSC\0\EndRotationXsweep\10N")
plot_rotation_with_x_sweep(r"E:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\TSC\0\\EndRotationXsweep\1000N")



plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.yticks([-90,-60,-30,0,30,60,90])
plt.ylim(-90, 90)
plt.xlim(-10, 10)
plt.xlabel(r'$x$ / m ', )
plt.ylabel(r'$\theta_{z}$ / \textdegree ')


plt.grid()

plt.legend((r"$S_{y}(x,0,0.05) = 10N$","$S_{y}(x,0,0.05) = 1000N$"),loc="lower right")



plt.show()
# plot_rotation(r"E:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\TSC\0\sweep")
# z_rotation_plot_along_beam(r"E:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\TSC\0\sweep\5.0\displacement.csv")
