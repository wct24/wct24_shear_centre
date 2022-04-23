import sys
# # adding Folder_2 to the system path
sys.path.insert(0, r'C:\Users\touze\project\wct24_shear_centre')
from beam_object import *



warping = Beam(r"D:\shear_centre\1-Semi-Circle\0.4_0.02_5.0\210.0_81.0_0.3\Warping")

# fig, ax = plt.subplots()

# line1 = warping.SimpleShearLoad(0,1.0).z_rotation_along_beam()
# line2 = warping.SimpleShearLoad(20,1.0).z_rotation_along_beam()
# line3 = warping.SimpleShearLoad(40,1.0).z_rotation_along_beam()
# line4 = warping.SimpleShearLoad(60,1.0).z_rotation_along_beam()
# line5 = warping.SimpleShearLoad(80,1.0).z_rotation_along_beam()

# """
# applying a shear load at the end of the beam and at a position closer to the support

# """



# plt.plot(line1[0],line1[1] , label="$S_x(1.0,0.0,5.0) = 10N$")
# plt.plot(line2[0],line2[1] , label="$S_x(1.0,0.0,4.0) = 10N$")
# plt.plot(line3[0],line3[1] , label="$S_x(1.0,0.0,3.0) = 10N$")
# plt.plot(line4[0],line4[1] , label="$S_x(1.0,0.0,2.0) = 10N$")
# plt.plot(line5[0],line5[1] , label="$S_x(1.0,0.0,1.0) = 10N$")



# plt.ylim(bottom=0)
# plt.xlim(left=0)
# ax.legend()
# ax.xaxis.tick_bottom()
# plt.xlabel(r'$z / m$ ', )
# plt.ylabel(r'$\theta_{z}$ / \textdegree ')
# plt.tight_layout()
# plt.grid()
# plt.show()




fig, ax = plt.subplots()

line1 = warping.SimpleShearLoad(0,1.0).warping_magnitude_along_beam()
line2 = warping.SimpleShearLoad(20,1.0).warping_magnitude_along_beam()
line3 = warping.SimpleShearLoad(40,1.0).warping_magnitude_along_beam()
line4 = warping.SimpleShearLoad(60,1.0).warping_magnitude_along_beam()
line5 = warping.SimpleShearLoad(80,1.0).warping_magnitude_along_beam()

# """
# applying a shear load at the end of the beam and at a position closer to the support

# """



plt.plot(line1[0],line1[1] , label="$S_x(1.0,0.0,5.0) = 10N$")
plt.plot(line2[0],line2[1] , label="$S_x(1.0,0.0,4.0) = 10N$")
plt.plot(line3[0],line3[1] , label="$S_x(1.0,0.0,3.0) = 10N$")
plt.plot(line4[0],line4[1] , label="$S_x(1.0,0.0,2.0) = 10N$")
plt.plot(line5[0],line5[1] , label="$S_x(1.0,0.0,1.0) = 10N$")



plt.ylim(bottom=0)
plt.xlim(left=0)
ax.legend()
ax.xaxis.tick_bottom()
plt.xlabel(r'$z / m$ ', )
plt.ylabel(r'$\theta_{z}$ / \textdegree ')
plt.tight_layout()
plt.grid()
plt.show()
