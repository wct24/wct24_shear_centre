# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Mon Jan 31 10:19:42 2022
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
execfile('box_script.py', __main__.__dict__)
#: ['Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object']
#: ['Cell object']
#: The section "warping" has been assigned to 1170 wires or attachment lines.
#: Model: E:/temp/box/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          1176
#: Number of Steps:              1
print 'RT script done'
#: RT script done
