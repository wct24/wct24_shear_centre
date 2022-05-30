import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""

# length = 2.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_81.0_0.3\\warping".format(str(length)))

# warping.LSC_every_n_m(0.5)


length = 5.0
warping = Load(r"D:\\shear_centre\\2-Reid\\1.0\\760.0_27.0_0.41\\warping")
warping.LSC_every_n_m(0.5)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_210.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(0.5)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\80.0_90.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(0.5)

