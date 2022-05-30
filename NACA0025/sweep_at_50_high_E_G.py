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
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21000.0_0.8_0.3\\warping".format(str(length)))

list_x = [-0.04,-0.05,-0.06,-0.07,-0.0825,0.09,0.12,-0.08,-0.15]

for LoadX in list_x:
    warping.SimpleShearLoad(50, LoadX, LoadMagnitude = -30).GetAllWholeBeam()


