import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_5.0\\210.0_81.0_0.3\\warping")

# # first get the shear centre
# warping.TSC(0, LoadMagnitude=-10)
# # run the get all for every section
# warping.end_rotation_x_sweep(0, -10)



# warping = Beam(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_15.0\\210.0_81.0_0.3\\warping")

warping.SimpleTorqueLoad(0, LoadMagnitude = -2).GetAllSingleSection(0).plot_warping_function()
warping.SimpleTorqueLoad(0, LoadMagnitude = -2).GetAllSingleSection(0).warping_centre_spread()



# warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllSingleSection(2).warping_centre_spread()



# warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllSingleSection(20).plot_warping_function()

# warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllSingleSection(20).warping_centre_spread()

# warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllSingleSection(99).plot_warping_function()

# warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllSingleSection(99).warping_centre_spread()








































# plt.show()
