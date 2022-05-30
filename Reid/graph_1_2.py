
import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *


encastre = Load(r"D:\\shear_centre\\2-Reid\\0.84\\760.0_270.0_0.41\\encastre")


warping1  = Load(r"D:\\shear_centre\\2-Reid\\0.84\\760.0_270.0_0.41\\warping")

line1 = warping1.LSC(0).GetAllWholeBeam().twist_along_beam()


warping2  = Load(r"D:\\shear_centre\\2-Reid\\0.84\\76.0_270.0_0.41\\warping")

line2 = warping2.LSC(0).GetAllWholeBeam().twist_along_beam()


warping3  = Load(r"D:\\shear_centre\\2-Reid\\0.84\\760.0_27.0_0.41\\warping")

line3 = warping3.LSC(0).GetAllWholeBeam().twist_along_beam()

warping4  = Load(r"D:\\shear_centre\\2-Reid\\0.84\\7600.0_27.0_0.41\\warping")

line4 = warping4.LSC(0).GetAllWholeBeam().twist_along_beam()



fig, ax = plt.subplots()

ax.plot(line1[0],line1[1], label="760 270")
ax.plot(line2[0],line2[1], label= "76 270")
ax.plot(line3[0],line3[1], label= "760 27")
ax.plot(line4[0],line4[1], label= "7600 27")
plt.legend()
plt.show()
