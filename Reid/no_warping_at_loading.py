import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from Load_object import *

"""
applying a torque and seeing the resulting warping plot



 """

warping = Load(r"D:\\shear_centre\\2-Reid\\1.0\\760.0_270.0_0.3\\warping")


line1 = warping.SimpleShearLoad(0,10.0, LoadMagnitude = -1000).z_rotation_along_beam()

fig,ax = plt.subplots()


ax.plot(line1[0], line1[1])


ax.set_ylim(top=0)
ax.set_xlim(0,1)
ax.set_ylabel(r'$\theta_{z}$ / \textdegree ')

ax.set_xlabel(r'$Z / m$ ' )
ax.grid()






fig.set_figwidth(6.29921)
fig.set_figheight(2.5)
fig.set_dpi(700)

plt.tight_layout()
folder_name = r"D:\\report\\figs"+r"\\"+warping.ShapeName+ r"\graph_1"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_fixed_loading.png")
plt.savefig(folder_name+r"\graph_fixed_loading.pgf")


plt.show()

# print(warping.SimpleTorqueLoad(0,1.0, LoadMagnitude = -4.91)._connected_nodes(0.0398765,0.408056,5))

