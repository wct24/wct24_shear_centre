import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

csv = "E:\\temp\\strip"+ "\\outfile.csv"



u = pd.read_csv(csv, header = 1, usecols = [0,1])
u.columns=["lambda",  "length"]

u = u.astype(np.float64)


E_G = u["lambda"].values**2
E_G = E_G*47

E_G = np.sqrt(E_G)
shed_length = u["length"].values
shed_length = u["length"].values/10
fig,ax = plt.subplots()

ax.plot(E_G,shed_length)

# ax.plot(line2[0],line2[1] , label="Encastre BC - 5m", color = "palegreen")
# ax.plot(line3[0][200:-1],line3[1][200:-1] , label="Encastre BC - 15m", color = "darkgreen")


ax.set_ylim(bottom=0)
ax.set_ylabel('shed rate  $z_{0.01}/L$')

ax.set_xlabel(r'$\sqrt{\frac{E}{G}}$ ', )
ax.grid()
plt.tight_layout()


print(E_G)












# handles, labels = ax[1].get_legend_handles_labels()


# fig.set_figwidth(6.29921)
# fig.set_dpi(300)

# plt.tight_layout()
# fig.legend(handles, labels, loc="lower center", prop={'size': 9}, ncol=5 )
# fig.subplots_adjust(bottom=0.2)



folder_name = r"D:\\report\\figs"+r"\\"+"strip"+ r"\graph_1"

if not os.path.exists(folder_name ):
    os.makedirs(folder_name)


plt.savefig(folder_name+r"\graph_1_1.png")
plt.savefig(folder_name+r"\graph_1_1.pgf")








