import subprocess
import smtplib, ssl
import pandas as pd
import os
import time
import numpy as np
from transforms3d.euler import mat2euler
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from decimal import Decimal



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(np.array([[1,2,],[1,2]]),np.array([[1,1],[0,0]]), np.array([[0.0,0.0],[0.0,0.0]]),cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.show()


r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)
print(r)

#https://matplotlib.org/3.3.1/gallery/mplot3d/contour3d_3.html
