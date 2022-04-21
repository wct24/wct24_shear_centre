# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Mon Jan 31 15:04:16 2022
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
execfile('NACA0025_script.py', __main__.__dict__)
#: 0.044268872
#: Warning: Grid center was moved to the sketch center.
#: ['Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object', 'Face object']
#: ['Cell object']
#: [1.0, 0.949999988079071, 0.899999976158142, 0.850000023841858, 0.800000011920929, 0.75, 0.699999988079071, 0.649999976158142, 0.600000023841858, 0.550000011920929, 0.5, 0.449999988079071, 0.400000005960464, 0.349999994039536, 0.300000011920929, 0.25, 0.200000002980232, 0.150000005960464, 0.100000001490116, 0.0500000007450581, 0.0]
#: ('e1', mdb.models['Model-1'].rootAssembly.edges)
#: ['Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object', 'Edge object']
#: The section "warping" has been assigned to 836 wires or attachment lines.
#: Job analysis: Analysis Input File Processor completed successfully.
#: Job analysis: Abaqus/Standard completed successfully.
#: Job analysis completed successfully. 
#: Model: E:/temp/reid_section/analysis.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             2
#: Number of Element Sets:       5
#: Number of Node Sets:          843
#: Number of Steps:              1
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(name='E:/temp/reid_section/analysis.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['E:/temp/reid_section/analysis.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63749, 
    farPlane=2.84765, width=0.617375, height=0.572432, cameraPosition=(
    0.908471, 0.732618, 2.43371), cameraUpVector=(-0.25755, 0.776533, 
    -0.575034), cameraTarget=(0.0327101, -0.0059111, 0.551222))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62625, 
    farPlane=2.87983, width=0.613136, height=0.568501, cameraPosition=(
    0.321445, -0.136753, 2.73671), cameraUpVector=(0.0980959, 0.948887, 
    -0.299985), cameraTarget=(0.0225264, -0.0209929, 0.556478))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6352, 
    farPlane=2.87963, width=0.616509, height=0.571628, cameraPosition=(
    0.0808535, -0.0721714, 2.75909), cameraUpVector=(0.141218, 0.938449, 
    -0.315233), cameraTarget=(0.0172542, -0.0195777, 0.556969))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0172542, 
    2.18409, 0.556969), cameraUpVector=(0, 0, 1))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2.22092, 
    -0.0195777, 0.556969), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0172542, 
    -0.0195777, 2.76063))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=NONUNIFORM, nonuniformScaleFactor=(100000, 100000, 0))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(10000, 10000, 0))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(1000, 1000, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.51391, 
    farPlane=8.73127, width=0.53581, height=0.496804, viewOffsetX=0.044507, 
    viewOffsetY=1.70066)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.101155, 
    8.04779, 0.5), cameraUpVector=(0, 0, 1), cameraTarget=(0.101155, 
    -0.0747993, 0.5), viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(8.22374, 
    -0.0747993, 0.5), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.101155, 
    -0.0747993, 8.62258))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(10000, 0, 0))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(8.22373, 
    -0.0747993, 0.5))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.101155, 
    -0.0747993, 8.62257))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.57646, 
    farPlane=8.66868, width=0.227196, height=0.210657, viewOffsetX=-0.0423193, 
    viewOffsetY=0.0625848)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.57482, 
    farPlane=8.66188, width=0.227147, height=0.210611, cameraPosition=(
    0.0153395, 0.911904, 8.57065), cameraUpVector=(-0.0327345, 0.99205, 
    -0.121516), cameraTarget=(0.103324, -0.072732, 0.508461), 
    viewOffsetX=-0.0423101, viewOffsetY=0.0625712)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.57746, 
    farPlane=8.66593, width=0.227226, height=0.210685, cameraPosition=(
    0.0455452, 0.125264, 8.62186), cameraUpVector=(-0.00636154, 0.999678, 
    -0.0245847), cameraTarget=(0.101564, -0.0740728, 0.501929), 
    viewOffsetX=-0.0423249, viewOffsetY=0.062593)
session.viewports['Viewport: 1'].view.setValues(width=0.227251, 
    height=0.210708, cameraPosition=(0.0557684, 8.11441, 0.500849), 
    cameraUpVector=(0, 0, 1), cameraTarget=(0.0557684, -0.00728053, 0.500849), 
    viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(8.17746, 
    -0.00728053, 0.500849), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0557684, 
    -0.00728053, 8.62254))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.58864, 
    farPlane=8.65644, width=0.167027, height=0.154868, viewOffsetX=0.00147713, 
    viewOffsetY=0.0171677)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    nonuniformScaleFactor=(100000, 0, 0))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.58901, 
    farPlane=8.65805, width=0.167035, height=0.154875, cameraPosition=(1.56205, 
    -0.10423, 8.48114), cameraUpVector=(0.0737435, 0.997276, -0.00179507), 
    cameraTarget=(0.0546028, -0.00712553, 0.501161), viewOffsetX=0.0014772, 
    viewOffsetY=0.0171686)
