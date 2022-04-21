# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Mon Mar 14 18:27:41 2022
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
execfile('semi-circle_script.py', __main__.__dict__)
#: ['Cell object']
#: The section "warping" has been assigned to 390 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/SC/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          397
#: Number of Steps:              1
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
o3 = session.openOdb(name='E:/temp/SC/analysis.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/temp/SC/analysis.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=9.14624, 
    farPlane=13.9431, width=5.39148, height=2.50963, cameraPosition=(5.9055, 
    -7.71562, 8.50548), cameraUpVector=(0.614556, 0.73883, -0.276497), 
    cameraTarget=(0.168123, -0.0656927, 2.72267))
session.viewports['Viewport: 1'].view.setValues(nearPlane=9.1336, 
    farPlane=13.9557, width=5.38403, height=2.50617, cameraPosition=(5.9055, 
    -7.71562, 8.50548), cameraUpVector=(0.520966, 0.852952, -0.0326743), 
    cameraTarget=(0.168123, -0.0656925, 2.72267))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.55381, 
    farPlane=14.4387, width=5.04226, height=2.34708, cameraPosition=(5.07935, 
    -3.37981, -7.1915), cameraUpVector=(0.618515, 0.608637, 0.496991), 
    cameraTarget=(0.141666, 0.0731604, 2.21998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=9.56881, 
    farPlane=13.4355, width=5.64058, height=2.62559, cameraPosition=(-7.37154, 
    8.25753, -1.0392), cameraUpVector=(0.774421, 0.433327, 0.460976), 
    cameraTarget=(-0.206284, 0.398375, 2.39191))
session.viewports['Viewport: 1'].view.setValues(nearPlane=9.01512, 
    farPlane=13.9956, width=5.3142, height=2.47366, cameraPosition=(-7.47073, 
    6.0734, 8.93943), cameraUpVector=(0.695992, 0.622464, -0.357959), 
    cameraTarget=(-0.209106, 0.336246, 2.67576))
session.viewports['Viewport: 1'].view.setValues(nearPlane=10.0234, 
    farPlane=13.0442, width=5.90856, height=2.75033, cameraPosition=(-9.77757, 
    6.00016, 0.867922), cameraUpVector=(0.77661, 0.626442, -0.0666802), 
    cameraTarget=(-0.275355, 0.334142, 2.44396))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.53686, 
    farPlane=14.5707, width=5.03228, height=2.34244, cameraPosition=(-4.37506, 
    1.70341, -8.05151), cameraUpVector=(0.609432, 0.761134, 0.221963), 
    cameraTarget=(-0.10727, 0.200459, 2.16645))
session.viewports['Viewport: 1'].view.setValues(nearPlane=8.58494, 
    farPlane=14.5244, width=5.06064, height=2.35563, cameraPosition=(-3.63564, 
    1.22974, -8.38816), cameraUpVector=(0.587265, 0.775357, 0.232252), 
    cameraTarget=(-0.0830246, 0.184928, 2.15541))
