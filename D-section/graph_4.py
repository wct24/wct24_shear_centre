import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *

"""
applying a torque and seeing the resulting warping plot



 """

warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

warping.SimpleTorqueLoad(0,1.0, LoadMagnitude = -4.91).plot_deformed_cross_section_3D_combind(1)
# print(warping.SimpleTorqueLoad(0,1.0, LoadMagnitude = -4.91)._connected_nodes(0.0398765,0.408056,5))

















































# plt.plot(line1[0],line1[1] , label="$T_z(1.0,0.0,5.0) = 10Nm$")
# plt.plot(line2[0],line2[1] , label="$T_z(1.0,0.0,4.0) = 10Nm$")
# plt.plot(line3[0],line3[1] , label="$T_z(1.0,0.0,3.0) = 10Nm$")
# plt.plot(line4[0],line4[1] , label="$T_z(1.0,0.0,2.0) = 10Nm$")
# plt.plot(line5[0],line5[1] , label="$T_z(1.0,0.0,1.0) = 10Nm$")

# plt.ylim(bottom=0)
# plt.xlim(left=0)
# ax.legend()
# ax.xaxis.tick_bottom()
# plt.xlabel(r'$z / m$ ', )
# plt.ylabel(r'$\theta_{z}$ / \textdegree ')
# plt.tight_layout()
# plt.grid()
# plt.show()
