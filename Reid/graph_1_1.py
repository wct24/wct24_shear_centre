

import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


encastre = Load(r"D:\\shear_centre\\2-Reid\\1.0\\0.760_0.27_0.41\\encastre")
warping  = Load(r"D:\\shear_centre\\2-Reid\\1.0\\0.760_0.27_0.41\\warping")

encastre.TSC_every_n_m(0.1)
encastre.LSC_every_n_m(0.1)

warping.TSC_every_n_m(0.1)
warping.LSC_every_n_m(0.1)









