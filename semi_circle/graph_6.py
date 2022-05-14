import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Beam(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.04_5.0\\210.0_81.0_0.3\\warping")


# # first get the shear centre
# warping.TSC(0, LoadMagnitude=-10)
# # run the get all for every section
# warping.end_rotation_x_sweep(0, -10)



# warping = Beam(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_15.0\\210.0_81.0_0.3\\warping")

warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAll(0).plot_deformed_cross_section_3D()

warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAll(0).warping_centre_spread()









































# plt.show()
