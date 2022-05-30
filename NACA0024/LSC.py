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
warping = Load(r"D:\\shear_centre\\9-NACA0024\\{}\\2100.0_81.0_0.3\\warping".format(str(length)))
warping.LSC_every_n_m(1)

length = 5.0
encastre = Load(r"D:\\shear_centre\\9-NACA0024\\{}\\2100.0_81.0_0.3\\encastre".format(str(length)))
encastre.LSC_every_n_m(1)

length = 5.0
warping = Load(r"D:\\shear_centre\\9-NACA0024\\{}\\80.0_90.0_0.3\\warping".format(str(length)))
warping.LSC_every_n_m(1)

length = 5.0
warping = Load(r"D:\\shear_centre\\9-NACA0024\\{}\\210.0_21.0_0.3\\warping".format(str(length)))
warping.LSC_every_n_m(1)
