# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Wed May 18 11:24:07 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=217.709365844727, 
    height=231.466674804688)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('strip_script.py', __main__.__dict__)
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
#: Model: E:/temp/strip/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       2
#: Number of Node Sets:          2
#: Number of Steps:              1
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=17.3338, 
    farPlane=26.5203, width=6.9599, height=7.15821, viewOffsetX=0.181688, 
    viewOffsetY=-0.795593)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/temp/strip/Job-1.odb'])
o3 = session.openOdb(name='E:/temp/strip/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=16.7439, 
    farPlane=27.3716, width=7.8985, height=8.12355, viewOffsetX=0.190593, 
    viewOffsetY=-0.342713)
session.viewports['Viewport: 1'].view.setValues(width=7.8517, height=8.07542, 
    cameraPosition=(0.0802139, -0.667063, 27.4182), cameraUpVector=(0, 1, 0), 
    cameraTarget=(0.0802139, -0.667063, 5.36048), viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(22.1379, 
    -0.667063, 5.36048))
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.4862, 
    farPlane=24.0723, width=22.6413, height=9.43866, viewOffsetX=-0.302562, 
    viewOffsetY=-0.169456)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3986, 
    farPlane=24.1598, width=22.5396, height=9.39625, cameraPosition=(22.1379, 
    -1.03067, 6.04488), cameraUpVector=(0, -0.999016, 0.0443605), 
    cameraTarget=(0.0802139, -1.03067, 6.04488), viewOffsetX=-0.301203, 
    viewOffsetY=-0.168694)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.2649, 
    farPlane=23.2935, width=10.5338, height=4.39129, viewOffsetX=-2.35904, 
    viewOffsetY=-1.05283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.3121, 
    farPlane=23.2464, width=10.5583, height=4.40151, cameraPosition=(22.1379, 
    -1.0969, 6.01779), cameraUpVector=(0, -0.999827, 0.0186004), cameraTarget=(
    0.0802139, -1.0969, 6.01779), viewOffsetX=-2.36453, viewOffsetY=-1.05528)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.314, 
    farPlane=23.2444, width=9.92575, height=4.13782, viewOffsetX=-2.80034, 
    viewOffsetY=-0.906055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=19.996, 
    farPlane=23.6145, width=9.77036, height=4.07304, cameraPosition=(21.9539, 
    3.57051, 4.96335), cameraUpVector=(0.211293, -0.976714, 0.0372089), 
    cameraTarget=(0.412299, -1.04841, 6.04434), viewOffsetX=-2.7565, 
    viewOffsetY=-0.891871)
