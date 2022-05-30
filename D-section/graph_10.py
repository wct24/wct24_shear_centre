import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *





"""
applying a torque load at the end of the beam and at a position closer to the support

"""



warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_3.0\\210.0_81.0_0.3\\warping")

fig, ax = plt.subplots(1,2)

line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAllWholeBeam().z_rotation_along_beam()
line2 = warping.SimpleTorqueLoad(15, LoadMagnitude = -1).GetAllWholeBeam().z_rotation_along_beam()
line3 = warping.SimpleTorqueLoad(30, LoadMagnitude = -1).GetAllWholeBeam().z_rotation_along_beam()
line4 = warping.SimpleTorqueLoad(45, LoadMagnitude = -1).GetAllWholeBeam().z_rotation_along_beam()

point_1 = [line1[0][0], line1[1][0]]
point_2 = [line2[0][15], line2[1][15]]
point_3 = [line3[0][30], line3[1][30]]
point_4 = [line4[0][45], line4[1][45]]





ax[0].plot(line1[0],line1[1] , label="$T_z(1.0,0.0,5.0) = 10Nm$")
ax[0].plot(line2[0],line2[1] , label="$T_z(1.0,0.0,4.0) = 10Nm$")
ax[0].plot(line3[0],line3[1] , label="$T_z(1.0,0.0,3.0) = 10Nm$")
ax[0].plot(line4[0],line4[1] , label="$T_z(1.0,0.0,2.0) = 10Nm$")
ax[0].scatter(point_1[0],point_1[1])
ax[0].scatter(point_2[0],point_2[1] )
ax[0].scatter(point_3[0],point_3[1])
ax[0].scatter(point_4[0],point_4[1])




ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,3.05)
ax[0].xaxis.tick_bottom()
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')
ax[0].set_xlabel(r'$Z / m$ ')
ax[0].grid()



line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAllWholeBeam().warping_magnitude_along_beam()
line2 = warping.SimpleTorqueLoad(15, LoadMagnitude = -1).GetAllWholeBeam().warping_magnitude_along_beam()
line3 = warping.SimpleTorqueLoad(30, LoadMagnitude = -1).GetAllWholeBeam().warping_magnitude_along_beam()
line4 = warping.SimpleTorqueLoad(45, LoadMagnitude = -1).GetAllWholeBeam().warping_magnitude_along_beam()


point_1 = [line1[0][0], line1[1][0]]
point_2 = [line2[0][15], line2[1][15]]
point_3 = [line3[0][30], line3[1][30]]
point_4 = [line4[0][45], line4[1][45]]


ax[1].plot(line1[0],line1[1] , label="$T_z(Z=3m)$")
ax[1].plot(line2[0],line2[1] , label="$T_z(Z=2.25m)$")
ax[1].plot(line3[0],line3[1] , label="$T_z(Z=1.5m)$")
ax[1].plot(line4[0],line4[1] , label="$T_z(Z=0.75m)$")

ax[1].scatter(point_1[0],point_1[1])
ax[1].scatter(point_2[0],point_2[1])
ax[1].scatter(point_3[0],point_3[1])
ax[1].scatter(point_4[0],point_4[1])







ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,3.05)

# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$Z / m$ ', )
ax[1].set_ylabel(r'Warping Magnitude / $m^4$')
ax[1].grid()






handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(500)
# plt.figure(figsize=(8, 6.29921), dpi=300)
plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\plots"+r"\\"+warping.ShapeName+ r"\graph_2"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_2_3.png")
plt.savefig(folder_name+r"\graph_2_3.pgf")
































# plt.show()
