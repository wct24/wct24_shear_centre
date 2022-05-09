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
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""

length = 15.0


encastre = Beam(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\encastre".format(str(length)))
warping = Beam(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))

fig, ax = plt.subplots(1,2)

line1 = warping.SimpleTorqueLoad(0,0.0,LoadMagnitude = -0.5).z_rotation_along_beam()
line2 = encastre.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).z_rotation_along_beam()


ax[0].plot(line1[0], line1[1], label="$Warping$", color = "darkblue")
ax[0].plot(line2[0], line2[1] , label="$Encastre$", color = "darkgreen")



ax[0].set_ylim(bottom=0)
ax[0].set_xlim(0,length)
ax[0].set_ylabel(r'$\theta_{z}$ / \textdegree ')

ax[0].set_xlabel(r'$z / m$ ', )
ax[0].grid()


#gradient of line
dy = line1[1][-1]-line1[1][0]
dx = line1[0][-1]-line1[0][0]
m = dy/dx
#ploat a trendline
start_point =2.6810558190871205
ax[0].plot([start_point,15],[0, (15-start_point)*m], "--", color="red")


max_warping = line1[1][0]



# ax[1].plot([2.75,2.75], [0,2.2*10**-5])









line1 = warping.SimpleTorqueLoad(0,0.0,LoadMagnitude = -0.5).warping_magnitude_along_beam()
line2 = encastre.SimpleTorqueLoad(0,0.0, LoadMagnitude = -0.5).warping_magnitude_along_beam(include_stress=True)

#ploat a trendline




ax[1].plot(line1[0],line1[1] , label="Warping BC", color = "darkblue")
ax[1].plot(line2[0],line2[1] , label="Encastre BC", color = "darkgreen")

ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,length)

# ax[1].xaxis.tick_bottom()
ax[1].set_xlabel(r'$z / m$ ', )
ax[1].set_ylabel('$ \overline{|\omega(x,y)|}$ / $m$')
ax[1].grid()


#get the warping equation:

xs = line2[0]
ys = line2[1]


def monoExp( z, A, lamb):
    return A*(1- np.exp(-z/lamb))
# perform the fit
p0 = (3.3e-5, 2.75) # start with values near those we expect
params, cv = scipy.optimize.curve_fit(monoExp, xs, ys, p0)
A, lamb = params
# sampleRate = 20_000 # Hz
# tauSec = (1 / t) / sampleRate

# determine quality of the fit
squaredDiffs = np.square(ys - monoExp(xs, A, lamb))
squaredDiffsFromMean = np.square(ys - np.mean(ys))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
print(f"R² = {rSquared}")
print(lamb)
print(A)
# plot the results

ax[1].plot(xs, monoExp(xs, A, lamb), '--', label="Curve Fit", color="red")



















handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)

plt.tight_layout()
fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\graph_1"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_1_1.png")
plt.savefig(folder_name+r"\graph_1_1.pgf")








