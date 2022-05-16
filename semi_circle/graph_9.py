import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.04_1.0\\210.0_81.0_0.3\\warping")

# # first get the shear centre
# warping.TSC(0, LoadMagnitude=-10)
# # run the get all for every section
# warping.end_rotation_x_sweep(0, -10)



# warping = Beam(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_15.0\\210.0_81.0_0.3\\warping")

# warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllWholeBeam()

# warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllSingleSection(0).plot_warping_function()
# warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllSingleSection(0).plot_warping_function()
warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllSingleSection(0).warping_centre_spread()
warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllSingleSection(19).warping_centre_spread()


# warping.SimpleTorqueLoad(10, LoadMagnitude = -1).GetAllSingleSection(i).warping_centre_spread()




# [[-1.00511691e-07]
#  [-4.12026625e-07]
#  [-7.18666575e-07]
#  [-1.01697619e-06]
#  [-1.30352954e-06]
#  [-1.57494763e-06]
#  [-1.82790575e-06]
#  [-2.05915413e-06]
#  [-2.26551600e-06]
#  [-2.44392925e-06]
#  [-2.59142313e-06]
#  [-2.70518175e-06]
#  [-2.78249900e-06]
#  [-2.82088425e-06]
#  [-2.81796975e-06]
#  [-2.77167800e-06]
#  [-2.68005425e-06]
#  [-2.54153588e-06]
#  [-2.35463525e-06]
#  [-2.11839469e-06]
#  [-1.83181561e-06]
#  [-1.49461525e-06]
#  [-1.10624810e-06]
#  [-6.67183513e-07]
#  [-1.77211110e-07]
#  [ 3.62339309e-07]
#  [ 9.51548279e-07]
#  [ 1.58800653e-06]
#  [ 2.27210330e-06]
#  [ 2.99992888e-06]
#  [ 3.77253087e-06]
#  [ 4.58553075e-06]
#  [ 5.43912062e-06]]
































# plt.show()
