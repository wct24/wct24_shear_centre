


import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

fig, ax = plt.subplots(2)

line1 = warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()
line2 = warping.SimpleShearLoad(20,1.0).z_rotation_along_beam()
line3 = warping.SimpleShearLoad(40,1.0).z_rotation_along_beam()
line4 = warping.SimpleShearLoad(60,1.0).z_rotation_along_beam()
line5 = warping.SimpleShearLoad(80,1.0).z_rotation_along_beam()


ax[0].plot(line1[0],line1[1] , label="$T_z(1.0,0.0,5.0) = 10Nm$")
ax[0].plot(line2[0],line2[1] , label="$T_z(1.0,0.0,4.0) = 10Nm$")
ax[0].plot(line3[0],line3[1] , label="$T_z(1.0,0.0,3.0) = 10Nm$")
ax[0].plot(line4[0],line4[1] , label="$T_z(1.0,0.0,2.0) = 10Nm$")
ax[0].plot(line5[0],line5[1] , label="$T_z(1.0,0.0,1.0) = 10Nm$")



ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,5.01)
ax[0].xaxis.tick_bottom()
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')
ax[0].grid()



line1 = warping.SimpleShearLoad(0,1.0).warping_magnitude_along_beam()
line2 = warping.SimpleShearLoad(20,1.0).warping_magnitude_along_beam()
line3 = warping.SimpleShearLoad(40,1.0).warping_magnitude_along_beam()
line4 = warping.SimpleShearLoad(60,1.0).warping_magnitude_along_beam()
line5 = warping.SimpleShearLoad(80,1.0).warping_magnitude_along_beam()


ax[1].plot(line1[0],line1[1] , label="$S_y(z=5m)$")
ax[1].plot(line2[0],line2[1] , label="$S_y(z=4m)$")
ax[1].plot(line3[0],line3[1] , label="$S_y(z=3m)$")
ax[1].plot(line4[0],line4[1] , label="$S_y(z=2m)$")
ax[1].plot(line5[0],line5[1] , label="$S_y(z=1m)$")



ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,5.01)

# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$z / m$ ', )
ax[1].set_ylabel(r'Warping Magnitude / $m^4$')
ax[1].grid()




ax[0].get_shared_x_axes().join(ax[0], ax[1])
ax[0].set_xticklabels([])

handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)
# plt.figure(figsize=(8, 6.29921), dpi=300)
plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\plots"+r"\\"+warping.ShapeName+ r"\graph_2"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_2.png")
plt.savefig(folder_name+r"\graph_2.pgf")
