# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Tue Mar 15 14:18:57 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.55729, 1.55556), width=229.233, 
    height=154.311)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('NACA0025_script.py', __main__.__dict__)
#: -0.2
#: ['Cell object']
#: [1.0, 0.949999988079071, 0.899999976158142, 0.850000023841858, 0.800000011920929, 0.75, 0.699999988079071, 0.649999976158142, 0.600000023841858, 0.550000011920929, 0.5, 0.449999988079071, 0.400000005960464, 0.349999994039536, 0.300000011920929, 0.25, 0.200000002980232, 0.150000005960464, 0.100000001490116, 0.0500000007450581, 0.0]
#* IndexError: list index out of range
#* File "NACA0025_script.py", line 320, in <module>
#*     main()
#* File "NACA0025_script.py", line 183, in main
#*     loading_z = list_of_z[loading_position]
