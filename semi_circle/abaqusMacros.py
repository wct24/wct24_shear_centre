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


