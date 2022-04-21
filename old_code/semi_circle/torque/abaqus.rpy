# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Sat Feb 19 19:54:59 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=217.709365844727, 
    height=211.244445800781)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('semi-circle_script.py', __main__.__dict__)
#: 1.0
#: ['Cell object']
#: The section "warping" has been assigned to 102 wires or attachment lines.
#* ipc_CONNECTION_BROKEN
#* File "semi-circle_script.py", line 300, in <module>
#*     main()
#* File "semi-circle_script.py", line 286, in main
#*     myJob.waitForCompletion()
