# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#410 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.002, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#81 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.02, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()


def Macro2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['part']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.69341, 
        farPlane=13.5676, width=3.72962, height=4.02374, viewOffsetX=0.0513868, 
        viewOffsetY=0.00817469)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.02533, 
        farPlane=14.5157, width=3.44301, height=3.71452, cameraPosition=(
        1.64089, 1.305, 13.5757), cameraUpVector=(-0.0503193, 0.891024, 
        -0.451159), cameraTarget=(-0.0924687, -0.147214, 2.67729), 
        viewOffsetX=0.0474377, viewOffsetY=0.00754647)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.36607, 
        farPlane=14.175, width=2.05659, height=2.21877, viewOffsetX=-0.0922439, 
        viewOffsetY=-0.0634463)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#20 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#80 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3a0 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.6708, 
        farPlane=14.1825, width=2.1315, height=2.29959, cameraPosition=(
        -6.18337, 1.22502, 12.0323), cameraUpVector=(0.134051, 0.88679, 
        -0.442305), cameraTarget=(-0.211627, -0.129797, 2.73759), 
        viewOffsetX=-0.0956039, viewOffsetY=-0.0657573)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#f ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.40537, 
        farPlane=14.2708, width=2.06625, height=2.22919, cameraPosition=(
        0.687518, 0.625326, 13.8012), cameraUpVector=(-0.114133, 0.913126, 
        -0.391374), cameraTarget=(-0.0193914, -0.1493, 2.72014), 
        viewOffsetX=-0.0926772, viewOffsetY=-0.0637443)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.51946, 
        farPlane=14.1568, width=1.44479, height=1.55873, viewOffsetX=-0.213742, 
        viewOffsetY=-0.0258407)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.005, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.05, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.04, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.02, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
