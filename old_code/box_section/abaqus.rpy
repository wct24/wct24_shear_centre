# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Sun Jan 30 21:09:17 2022
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
execfile('box_script.py', __main__.__dict__)
#: ['Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object']
#: ['Cell object']
#: The section "warping" has been assigned to 2304 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/box/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          6
#: Number of Steps:              1
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/temp/box/analysis.odb'])
o3 = session.openOdb(name='E:/temp/box/analysis.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S33'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.44415, 
    farPlane=9.58959, width=2.29312, height=2.12619, cameraPosition=(-0.274526, 
    1.05001, 8.94491), cameraUpVector=(-0.202217, 0.854455, -0.478555), 
    cameraTarget=(-0.0222768, -0.0981978, 1.6226))
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.53111, 
    farPlane=9.52831, width=2.32975, height=2.16015, cameraPosition=(0.267725, 
    0.125081, 9.03069), cameraUpVector=(-0.231259, 0.906298, -0.353755), 
    cameraTarget=(-0.015006, -0.1106, 1.62375))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.40107, 
    -0.1106, 1.62375), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.015006, 
    -0.1106, 9.03983))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=NONUNIFORM, nonuniformScaleFactor=(0, 0, 10000000))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(0, 0, 1E+06))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.4905, 
    farPlane=33.0812, width=1.78837, height=1.65818, cameraPosition=(0.151561, 
    -0.706642, 32.5422), cameraUpVector=(0.0194206, 0.99955, 0.0228538), 
    cameraTarget=(0.00381448, -0.0177847, 2.53947))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.506, 
    farPlane=33.0657, width=1.78934, height=1.65908, cameraPosition=(15.423, 
    -0.682122, 28.4), cameraUpVector=(-0.0478643, 0.997433, 0.0532598), 
    cameraTarget=(0.388166, -0.0171676, 2.43522))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.4871, 
    farPlane=32.0844, width=1.85093, height=1.71618, cameraPosition=(29.9157, 
    -0.8794, -5.44921), cameraUpVector=(0.0675967, 0.984756, 0.160271), 
    cameraTarget=(0.752916, -0.0221327, 1.58331))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.4023, 
    farPlane=33.1693, width=1.78284, height=1.65305, cameraPosition=(3.41163, 
    3.01447, -28.6824), cameraUpVector=(0.11903, 0.986664, 0.111023), 
    cameraTarget=(0.0858649, 0.0758677, 0.99858))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.441, 
    farPlane=33.1305, width=1.78527, height=1.6553, cameraPosition=(-2.19425, 
    16.191, -24.3272), cameraUpVector=(0.380166, 0.799887, 0.464386), 
    cameraTarget=(-0.0552228, 0.407493, 1.10819))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.5457, 
    farPlane=33.0257, width=1.79184, height=1.6614, cameraPosition=(19.0492, 
    5.16424, -21.8618), cameraUpVector=(0.3202, 0.838244, 0.441384), 
    cameraTarget=(0.479428, 0.129973, 1.17024))
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.7618, 
    farPlane=31.8097, width=1.86818, height=1.73218, cameraPosition=(30.3608, 
    -4.89413, 0.339996), cameraUpVector=(0.161091, 0.856629, 0.490139), 
    cameraTarget=(0.764116, -0.123173, 1.72901))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.3798, 
    farPlane=33.1917, width=1.78143, height=1.65174, cameraPosition=(-3.70354, 
    -4.32078, 32.02), cameraUpVector=(-0.19681, 0.973679, 0.114961), 
    cameraTarget=(-0.0932101, -0.108743, 2.52633))
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.4647, 
    farPlane=33.1066, width=1.78676, height=1.65669, cameraPosition=(0.321234, 
    2.25606, 32.4661), cameraUpVector=(-0.2666, 0.961416, -0.0678593), 
    cameraTarget=(0.00808455, 0.0567814, 2.53756))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00808455, 
    30.0677, 2.53756), cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(30.019, 
    0.0567814, 2.53756), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.00808455, 
    0.0567814, 32.5485))
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
