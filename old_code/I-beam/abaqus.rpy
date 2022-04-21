# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Mon Feb 14 09:57:32 2022
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
execfile('I-beam_script.py', __main__.__dict__)
#: ['Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object']
#: ['Cell object']
#: The section "warping" has been assigned to 199 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/I/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          205
#: Number of Steps:              1
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63898, 
    farPlane=2.90045, width=0.607309, height=0.563098, cameraPosition=(
    -0.0420009, 0.108423, 2.76698), cameraUpVector=(-0.209711, 0.896442, 
    -0.390402), cameraTarget=(-0.01792, -0.0259162, 0.543836))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74744, 
    farPlane=2.79199, width=0.0893984, height=0.0828904, viewOffsetX=0.0346862, 
    viewOffsetY=0.0476122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74859, 
    farPlane=2.79211, width=0.089457, height=0.0829448, cameraPosition=(
    0.0229771, 0.123519, 2.76711), cameraUpVector=(-0.218073, 0.89452, 
    -0.390229), cameraTarget=(-0.0167918, -0.0255135, 0.545133), 
    viewOffsetX=0.0347089, viewOffsetY=0.0476434)
