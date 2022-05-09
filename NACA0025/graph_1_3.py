
import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""

encastre_long = Beam(r"D:\\shear_centre\\5-NACA0025\\15.0\\210.0_81.0_0.3\\encastre")

encastre_short = Beam(r"D:\\shear_centre\\5-NACA0025\\5.0\\210.0_81.0_0.3\\encastre")

fig, ax = plt.subplots()


line1 = encastre_long.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)
line2  = encastre_short.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)

ax.plot(np.array(line1[0]),np.array(line1[2]), label="Warping Stress", color = "darkblue")
# ax.plot(np.array(line2[0]),np.array(line2[2]) , label="Warping Stress", color = "darkblue")






print(np.array(line1[0])/15.0)
ax.set_ylim(bottom=0)
# ax.set_xlim(0,1)
ax.set_ylabel(r'Dimensionless Warping')

ax.set_xlabel(r'$z / m$ ', )
ax.grid()



#get the warping equation:

# xs = line1[0]
# ys = line1[2]


# # def monoExp( z, A, lamb):
# #     return A*(np.exp(-z/lamb))
# # # perform the fit
# # p0 = (0.007, 0.7399896433500958) # start with values near those we expect
# # params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
# # A, lamb = params

# # squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
# # squaredDiffsFromMean = np.square(ys - np.mean(ys))
# # rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# # print(f"R² = {rSquared}")
# # print(lamb)
# # print(A)
# # # plot the results



# # ax.plot(line1[0]/15.0, monoExp(xs, A, lamb)/0.07 , '--', color="red")





# line1 = encastre_long.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)
# line2 = encastre_short.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)

# ax.plot(np.array(line1[0])/15.0,np.array(line1[1])/1.5355104886623464e-07, color = "darkblue")
# ax.plot(np.array(line2[0])/5.0,np.array(line2[1])/1.5355104886623464e-07 , color = "darkblue")

# ax.plot(line2[0],line2[1] , label="Encastre BC - 5m", color = "palegreen")
# ax.plot(line3[0][200:-1],line3[1][200:-1] , label="Encastre BC - 15m", color = "darkgreen")


ax.set_ylim(bottom=0)
# ax.set_xlim(0,1)
ax.set_ylabel(r'Dimensionless Warping')

ax.set_xlabel(r'$z / L$ ', )
ax.grid()



#get the warping equation:

xs = line1[0]
ys = line1[1]


def monoExp( z, A, lamb):
    return A*(1-np.exp(-z/lamb))
# perform the fit
p0 = (1.5355104886623464e-07, 2.6) # start with values near those we expect
params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
A, lamb = params

squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
squaredDiffsFromMean = np.square(ys - np.mean(ys))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
print(f"R² = {rSquared}")
print(lamb)
print(A)
# plot the results



# ax.plot(np.array(line1[0])/15.0, monoExp(xs, A, lamb)/1.5355104886623464e-07 , '--', label="Curve Fit", color="red")








handles, labels = ax.get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)

plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\\report\\figs"+r"\\"+encastre_long.ShapeName+ r"\graph_1"

print(folder_name)
if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_1_3.png")
plt.savefig(folder_name+r"\graph_1_3.pgf")








