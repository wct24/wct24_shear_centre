import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *
import scipy.optimize

"""
applying a torque load at the end of the beam and at a position closer to the support

"""
fig,ax = plt.subplots(1,2)

def f1(x):
    return np.e**-(x/2.68)


xs1 = np.linspace(0,3,100)
ys1 = f1(xs1)

ax[0].plot(xs1/3,ys1, color ="green")



def f2(x):
    return -np.e**(-3/2.68)*np.e**((x-3)/2.68)


xs2 = np.linspace(0,3,100)
ys2 = f2(xs2)

ax[0].plot(xs2/3,ys2,  color="red")






ax[0].plot(xs2/3,ys2+ys1, color = "deepskyblue")


# ax[0].arrow(xs1[-1]/3,ys1[-1], 0,-2*ys1[-1] )


ax[0].set_ylabel("Normalised Axial Stress")

# # ax[0].set_ylim(0,1)
ax[0].set_xlim(0,1)
# ax[0].set_ylabel(r'')

ax[0].set_xlabel(r'$Z / 3$ ', )
ax[0].grid()


ax[1].set_ylim(bottom=0)
ax[1].set_xlim(0,1)
ax[1].set_ylim(0,1)
ax[1].set_ylabel(r'')

ax[1].set_xlabel(r'$Z / 3$ ', )
ax[1].grid()


























# handles, labels = ax[1].get_legend_handles_labels()


fig.set_figwidth(6.29921)
fig.set_dpi(300)

plt.tight_layout()
# # fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
# fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\\report\\figs"+r"\\"+"1-Semi-Circle"+ r"\graph_1"

print(folder_name)
if not os.path.exists(folder_name ):
    os.makedirs(folder_name)

plt.savefig(folder_name+r"\graph_1_3_2.png")
plt.savefig(folder_name+r"\graph_1_3_2.pgf")








