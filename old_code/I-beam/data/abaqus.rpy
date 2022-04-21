# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Fri Jan 14 00:17:24 2022
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
#: ['Cell object']
#: The section "warping" has been assigned to 135 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/I/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       3
#: Number of Node Sets:          141
#: Number of Steps:              1
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.86781, 
    farPlane=4.49686, width=3.7494, height=1.34576, cameraPosition=(0.152477, 
    -0.225107, 4.17256), cameraUpVector=(0.213245, 0.931419, -0.294931), 
    cameraTarget=(0.0209791, -0.0419579, 0.520979))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.56086, 
    farPlane=4.79561, width=3.3481, height=1.20172, cameraPosition=(2.20639, 
    1.22646, 3.17565), cameraUpVector=(-0.534725, 0.755211, -0.379111), 
    cameraTarget=(0.0342509, -0.0325783, 0.514537))
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/temp/I/analysis.odb'])
o3 = session.openOdb(name='E:/temp/I/analysis.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=NONUNIFORM, nonuniformScaleFactor=(0, 0.00, 192506.1))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.26076, 
    farPlane=5.05628, width=2.95573, height=1.06089, cameraPosition=(2.13324, 
    2.0703, 2.63324), cameraUpVector=(-0.866479, 0.466602, -0.177473), 
    cameraTarget=(0.020979, -0.0419581, 0.520979))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.84162, 
    farPlane=4.38941, width=3.71516, height=1.33347, cameraPosition=(-0.23058, 
    3.60759, 0.569969), cameraUpVector=(-0.895594, -0.393094, -0.208298), 
    cameraTarget=(0.020991, -0.0419658, 0.520989))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.69834, 
    farPlane=4.5327, width=5.1347, height=1.84298, viewOffsetX=0.0546312, 
    viewOffsetY=0.127164)
session.viewports['Viewport: 1'].view.setValues(width=5.1958, height=1.86491, 
    cameraPosition=(-0.13224, -0.00795144, 4.02878), cameraUpVector=(0, 1, 0), 
    cameraTarget=(-0.13224, -0.00795144, 0.413265), viewOffsetX=0, 
    viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(3.48327, 
    -0.00795144, 0.413265))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.13224, 
    3.60756, 0.413265), cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.70949, 
    farPlane=4.50563, width=4.94306, height=1.77419, viewOffsetX=-0.000531653, 
    viewOffsetY=-0.00364892)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(0, 0, 19506))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(0, 0, 29506))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.68003, 
    farPlane=4.53509, width=5.22267, height=1.87455, viewOffsetX=-0.0194979, 
    viewOffsetY=0.0372274)
session.viewports['Viewport: 1'].view.setValues(width=5.23418, height=1.87868, 
    cameraPosition=(3.50157, -2.38419e-07, 0.463376), cameraUpVector=(0, 1, 0), 
    cameraTarget=(-0.105994, -2.38419e-07, 0.463376), viewOffsetX=0, 
    viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.105994, 
    3.60756, 0.463376), cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(0, 0, 49506))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(0, 0, 89506))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.70551, 
    farPlane=4.50961, width=5.56108, height=1.99601, viewOffsetX=0.0550005, 
    viewOffsetY=0.0414276)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.42972, 
    farPlane=4.76893, width=4.99421, height=1.79255, cameraPosition=(
    -0.0839381, 3.30076, -0.936992), cameraUpVector=(-0.0458408, 0.390132, 
    0.919617), cameraTarget=(-0.10354, -0.0206055, 0.471067), 
    viewOffsetX=0.0493941, viewOffsetY=0.0372047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.6063, 
    farPlane=4.56576, width=5.35716, height=1.92282, cameraPosition=(0.301229, 
    3.56755, 0.272213), cameraUpVector=(-0.14538, 0.0715121, 0.986788), 
    cameraTarget=(-0.100084, -0.0120196, 0.472502), viewOffsetX=0.0529837, 
    viewOffsetY=0.0399085)
session.viewports['Viewport: 1'].view.setValues(width=5.38932, height=1.93436, 
    cameraPosition=(3.40869, 0.0206838, 0.514396), cameraUpVector=(0, 1, 0), 
    cameraTarget=(-0.177341, 0.0206838, 0.514396), viewOffsetX=0, 
    viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.177341, 
    3.60671, 0.514396), cameraUpVector=(0, 0, 1))
