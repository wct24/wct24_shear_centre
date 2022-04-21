import pandas as pd
import numpy as np
import transforms3d.euler as eul
import matplotlib.pyplot as plt
import subprocess, sys
import os

os.chdir(r"E:\temp\reid_section")
file = open("loading_z.txt", "r")
loading_z_str = file.read()
loading_position = int(float(loading_z_str))

file.close()
os.remove("loading_z.txt")

# be careful to make sure that the csv matches to the index
u = pd.read_csv(r'E:\temp\reid_section\analysis.csv', header = 0, usecols = [3, 12,13,14,16,17,18])
u.columns=["Part Instance", "x", "y", "z","U1", "U2", "U3" ]

AF=1
list_of_z_values = np.flip(np.unique(u["z"].values))


def centroid_translation(z,DF):
    df2 = DF.loc[DF["z"]==z]
    NoValue = "ASSEMBLY"  ## remove the loading point
    indexNames = df2[df2["Part Instance"]==NoValue].index

    loading_node = df2.loc[df2["Part Instance"]==NoValue]

    x_a = loading_node["x"].values + loading_node["U1"].values*AF
    y_a = loading_node["y"].values + loading_node["U2"].values*AF
    z_a = loading_node["z"].values + loading_node["U3"].values*AF

    df2.drop(indexNames , inplace=True)
    df2.drop(labels = "Part Instance", axis=1, inplace = True)
    df2 = df2.astype(np.float64)

    x_1 = df2["x"].values + df2["U1"].values*AF
    y_1 = df2["U2"].values*AF
    z_1 = df2["z"].values + df2["U3"].values*AF
    [x_b, y_b, z_b] = [x_1[0],y_1[0],z_1[0]]

    m = (y_b - y_a)/(x_b- x_a)
    c = y_b-m*x_b

    s_c = -c/m
    # find mean column wise
    return float(s_c)
sc = centroid_translation(list_of_z_values[loading_position], u)

print(sc)
