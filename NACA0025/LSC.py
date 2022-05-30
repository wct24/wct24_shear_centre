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


length = 10.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\encastre".format(str(length)))
line1 = encastre.LSC_every_n_m(0.2)
print(line1)
plt.plot(line1["LoadZ"].values, line1["LoadX"].values)







length = 10.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
line2 = warping.LSC_every_n_m(0.2)

plt.plot(line2["LoadZ"].values, line2["LoadX"].values)



length = 10.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
line3 = warping.SimpleTorqueLoad(0,LoadMagnitude=-1000).GetAllWholeBeam().MeanRCX_along_beam()

plt.plot(line3[0], line3[1])



# length = 5.0
# encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_81.0_0.3\\encastre".format(str(length)))
# encastre.LSC_every_n_m(0.2)



# length = 5.0
# encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\2100.0_81.0_0.3\\encastre".format(str(length)))
# encastre.LSC_every_n_m(0.2)


plt.show()






# warping.SimpleTorqueLoad(0,  LoadMagnitude = -1000)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_210.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(1)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\80.0_90.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(1)

