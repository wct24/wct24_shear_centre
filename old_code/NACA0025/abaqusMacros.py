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
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, distortionControl=DEFAULT)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
    elemType1 = mesh.ElemType(elemCode=C3D20R)
    elemType2 = mesh.ElemType(elemCode=C3D15)
    elemType3 = mesh.ElemType(elemCode=C3D10)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
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
    session.viewports['Viewport: 1'].view.setValues(width=4.2405, height=1.52203, 
        viewOffsetX=0.527442, viewOffsetY=-0.143004)
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.56982, 
        farPlane=8.23446, width=1.33246, height=0.479449, 
        viewOffsetX=-0.788886, viewOffsetY=-0.198322)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    p.PartitionFaceByAuto(face=f[70])
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.51943, 
        farPlane=8.28485, width=1.95835, height=0.702901, 
        viewOffsetX=-0.665881, viewOffsetY=-0.199994)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByThreePoints(name='Datum csys-2', coordSysType=CARTESIAN, origin=(
        0.0, 0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.60584, 
        farPlane=8.19844, width=1.00703, height=0.361449, 
        viewOffsetX=-0.795263, viewOffsetY=-0.318978)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    a.DatumCsysByThreePoints(origin=r1[130], name='Datum csys-3', 
        coordSysType=CARTESIAN, point1=(0.0, 0.0, 0.0), line2=(0.0, 9.0, 0.0))
def Macro4():
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
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.63592, 
        farPlane=8.16835, width=0.20801, height=0.183791, 
        viewOffsetX=-0.885241, viewOffsetY=-0.379321)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByThreePoints(name='Datum csys-2', coordSysType=CARTESIAN, origin=(
        0.0, 0.0, 3.0), point1=(0.0, 0.0, 0.0), line2=(0.0, 9.0, 0.0), 
        isDependent=False)
def Macro5():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30767, 
        farPlane=3.84838, width=1.71487, height=0.800238, 
        viewOffsetX=-0.0636238, viewOffsetY=0.220195)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.39196, 
        farPlane=3.78311, width=1.77751, height=0.829468, cameraPosition=(
        -0.312479, 0.275078, 3.55007), cameraUpVector=(0.0191675, 0.893571, 
        -0.448512), cameraTarget=(0.0388155, -0.107079, 0.516134), 
        viewOffsetX=-0.0659477, viewOffsetY=0.228238)
    p = mdb.models['Model-1'].parts['part']
    del p.features['Partition face-1']
def Macro6():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.26946, 
        farPlane=3.88659, width=2.46479, height=1.15019, viewOffsetX=0.294047, 
        viewOffsetY=0.0519966)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.99829, 
        farPlane=3.53436, width=2.17028, height=1.01275, cameraPosition=(
        -0.445863, 0.592671, 3.15121), cameraUpVector=(-0.101317, 0.81772, 
        -0.566629), cameraTarget=(0.00358334, -0.144227, 0.196681), 
        viewOffsetX=0.258912, viewOffsetY=0.0457836)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1333, 
        farPlane=3.39936, width=0.63182, height=0.294836, viewOffsetX=0.379509, 
        viewOffsetY=-0.0493)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.79354, 
        farPlane=3.31712, width=0.531194, height=0.24788, cameraPosition=(
        -1.91325, -0.158555, 2.08045), cameraUpVector=(0.211664, 0.964012, 
        -0.160872), cameraTarget=(0.339866, 0.0630541, -0.00488544), 
        viewOffsetX=0.319067, viewOffsetY=-0.0414483)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85846, 
        farPlane=3.34658, width=0.550423, height=0.256853, cameraPosition=(
        -1.53287, 0.267741, 2.52095), cameraUpVector=(0.217626, 0.902058, 
        -0.372733), cameraTarget=(0.185544, -0.0560966, -0.0121171), 
        viewOffsetX=0.330617, viewOffsetY=-0.0429486)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.09778, 
        farPlane=3.53488, width=0.621304, height=0.289929, cameraPosition=(
        1.04388, 0.307054, 3.15637), cameraUpVector=(-0.00246805, 0.893266, 
        -0.449523), cameraTarget=(-0.307663, 0.0655795, 0.401506), 
        viewOffsetX=0.373192, viewOffsetY=-0.0484793)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04772, 
        farPlane=3.58494, width=1.13523, height=0.52975, viewOffsetX=0.283367, 
        viewOffsetY=-0.054964)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #92492292 #24924924 #49249249 #12492 ]', 
        ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02641, 
        farPlane=3.61757, width=1.12341, height=0.524236, cameraPosition=(
        1.49749, 0.349093, 2.95027), cameraUpVector=(-0.19249, 0.896997, 
        -0.397925), cameraTarget=(-0.327806, 0.0119686, 0.494888), 
        viewOffsetX=0.280418, viewOffsetY=-0.054392)
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13603, 
        farPlane=3.45329, width=1.18419, height=0.552595, cameraPosition=(
        -0.592715, 0.27276, 3.21399), cameraUpVector=(0.465759, 0.833321, 
        -0.297732), cameraTarget=(-0.136086, 0.16193, 0.172041), 
        viewOffsetX=0.295588, viewOffsetY=-0.0573344)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.19664, 
        farPlane=3.39268, width=0.312166, height=0.145671, 
        viewOffsetX=0.0668044, viewOffsetY=-0.11643)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.19812, 
        farPlane=3.3912, width=0.312377, height=0.14577, cameraPosition=(
        -0.672608, 0.246555, 3.20295), cameraUpVector=(0.0131374, 0.929269, 
        -0.369171), cameraTarget=(-0.215979, 0.135725, 0.161003), 
        viewOffsetX=0.0668497, viewOffsetY=-0.116509)
