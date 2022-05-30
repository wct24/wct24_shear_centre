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
from Load_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""


length = 3.0


encastre = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\encastre".format(str(length)))
warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\warping".format(str(length)))
encastre_long = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_15.0\\210.0_81.0_0.3\\encastre")

fig, ax = plt.subplots(1,2)

# line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam()


line1 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.5000001).GetAllWholeBeam().z_rotation_along_beam()
line2 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5000001).GetAllWholeBeam().z_rotation_along_beam()
line3 = encastre_long.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().z_rotation_along_beam()




ax[0].plot(np.append(line1[0],0),np.append(line1[1],0) , label="Warping BC", color = "orange")
ax[0].plot(np.append(line2[0],0),np.append(line2[1],0) , label="Encastre BC - 5m", color = "darkgreen")
ax[0].plot(np.append(line3[0][240:-1],0),np.append(line3[1][240:-1],0) , label="Encastre BC - 15m", color = "darkblue")

# print(line3[0])
ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,length)
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')

ax[0].set_xlabel(r'$z / m$ ', )
ax[0].grid()




dy = line3[1][-1]-line3[1][0]
dx = line3[0][-1]-line3[0][0]
m = dy/dx
print(m)
#ploat a trendline
start_point =2.6810558190871205
ax[0].plot([start_point,15],[0, (15-start_point)*m], "-.", color="red")







# #gradient of line
# dy = line1[1][-1]-line1[1][0]
# dx = line1[0][-1]-line1[0][0]
# m = dy/dx
# #ploat a trendline
# start_point =2.6810558190871205
# ax[0].plot([start_point,15],[0, (15-start_point)*m], "--", color="red")


# max_warping = line1[1][0]



# # ax[1].plot([2.75,2.75], [0,2.2*10**-5])


# line1 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.500001).GetAllWholeBeam().warping_magnitude_along_beam()
# line2 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.500001).GetAllWholeBeam().warping_magnitude_along_beam()
# line3 = encastre_long.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().warping_magnitude_along_beam()



line1 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.5000001).GetAllWholeBeam().warping_magnitude_along_beam()
line2 = warping.SimpleTorqueLoad(0, LoadMagnitude =-0.5000001).GetAllWholeBeam().warping_magnitude_along_beam()
line3 = encastre_long.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().warping_magnitude_along_beam()



ax[1].plot(np.append(line1[0],0),np.append(line1[1],0) , label="Encastre BC", color = "orange")
ax[1].plot(line2[0],line2[1] , label="Warping BC ", color = "darkgreen")
ax[1].plot(np.append(line3[0][240:-1],0),np.append(line3[1][240:-1],0)  , label="Encastre BC - 15m", color = "darkblue")


ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,length+0.05)

# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$z / m$ ', )
ax[1].set_ylabel('W / $m$')
ax[1].grid()



#gradient of line

# max_warping = line1[1][0]

# #gradient of line
# dy = line2[1][-1]-line2[1][0]
# dx = line2[0][-1]-line2[0][0]
# m = dy/dx
# #ploat a trendline
# start_point =2.6810558190871205
# ax[0].plot([start_point,15],[0, (15-start_point)*m], "-.", color="red")






# # #get the warping equation:

# # xs = line2[0]
# # ys = line2[1]


# # def monoExp( z, A, lamb):
# #     return A*(1- np.exp(-z/lamb))
# # # perform the fit
# # p0 = (3.3e-5, 2.75) # start with values near those we expect
# # params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
# # A, lamb = params
# # # sampleRate = 20_000 # Hz
# # # tauSec = (1 / t) / sampleRate

# # # determine quality of the fit
# # squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
# # squaredDiffsFromMean = np.square(ys - np.mean(ys))
# # rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# # print(f"R² = {rSquared}")
# # print(lamb)
# # print(A)
# # # plot the results

# # lamb = 2.6810558190871205
# # # A = 3.283613e-05

# # ax[1].plot(xs, monoExp(xs, A, lamb), '--', label="Curve Fit", color="red")



















handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)

plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\graph_1"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_1_2.png")
plt.savefig(folder_name+r"\graph_1_2.pgf")













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






# import sys
# # # adding Folder_2 to the system path
# sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
# from Load_object import *
# import scipy.optimize

# """
# applying a torque load at the end of the beam and at a position closer to the support

# """

# length = 3.0


# encastre = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\encastre".format(str(length)))
# warping = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_{}\\210.0_81.0_0.3\\warping".format(str(length)))

# fig, ax = plt.subplots(1,2)

# # line1 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam()
# line1 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().z_rotation_along_beam()
# line2 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().z_rotation_along_beam()



# # warping_2 = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_0.5\\210.0_81.0_0.3\\warping")
# # J = warping_2.SimpleTorqueLoad(0, LoadMagnitude = -1).GetAllSingleSection(0).get_J()
# # print(J)




# ax[0].plot(line1[0], line1[1], label="$Warping$", color = "darkblue")
# ax[0].plot(line2[0], line2[1] , label="$Encastre$", color = "darkgreen")



# ax[0].set_ylim(bottom=0)
# ax[0].set_xlim(0,length)
# ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')

# ax[0].set_xlabel(r'$z / m$ ', )
# ax[0].grid()


# #gradient of line
# dy = line2[1][-1]-line2[1][0]
# dx = line2[0][-1]-line2[0][0]
# m = dy/dx
# #ploat a trendline
# start_point =2.6810558190871205
# ax[0].plot([start_point,15],[0, (15-start_point)*m], "-.", color="red")

# max_warping = line1[1][0]



# # ax[1].plot([2.75,2.75], [0,2.2*10**-5])



# line1 = encastre.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().warping_magnitude_along_beam()
# line2 = warping.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().warping_magnitude_along_beam()
# # #ploat a trendline




# ax[1].plot(line1[0],line1[1] , label="Encastre BC", color = "darkblue", linewidth = 4)
# ax[1].plot(line2[0],line2[1] , label="Warping BC", color = "darkgreen")

# ax[1].set_ylim(bottom=0)
# ax[1].set_xlim(0,length)

# ax[1].xaxis.tick_bottom()
# ax[1].set_xlabel(r'$z / m$ ', )
# ax[1].set_ylabel('Warping Magnitude / $m$')
# ax[1].grid()


# #get the warping equation:

# xs = np.array(line1[0])
# ys = np.array(line1[1])


# def monoExp( z, A, lamb):
#     return A*(1- np.exp(-z/lamb))
# # perform the fit
# p0 = (3.3e-5, 2.75) # start with values near those we expect
# params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)

# print(params)
# A = params[0]
# lamb = params[1]
# # A, lamb = params
# # sampleRate = 20_000 # Hz
# # tauSec = (1 / t) / sampleRate

# # determine quality of the fit
# # squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
# # squaredDiffsFromMean = np.square(ys - np.mean(ys))
# # rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# # print(f"R² = {rSquared}")
# # print(lamb)
# # print(A)
# # plot the results

# ax[1].plot(xs, monoExp(xs, A, lamb), '-.', label="Curve Fit", color="red")

# handles, labels = ax[1].get_legend_handles_labels()


# plt.tight_layout()
# fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
# fig.subplots_adjust(bottom=0.2)

# fig.set_figwidth(6.29921)
# fig.set_dpi(700)

# folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\graph_1"

# if not os.path.exists(folder_name ):
#     os.makedirs(folder_name)


# plt.savefig(folder_name+r"\graph_1_1.png")
# plt.savefig(folder_name+r"\graph_1_1.pgf")









