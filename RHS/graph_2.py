import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Load(r"D:\\shear_centre\\3-RHS\\0.4_0.02_1.0\\210.0_81.0_0.3\\warping")

J = warping.SimpleTorqueLoad(0, LoadMagnitude = -100).GetAllSingleSection(0).get_J()
print(J)


