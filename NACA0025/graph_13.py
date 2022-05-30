import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


length = 3.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\encastre".format(str(length)))
encastre.SimpleTorqueLoad(0, LoadMagnitude =  -10001).GetAllSingleSection(50).plot_deflected_section(name="w_off")






length = 3.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))




warping.SimpleTorqueLoad(0, LoadMagnitude =  -10001).GetAllSingleSection(50).plot_deflected_section(name="w_on")






# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
# warping.SimpleTorqueLoad(0, LoadMagnitude =  -10000).GetAllSingleSection(80).plot_deflected_section()
