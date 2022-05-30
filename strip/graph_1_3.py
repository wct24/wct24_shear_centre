
import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""

warping = Load(r"D:\\shear_centre\\8-Strip\\5.0_5.0_5.0\\1.0_1.0_0.3\\warping")

warping.SimpleTorqueLoad(0,LoadMagnitude=-0.5).GetAllSingleSection(0).plot_warping_function()








