# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Tue Mar  8 08:30:36 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=217.709365844727, 
    height=255.733337402344)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('c_section_script.py', __main__.__dict__)
#: ['Cell object']
#: The section "warping" has been assigned to 723 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/c_section/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          729
#: Number of Steps:              1
