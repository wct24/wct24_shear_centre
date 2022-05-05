# import sys
# # # adding Folder_2 to the system path
# sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
# from beam_object import *


# Encatre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
# warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

# fig, ax = plt.subplots(1,2)

# ax[0].plot(Encatre.SimpleShearLoad(0,1.0).z_rotation_along_beam()[0],Encatre.SimpleShearLoad(0,1.0).z_rotation_along_beam()[1] , label="Encastre")
# ax[0].plot(Warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()[0], Warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()[1], label="Warping")


# ax[0].set_ylim(bottom=0)
# ax[0].set_xlim(left=0)
# ax.legend()
# ax.xaxis.tick_bottom()
# plt.xlabel(r'$z / m$ ', )
# plt.ylabel(r'$\theta_{z}$ / \textdegree ')
# plt.tight_layout()
# plt.grid()

# folder_name = r"D:\plots"+r"\\"+ warping.ShapeName+ r"\graph_1"
# if not os.path.exists(folder_name ):
#     os.makedirs(folder_name)












# plt.savefig(folder_name+r"\graph_1.png")
# plt.savefig(folder_name+r"\graph_1.pgf")






import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""

encastre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

fig, ax = plt.subplots(1,2)

line1 = warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()
line2 = encastre.SimpleShearLoad(0,1.0).z_rotation_along_beam()



ax[0].plot(line1[0],line1[1] , label="$Warping$")
ax[0].plot(line2[0],line2[1] , label="$Encastre$")



ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,5.01)
ax[0].xaxis.tick_bottom()
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')
ax[0].grid()



line1 = warping.SimpleShearLoad(0,1.0).warping_magnitude_along_beam()
line2 = encastre.SimpleShearLoad(0,1.0).warping_magnitude_along_beam()


ax[1].plot(line1[0],line1[1] , label="$Warping$")
ax[1].plot(line2[0],line2[1] , label="$Encastre$")

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



folder_name = r"D:\report\figs"+r"\\"+warping.ShapeName+ r"\graph_1"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_1.png")
plt.savefig(folder_name+r"\graph_1.pgf")








