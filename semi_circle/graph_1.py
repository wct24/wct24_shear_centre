import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *


Encatre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
Warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

fig, ax = plt.subplots()

plt.plot(Encatre.SimpleShearLoad(0,1.0).z_rotation_along_beam()[0],Encatre.SimpleShearLoad(0,1.0).z_rotation_along_beam()[1] , label="Encastre")
plt.plot(Warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()[0], Warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()[1], label="Warping")
plt.ylim(bottom=0)
plt.xlim(left=0)
ax.legend()
ax.xaxis.tick_bottom()
plt.xlabel(r'$z / m$ ', )
plt.ylabel(r'$\theta_{z}$ / \textdegree ')
plt.tight_layout()
plt.grid()
plt.show()
