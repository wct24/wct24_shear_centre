import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

"""

comparison of long and short beams with encastre BC
"""

encastre_long = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_15.0\\210.0_81.0_0.3\\encastre")

encastre_short = Load(r"D:\\shear_centre\\1-Semi-Circle\\0.4_0.02_3.0\\210.0_81.0_0.3\\encastre")

fig, ax = plt.subplots()


line1 = encastre_long.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().stress_magnitude_along_beam()
line2 = encastre_short.SimpleTorqueLoad(0, LoadMagnitude = -0.5000001).GetAllWholeBeam().stress_magnitude_along_beam()

max_stress = np.amax(line1[1])

ax.plot(np.array(line1[0])/15.0,np.array(line1[1])/max_stress , label="Dimensionless Bimoment Stresses", color = "deepskyblue", linewidth =3)
# ax[1].plot(np.append(np.array(line2[0]),0)/3.0,np.append(np.array(line2[1]),0.86*max_stress)/max_stress  , label="Dimensionless Axial Stress", color = "deepskyblue")


# print(np.array(line1[0])/15.0)
# ax.set_ylim(bottom=0)
# ax.set_xlim(0,1)
# ax.set_ylabel(r'Dimensionless Warping')

# ax.set_xlabel(r'$z / m$ ', )
# ax.grid()



# #get the warping equation:

# xs = line1[0]
# ys = line1[1]


# def monoExp( z, A, lamb):
#     return A*(np.exp(-z/lamb))
# # perform the fit
# p0 = (max_stress, 2.6) # start with values near those we expect
# params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
# A, lamb = params

# squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
# squaredDiffsFromMean = np.square(ys - np.mean(ys))
# rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# print(f"R² = {rSquared}")
# print(lamb)
# print(A)
# # plot the results



# ax.plot(line1[0]/15.0, monoExp(xs, A, lamb)/max_stress, '--', color="red")





# line1 = encastre_long.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)
# line2 = encastre_short.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)

line1 = encastre_long.SimpleTorqueLoad(0, LoadMagnitude = -0.5).GetAllWholeBeam().warping_magnitude_along_beam()
line2 = encastre_short.SimpleTorqueLoad(0, LoadMagnitude = -0.5000001).GetAllWholeBeam().warping_magnitude_along_beam()

max_warping = np.amax(line1[1])

ax.plot(np.append(np.array(line1[0])/15.0, 0),np.append(np.array(line1[1])/max_warping,0) , color = "darkviolet", label= "Dimensionless Warping Displacements", linewidth =3)
# ax[1].plot(np.array(line2[0])/3.0,np.array(line2[1])/max_warping , color = "darkviolet", label= "Dimensionless Warping")

# ax.plot(line2[0],line2[1] , label="Encastre BC - 5m", color = "palegreen")
# ax.plot(line3[0][200:-1],line3[1][200:-1] , label="Encastre BC - 15m", color = "darkgreen")


ax.set_ylim(0,1)
ax.set_xlim(0,1)
ax.set_ylabel(r'')

ax.set_xlabel(r'$Z / L$ ', )
ax.grid()


# ax[1].set_ylim(bottom=0)
# ax[1].set_xlim(0,1)
# ax[1].set_ylim(0,1)
# ax[1].set_ylabel(r'')

# ax[1].set_xlabel(r'$Z / 3$ ', )
# ax[1].grid()






handles, labels = ax.get_legend_handles_labels()


fig.set_figwidth(6.29921*2)
# fig.set_dpi(300)

plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 20}, ncol=5 )
fig.subplots_adjust(bottom=0.3)



folder_name = r"D:\\report\\figs"+r"\\"+encastre_long.ShapeName+ r"\graph_1"

print(folder_name)
if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_1_3_presentation.png")
# plt.savefig(folder_name+r"\graph_1_3.pgf")








