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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=25.2752, 
        farPlane=27.6494, width=3.00796, height=2.8065, viewOffsetX=0.267907, 
        viewOffsetY=-1.51788)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
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
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00892, 
        farPlane=3.7626, width=0.978657, height=0.913111, cameraPosition=(
        1.11748, 1.65556, 2.68077), cameraUpVector=(-0.495861, 0.554842, 
        -0.668036), cameraTarget=(0.196864, -0.0244346, 0.532571))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14759, 
        farPlane=3.62392, width=0.294774, height=0.275032, 
        viewOffsetX=-0.34707, viewOffsetY=-0.256452)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.2992, 
        farPlane=3.62428, width=0.315584, height=0.294448, cameraPosition=(
        1.87016, 0.716548, 2.84306), cameraUpVector=(-0.462626, 0.821407, 
        -0.333568), cameraTarget=(0.200723, 0.0334766, 0.600053), 
        viewOffsetX=-0.371571, viewOffsetY=-0.274556)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16667, 
        farPlane=3.75682, width=1.03775, height=0.968251, 
        viewOffsetX=-0.329376, viewOffsetY=-0.170944)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.89277, 
        farPlane=3.4677, width=0.906565, height=0.845847, cameraPosition=(
        1.89534, 1.83995, 1.47843), cameraUpVector=(-0.786876, 0.497041, 
        -0.365754), cameraTarget=(-0.00733924, -0.0331248, 0.403208), 
        viewOffsetX=-0.287737, viewOffsetY=-0.149334)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1468, 
        farPlane=3.74608, width=1.02824, height=0.95937, cameraPosition=(
        1.34949, 0.957156, 3.05353), cameraUpVector=(-0.692481, 0.680553, 
        -0.239413), cameraTarget=(0.143011, 0.253924, 0.536673), 
        viewOffsetX=-0.326355, viewOffsetY=-0.169376)
def Macro3():
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
    odb = session.odbs['E:/temp/SC/analysis.odb']
    session.writeFieldReport(fileName='stress.csv', append=OFF, 
        sortItem='Node Label', odb=odb, step=0, frame=1, 
        outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT), ))
