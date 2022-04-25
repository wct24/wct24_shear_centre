import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *


"""
applying a torque load at the end of the beam and at a position closer to the support

"""


warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

# x_array, rotation_array, warping_array = warping.end_rotation_x_sweep( 0, 0, 0, -10)



# fig, ax = plt.subplots()


# x_array0, rotation_array0, warping_array0 = warping.end_rotation_x_sweep( 0, 0, 0, -10)
# # x_array1, rotation_array1, warping_array1 = warping.end_rotation_x_sweep( 0, 0, 0, -1000)


# print(warping_array0)
# print(x_array0*0.1)
# ax[0].plot(x_array0*0.1, rotation_array0*180/np.pi, label="$S_{y}(x,0,0.05) = -10N$")
# # ax[0].plot(x_array1, rotation_array1, label="$S_{y}(x,0,0.05) = -1000N$")
# ax[0].xaxis.tick_bottom()
# ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')
# # ax[0].set_xlabel(r'$x / m$ ', )
# ax[0].grid()

# ax[0].set_yticks([-90,-60,-30,0,30,60,90])
# ax[0].set_ylim(-90, 90)
# ax[0].set_xlim(-10, 10)

# ax[1].plot(x_array0*0.1, warping_array0 , label="$S_{y}(x,0,0.05) = -10N$")
# # ax[0].plot(x_array1, rotation_array1, label="$S_{y}(x,0,0.05) = -1000N$")


# # ax[1].xaxis.tick_bottom()
# ax[1].set_xlabel(r'$x / m$ ', )
# ax[1].set_ylabel(r'Warping Magnitude / $m^4$')
# ax[1].grid()
# ax[1].set_xlim(-10, 10)
# ax[1].set_ylim(bottom=0)

# ax[0].get_shared_x_axes().join(ax[0], ax[1])
# ax[0].set_xticklabels([])

# handles, labels = ax[1].get_legend_handles_labels()


# fig.set_figwidth(6.29921)
# fig.set_dpi(300)
# # plt.figure(figsize=(8, 6.29921), dpi=300)
# plt.tight_layout()
# fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
# fig.subplots_adjust(bottom=0.2)



# folder_name = r"D:\plots"+r"\\"+warping.ShapeName+ r"\graph_5"

# if not os.path.exists(folder_name ):
#     os.makedirs(folder_name)

# plt.savefig(folder_name+r"\graph_5.png")
# plt.savefig(folder_name+r"\graph_5.pgf")







fig, ax = plt.subplots(2)


x_array0, rotation_array0, warping_array0 = warping.end_rotation_x_sweep( 0, 0, 0, -1000)
# x_array1, rotation_array1, warping_array1 = warping.end_rotation_x_sweep( 0, 0, 0, -1000)


# print(warping_array0)
# print(x_array0)
ax[0].plot(x_array0,rotation_array0, label="$S_{y}(x,0,0.05) = -1000N$")
# ax[0].plot(x_array1, rotation_array1, label="$S_{y}(x,0,0.05) = -1000N$")
ax[0].xaxis.tick_bottom()
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')
# ax[0].set_xlabel(r'$x / m$ ', )
ax[0].grid()

ax[0].set_yticks([-90,-60,-30,0,30,60,90])
ax[0].set_ylim(-90, 90)
ax[0].set_xlim(-10, 10)

ax[1].plot(x_array0, warping_array0 , label="$S_{y}(x,0,0.05) = -1000N$")
# ax[0].plot(x_array1, rotation_array1, label="$S_{y}(x,0,0.05) = -1000N$")


# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$x / m$ ', )
ax[1].set_ylabel(r'Warping Magnitude / $m^4$')
ax[1].grid()
ax[1].set_xlim(-10, 10)
ax[1].set_ylim(bottom=0)

ax[0].get_shared_x_axes().join(ax[0], ax[1])
ax[0].set_xticklabels([])

handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)
# plt.figure(figsize=(8, 6.29921), dpi=300)
plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\plots"+r"\\"+warping.ShapeName+ r"\graph_5_2"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_5_2.png")
plt.savefig(folder_name+r"\graph_5_2.pgf")







































# plt.show()
