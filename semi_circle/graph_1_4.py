
import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""


length = 1.0


encastre = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\encastre".format(str(length)))
# warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\warping".format(str(length)))

# fig, ax = plt.subplots(1,2)

# line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam()
line2 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.50001).GetAllWholeBeam()







