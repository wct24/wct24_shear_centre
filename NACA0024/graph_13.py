import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


length = 3.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21000.0_0.8_0.3\\warping".format(str(length)))
warping.SimpleTorqueLoad(30, LoadMagnitude =  -50).GetAllSingleSection(31).plot_deflected_section()
