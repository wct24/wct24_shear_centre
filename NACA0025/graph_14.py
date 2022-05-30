import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *





"""
applying a torque load at the end of the beam and at a position closer to the support

"""
length = 5.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21000.0_0.8_0.3\\warping".format(str(length)))


fig, ax = plt.subplots(1,2)

line1 = warping.SimpleShearLoad(50, -0.06215231880393973, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().z_rotation_along_beam()
line2 = warping.SimpleShearLoad(50, -0.0825, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().z_rotation_along_beam()
line3 = warping.SimpleShearLoad(50, 0.12, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().z_rotation_along_beam()
# line4 = warping.SimpleTorqueLoad(50, LoadMagnitude = -50.1).GetAllWholeBeam().twist_along_beam()

# point_1 = [line1[0][0], line1[1][0]]
# point_2 = [line2[0][15], line2[1][15]]
# point_3 = [line3[0][30], line3[1][30]]
# point_4 = [line4[0][45], line4[1][45]]





ax[0].plot(line1[0],line1[1] , label="$T_z(1.0,0.0,5.0) = 10Nm$")
ax[0].plot(line2[0],line2[1] , label="$T_z(1.0,0.0,4.0) = 10Nm$")
ax[0].plot(line3[0],line3[1] , label="$T_z(1.0,0.0,3.0) = 10Nm$")
# ax[0].plot(line4[0],line4[1] , label="$T_z(1.0,0.0,2.0) = 10Nm$")
# ax[0].scatter(point_1[0],point_1[1])
# ax[0].scatter(point_2[0],point_2[1] )
# ax[0].scatter(point_3[0],point_3[1])
# ax[0].scatter(point_4[0],point_4[1])




# ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,5.05)
ax[0].xaxis.tick_bottom()
ax[0].set_ylabel(r'$\theta_{z}$ / $rad$ ')
ax[0].set_xlabel(r'$Z / m$ ')
ax[0].grid()


line1 = warping.SimpleShearLoad(50, -0.06215231880393973, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().twist_along_beam()
line2 = warping.SimpleShearLoad(50, -0.0825, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().twist_along_beam()
line3 = warping.SimpleShearLoad(50, 0.12, LoadY=0.0, LoadMagnitude = -30).GetAllWholeBeam().twist_along_beam()












# line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -50.1).GetAllWholeBeam().gamma_along_beam()
# line2 = warping.SimpleTorqueLoad(15, LoadMagnitude = -50.1).GetAllWholeBeam().gamma_along_beam()
# line3 = warping.SimpleTorqueLoad(30, LoadMagnitude = -50.1).GetAllWholeBeam().gamma_along_beam()
# line4 = warping.SimpleTorqueLoad(45, LoadMagnitude = -50.1).GetAllWholeBeam().gamma_along_beam()


# point_1 = [line1[0][0], line1[1][0]]
# point_2 = [line2[0][15], line2[1][15]]
# point_3 = [line3[0][30], line3[1][30]]
# point_4 = [line4[0][45], line4[1][45]]


ax[1].plot(line1[0],line1[1] , label=" -0.062")
ax[1].plot(line2[0],line2[1] , label=" -0.0825")
ax[1].plot(line3[0],line3[1] , label="$0.12$")
# ax[1].plot(line4[0],line4[1] , label="$T_z(Z=0.75m)$")

# ax[1].scatter(point_1[0],point_1[1])
# ax[1].scatter(point_2[0],point_2[1])
# ax[1].scatter(point_3[0],point_3[1])
# ax[1].scatter(point_4[0],point_4[1])







# ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,5.05)

# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$Z / m$ ', )
ax[1].set_ylabel(r'$\frac{d\theta_{z}}{dz}$ / $radm^{-1}$ ')
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

plt.savefig(folder_name+r"\graph_2_7.png")
plt.savefig(folder_name+r"\graph_2_7.pgf")
