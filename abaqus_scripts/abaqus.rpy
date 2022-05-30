# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-17.21.41 127140
# Run by wct24 on Wed May 18 22:10:50 2022
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
execfile('shape_7.py', __main__.__dict__)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
    geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
import os
os.chdir(r"C:\Users\touze\project\wct24_shear_centre\abaqus_scripts")
session.viewports['Viewport: 1'].setValues(displayedObject=None)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.797034, 
    farPlane=1.08858, width=2.17075, height=1.01856, cameraPosition=(
    -0.0231676, 0.132199, 0.942809), cameraTarget=(-0.0231676, 0.132199, 0))
s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, 0.4), point2=(0.0, -0.4), 
    direction=CLOCKWISE)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914143, 
    farPlane=0.971475, width=0.353102, height=0.165683, cameraPosition=(
    0.340686, -0.0152572, 0.942809), cameraTarget=(0.340686, -0.0152572, 0))
s.Arc3Points(point1=(0.0, 0.41), point2=(0.0, -0.41), point3=(
    0.412606418132782, 0.0193976201117039))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.908058, 
    farPlane=0.977561, width=0.428066, height=0.200857, cameraPosition=(
    0.25893, -0.00494628, 0.942809), cameraTarget=(0.25893, -0.00494628, 0))
s.Arc3Points(point1=(0.0, 0.39), point2=(0.0, -0.39), point3=(0.39, 0.02))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.803878, 
    farPlane=1.08174, width=1.93678, height=0.908778, cameraPosition=(
    -0.157778, -0.0127311, 0.942809), cameraTarget=(-0.157778, -0.0127311, 0))
s.delete(objectList=(g[2], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.833002, 
    farPlane=1.05262, width=1.35259, height=0.634665, cameraPosition=(
    -0.121323, 0.234666, 0.942809), cameraTarget=(-0.121323, 0.234666, 0))
s.rectangle(point1=(0.0, -0.41), point2=(-0.02, 0.41))
s.autoTrimCurve(curve1=g[5], point1=(0.00229237228631973, 0.400285542011261))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.882199, 
    farPlane=1.00342, width=0.746594, height=0.350317, cameraPosition=(
    -0.0508321, -0.357238, 0.942809), cameraTarget=(-0.0508321, -0.357238, 0))
s.autoTrimCurve(curve1=g[9], point1=(-0.00122997164726257, -0.402132749557495))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.648681, 
    farPlane=1.23694, width=4.10031, height=1.92395, cameraPosition=(-0.30632, 
    -0.0456021, 0.942809), cameraTarget=(-0.30632, -0.0456021, 0))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s, depth=3.0)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.51035, 
    farPlane=8.2819, width=1.94982, height=0.880874, viewOffsetX=-0.589305, 
    viewOffsetY=-0.140395)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46631, 
    farPlane=8.32594, width=2.80376, height=1.26983, viewOffsetX=-0.296069, 
    viewOffsetY=-0.0733024)
p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#11491 ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
    constraint=FINER)
session.viewports['Viewport: 1'].view.setValues(nearPlane=5.45483, 
    farPlane=8.33742, width=2.63, height=1.19114, viewOffsetX=-0.333459, 
    viewOffsetY=-0.070095)
p = mdb.models['Model-1'].parts['Part-1']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Part-1']
p.generateMesh()
