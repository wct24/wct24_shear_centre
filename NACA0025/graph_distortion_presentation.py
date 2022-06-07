import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

from matplotlib.ticker import LogLocator, NullFormatter
length = 5.0
encastre = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\encastre".format(str(length)))
line1 = encastre.SimpleTorqueLoad(0,LoadMagnitude=-1000).GetAllWholeBeam().distorsion_along_beam(0)





length = 5.0
warping = Load(r"D:\\shear_centre\\5-NACA0025\\{}\\210.0_81.0_0.3\\warping".format(str(length)))
line2 = warping.SimpleTorqueLoad(0,LoadMagnitude=-1000).GetAllWholeBeam().distorsion_along_beam(0)





fig,ax = plt.subplots()


ax.plot(line1.index[1:], line1["above"].values[1:] + line1["bellow"].values[1:], label =  "Distorsion between load and free-end", linewidth=2)
# ax.plot(line1.index[1:], , label = "Distorsion between load and BC", linewidth=2)
# ax[1].plot(line2.index[1:], line2["above"].values[1:], label =  "Distorsion between load and free-end", linewidth=2)
# ax[1].plot(line2.index[1:], line2["bellow"].values[1:], label = "Distorsion between load and BC", linewidth=2)







handles, labels = ax.get_legend_handles_labels()


ax.set_xlabel(r'Load Position / m ',  fontsize=20)
ax.set_ylabel('Distorsion',  fontsize=20)
ax.grid()

# ax[1].set_xlabel(r'$LoadZ / m$ ', )
# ax[1].set_ylabel('Distorsion')
# ax[1].grid()



ax.set_yscale('log')
# ax[1].set_yscale('log')

# ax[0].LogLocator(base=10.0, subs=[1.0], numdecs=4, numticks=15)
ax.locator_params(axis="x", nbins=6)
# ax[1].locator_params(axis="x", nbins=6)

# ax[1].set_locator_params(axis='y', nbins=3)



# ax[0].yaxis.set_major_locator(LogLocator(base = 10, subs=[1.0], numdecs=4, numticks=15))
# ax[1].yaxis.set_major_locator(LogLocator(base = 10, subs=[1.0], numdecs=4, numticks=15))



y_major = LogLocator(base = 10.0, numticks = 6)
ax.yaxis.set_major_locator(y_major)
y_minor =LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 10)
ax.yaxis.set_minor_locator(y_minor)
ax.yaxis.set_minor_formatter(NullFormatter())



# y_major =LogLocator(base = 10.0, numticks = 5)
# ax[1].yaxis.set_major_locator(y_major)
# y_minor = LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 10)
# ax[1].yaxis.set_minor_locator(y_minor)
# ax[1].yaxis.set_minor_formatter(NullFormatter())






plt.tight_layout()

# fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
fig.subplots_adjust(bottom=0.3)

fig.set_figwidth(6.29921)
fig.set_figheight(3)

# fig.set_dpi(500)




folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\LSC"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_distortion_presentation.png")
# plt.savefig(folder_name+r"\graph_distortion.pgf")














