#  # s.Line(point1=(0.0, 0.39), point2=(0.0, 0.41))


# import pandas as pd
# import numpy as np
# # be careful to make sure that the csv matches to the index
# u = pd.read_csv('points.csv', header = 0, usecols = [0,1,2,3])
# u.columns=[ "xo", "yo", "xi", "yi" ]
# print(u)
# u = u.astype(np.float64)

# print(u)
# x_i = u["xo"].values
# y_i = u["yo"].values
# x_o = u["xi"].values
# y_o = u["yi"].values




import csv


with open('points.csv') as f:
    x = csv.reader(f)
    data = list(x)
x_o = data[0]
y_o = data[1]
x_i = data[2]
y_i = data[3]

print(x_o)
