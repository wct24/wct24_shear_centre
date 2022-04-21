from ../beam_object.py import *


Encatre = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\encastre")
Warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

fig, ax = plt.subplots()
print(Encatre.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
print(Warping.SimpleShearLoad(0,1.0).plot_z_rotation_along_beam())
plt.ylim(bottom=0)
plt.xlim(left=0)
ax.legend()
ax.xaxis.tick_bottom()
plt.xlabel(r'$z / m$ ', )
plt.ylabel(r'$\theta_{z}$ / \textdegree ')
plt.tight_layout()
plt.grid()
plt.show()
