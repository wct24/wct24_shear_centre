import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""



warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_3.0\\210.0_81.0_0.3\\warping")


warping.SimpleTorqueLoad(30, LoadMagnitude = -1.1).GetAllSingleSection(1).warping_centre_spread(write_up=True)



































# plt.show()
