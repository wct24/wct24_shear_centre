# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Thu Jan 13 17:02:50 2022
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
execfile('semi-circle_script.py', __main__.__dict__)
#: 0.519999389648
#* IndexError: list index out of range
#* File "semi-circle_script.py", line 277, in <module>
#*     main()
#* File "semi-circle_script.py", line 75, in main
#*     lambda_ =list_of_lambda[lambda_position]
