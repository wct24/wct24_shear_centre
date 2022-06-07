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


length = 5.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\encastre".format(str(length)))
line1 = encastre.LSC_every_n_m(0.2)
plt.plot(line1["LoadZ"].values, line1["LoadX"].values)




length = 5.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_81.0_0.3\\encastre".format(str(length)))
line2 = encastre.LSC_every_n_m(0.2)
plt.plot(line2["LoadZ"].values, line2["LoadX"].values)




length = 5.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\2100.0_81.0_0.3\\encastre".format(str(length)))
encastre.LSC_every_n_m(0.2)
line3 = encastre.LSC_every_n_m(0.2)
plt.plot(line3["LoadZ"].values, line3["LoadX"].values)




length = 5.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
line5 = warping.SimpleTorqueLoad(0,LoadMagnitude=-1000).GetAllWholeBeam().MeanRCX_along_beam()







# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
# line2 = warping.LSC_every_n_m(0.2)

# plt.plot(line2["LoadZ"].values, line2["LoadX"].values)



# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
# line3 = warping.SimpleTorqueLoad(0,LoadMagnitude=-1000).GetAllWholeBeam().MeanRCX_along_beam()

# plt.plot(line3[0], line3[1])







fig,ax = plt.subplots()


# ax.plot(line1.index, (line1["MeanRCX"].values-line5[1][3])*100, label =  "Torque Encastre BC", linewidth=5, linestyle='dashed')

# ax.plot(line2.index, (line2["MeanRCX"].values-line5[1][3])*100, label =   "Torque Warping BC", linewidth=5, linestyle='dashed')


ax.plot(line1["LoadZ"].values, (line1["LoadX"].values-line5[1][3])*100, label =   "$E = 210 GPa$, $G = 81 GPa$", linewidth=2, c="g")

ax.plot(line2["LoadZ"].values, (line2["LoadX"].values-line5[1][3])*100, label =  "$E = 21 GPa$, $G = 81 GPa$", linewidth=2, c="m")

ax.plot(line3["LoadZ"].values, (line3["LoadX"].values-line5[1][3])*100, label =   "$E = 2100 GPa$, $G = 81 GPa$", linewidth=2, c="c")

# ax.plot(line4["LoadZ"].values, (line4["LoadX"].values-line5[1][3])*100, label =  "Shear Warping BC", linewidth=2)




# ax.plot(line5[0], line5[1]-line5[1])







handles, labels = ax.get_legend_handles_labels()


ax.set_xlabel(r'$Z / m$ ', )
ax.set_ylabel('$\mu$ / \%')
ax.grid()

ax.set_ylim(top=0)

plt.tight_layout()

fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.3)

fig.set_figwidth(6.29921)
fig.set_figheight(3)

# fig.set_dpi(300)




folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\LSC"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_LSC_material.png")
plt.savefig(folder_name+r"\graph_LSC_material.pgf")






















# plt.show()






# warping.SimpleTorqueLoad(0,  LoadMagnitude = -1000)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\21.0_210.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(1)

# length = 5.0
# warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\80.0_90.0_0.3\\warping".format(str(length)))
# warping.LSC_every_n_m(1)

