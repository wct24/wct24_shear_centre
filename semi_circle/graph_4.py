import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *

"""
applying a torque and seeing the resulting warping plot



 """

warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.04_0.5\\210.0_81.0_0.3\\warping")

# warping.SimpleTorqueLoad(0,LoadMagnitude = -1).GetAllSingleSection(0)

warping.SimpleTorqueLoad(0,LoadMagnitude = -1).GetAllSingleSection(0).plot_warping_function(write_up=True)
warping.SimpleTorqueLoad(0,LoadMagnitude = -1).GetAllSingleSection(0).warping_centre_spread(write_up=True)