session.viewports['Viewport: 1'].view.setValues(nearPlane=7.5304, 
    farPlane=8.71666, width=0.446062, height=0.41359, viewOffsetX=0.0707503, 
    viewOffsetY=-0.00162328)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.60984, 
    farPlane=7.46895, width=0.0796066, height=0.0738114, viewOffsetX=0.394928, 
    viewOffsetY=0.216358)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.33787, 
    farPlane=7.60574, width=0.0757472, height=0.070233, cameraPosition=(
    3.33489, 2.93742, 6.26265), cameraUpVector=(-0.467863, 0.681529, 
    -0.562692), cameraTarget=(-0.0692434, -0.0799135, 1.56464), 
    viewOffsetX=0.375781, viewOffsetY=0.205869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.34954, 
    farPlane=7.59406, width=0.0173352, height=0.0160733, viewOffsetX=0.347544, 
    viewOffsetY=0.181952)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.80893, 
    farPlane=7.77692, width=0.0155834, height=0.014449, cameraPosition=(
    0.181733, 1.05646, 7.71079), cameraUpVector=(-0.195634, 0.850993, 
    -0.487379), cameraTarget=(-0.142446, -0.134498, 1.28894), 
    viewOffsetX=0.312422, viewOffsetY=0.163564)
session.viewports['Viewport: 1'].view.setValues(width=0.0161937, 
    height=0.0150149, cameraPosition=(0.229986, 6.48312, 1.4609), 
    cameraUpVector=(0, 0, 1), cameraTarget=(0.229986, 0.190196, 1.4609), 
    viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6.52291, 
    0.190196, 1.4609), cameraUpVector=(0, 1, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.229986, 
    0.190196, 7.75382))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.75128, 
    farPlane=7.75636, width=0.0124908, height=0.0115815, 
    viewOffsetX=0.00418676, viewOffsetY=0.00163595)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.75077, 
    farPlane=7.75687, width=0.0170179, height=0.015779, viewOffsetX=0.00488216, 
    viewOffsetY=0.00176632)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, interactions=ON, constraints=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.75366, 
    farPlane=7.75398, width=0.000778232, height=0.000721578, 
    viewOffsetX=-0.00114329, viewOffsetY=0.00203207)
session.viewports['Viewport: 1'].view.setValues(width=0.000783097, 
    height=0.00072609, cameraPosition=(0.228482, 6.44669, 1.5), 
    cameraUpVector=(0, 0, 1), cameraTarget=(0.228482, 0.192869, 1.5), 
    viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39267, 
    farPlane=6.44671, width=0.000110246, height=0.00010222, 
    viewOffsetX=-8.11958e-05, viewOffsetY=-0.000158051)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39266, 
    farPlane=6.44672, width=0.000331074, height=0.000124608, 
    viewOffsetX=-8.11957e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39265, 
    farPlane=6.44673, width=0.000483786, height=0.000182084, 
    viewOffsetX=-8.11956e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39266, 
    farPlane=6.44672, width=0.000411354, height=0.000154823, 
    viewOffsetX=-8.11957e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39266, 
    farPlane=6.44672, width=0.000362341, height=0.000136376, 
    viewOffsetX=-8.11957e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39265, 
    farPlane=6.44673, width=0.000505511, height=0.000190261, 
    viewOffsetX=-8.11956e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39263, 
    farPlane=6.44675, width=0.000765186, height=0.000287996, 
    viewOffsetX=-8.11954e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.39263, 
    farPlane=6.44675, width=0.000804324, height=0.000302726, 
    viewOffsetX=-8.11954e-05, viewOffsetY=-0.00015805)
session.viewports['Viewport: 1'].view.setValues(nearPlane=6.37068, 
    farPlane=6.4687, width=0.306657, height=0.115417, viewOffsetX=0.142036, 
    viewOffsetY=-0.0276995)
session.viewports['Viewport: 1'].view.setValues(width=0.298734, 
    height=0.112435, cameraPosition=(6.50504, 0.027, 1.47209), cameraUpVector=(
    0, 1, 0), cameraTarget=(0.0853535, 0.027, 1.47209), viewOffsetX=0, 
    viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0853535, 
    0.027, 7.89178))
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.88113, 
    farPlane=7.90243, width=0.131179, height=0.0493724, viewOffsetX=-0.01558, 
    viewOffsetY=-0.0105483)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.88046, 
    farPlane=7.90265, width=0.131161, height=0.0493656, cameraPosition=(
    -0.24407, -0.104609, 7.88327), cameraUpVector=(0.0274546, 0.999382, 
    0.0219356), cameraTarget=(0.0871378, 0.0269812, 1.47348), 
    viewOffsetX=-0.0155779, viewOffsetY=-0.0105468)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.86512, 
    farPlane=7.918, width=0.353318, height=0.132979, viewOffsetX=0.0314465, 
    viewOffsetY=0.00464096)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.86352, 
    farPlane=7.91959, width=0.353202, height=0.132936, cameraPosition=(
    -0.244287, -0.102203, 7.88331), cameraUpVector=(0.0851361, 0.996059, 
    0.0248479), cameraTarget=(0.0869207, 0.029387, 1.47352), 
    viewOffsetX=0.0314362, viewOffsetY=0.00463944)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.87339, 
    farPlane=7.92306, width=0.353919, height=0.133206, cameraPosition=(
    0.307739, 0.570221, 7.87018), cameraUpVector=(0.0518243, 0.994891, 
    -0.0866439), cameraTarget=(0.0845698, 0.0251205, 1.47757), 
    viewOffsetX=0.0315, viewOffsetY=0.00464886)
session.viewports['Viewport: 1'].view.setValues(nearPlane=4.87789, 
    farPlane=7.91855, width=0.276578, height=0.104097, viewOffsetX=-0.00154436, 
    viewOffsetY=0.00180578)
session.viewports['Viewport: 1'].view.setValues(width=0.277506, 
    height=0.104446, cameraPosition=(6.48164, 0.0294106, 1.4988), 
    cameraUpVector=(0, 1, 0), cameraTarget=(0.0834171, 0.0294106, 1.4988), 
    viewOffsetX=0, viewOffsetY=0)
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0834171, 
    0.0294106, 7.89702))
