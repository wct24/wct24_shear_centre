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


# warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleShearLoad(0, 1e-5, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleShearLoad(20, 1e-5, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleShearLoad(40, 1e-5, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleShearLoad(60, 1e-5, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleShearLoad(80, 1e-5, LoadMagnitude = -1).GetAllWholeBeam()

warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleTorqueLoad(20, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleTorqueLoad(40,  LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleTorqueLoad(60, LoadMagnitude = -1).GetAllWholeBeam()
warping.SimpleTorqueLoad(80,  LoadMagnitude = -1).GetAllWholeBeam()







# warping.SimpleShearLoad(0, 1e-5, LoadMagnitude = -1).GetAllSingleSection(0).plot_deformed_cross_section_3D()
# warping.SimpleShearLoad(0, 1e-5, LoadMagnitude = -1).GetAllSingleSection(0).warping_centre_spread()



# warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAll(0).warping_centre_line()








































# plt.show()
