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
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.39))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.828168, 
        farPlane=1.05745, width=1.59816, height=0.69412, cameraPosition=(
        0.00172994, 0.0318447, 0.942809), cameraTarget=(0.00172994, 0.0318447, 
        0))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.42))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.775952, 
        farPlane=1.10967, width=2.05533, height=0.892682, cameraPosition=(
        0.153979, -0.18111, 0.942809), cameraTarget=(0.153979, -0.18111, 0))
    s1.delete(objectList=(g[2], ))
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.38))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.847201, 
        farPlane=1.03842, width=1.17769, height=0.511502, cameraPosition=(
        0.0933151, -0.331871, 0.942809), cameraTarget=(0.0933151, -0.331871, 
        0))
    s1.rectangle(point1=(-0.04, -0.42), point2=(0.0, 0.42))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.901607, 
        farPlane=0.984012, width=0.507529, height=0.220433, cameraPosition=(
        0.0523625, 0.367115, 0.942809), cameraTarget=(0.0523625, 0.367115, 0))
    s1.autoTrimCurve(curve1=g[3], point1=(-0.0592432878911495, 0.414711952209473))
    s1.autoTrimCurve(curve1=g[9], point1=(-0.0316980294883251, 0.417242050170898))
    s1.autoTrimCurve(curve1=g[4], point1=(-0.0215664468705654, 0.379923462867737))
    s1.autoTrimCurve(curve1=g[11], point1=(-0.0586100779473782, 0.375179588794708))
    s1.autoTrimCurve(curve1=g[7], point1=(0.00154623761773109, 0.392890095710754))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.85907, 
        farPlane=1.02655, width=1.03149, height=0.448003, cameraPosition=(
        0.11421, -0.30877, 0.942809), cameraTarget=(0.11421, -0.30877, 0))
    s1.autoTrimCurve(curve1=g[13], point1=(-0.00129442662000656, 
        -0.402290999889374))
    s1.autoTrimCurve(curve1=g[12], point1=(-0.0167378708720207, 
        -0.381079912185669))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.909572, 
        farPlane=0.976046, width=0.409409, height=0.177816, cameraPosition=(
        0.0328638, -0.3868, 0.942809), cameraTarget=(0.0328638, -0.3868, 0))
    s1.autoTrimCurve(curve1=g[10], point1=(-0.0295818783342838, 
        -0.417797148227692))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.746227, 
        farPlane=1.13939, width=2.42148, height=1.05171, cameraPosition=(
        0.172411, 0.0859817, 0.942809), cameraTarget=(0.172411, 0.0859817, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s1, depth=1.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10653, 
        farPlane=3.75682, width=2.23751, height=0.971806, 
        viewOffsetX=0.000473559, viewOffsetY=0.000415348)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28334, 
        farPlane=3.64121, width=2.42532, height=1.05338, cameraPosition=(
        0.225595, 0.0143203, 3.46216), cameraUpVector=(-0.576739, 0.744839, 
        -0.33554), cameraTarget=(0.184134, -0.0262091, 0.531057), 
        viewOffsetX=0.000513308, viewOffsetY=0.000450211)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.40332, 
        farPlane=3.52124, width=0.615108, height=0.267825, 
        viewOffsetX=-0.262468, viewOffsetY=-0.146112)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#40 ]', ), )
    v1, e, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[9], point2=v1[6], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.40531, 
        farPlane=3.51925, width=0.590614, height=0.25716, viewOffsetX=0.109459, 
        viewOffsetY=0.349129)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#40 ]', ), )
    v2, e1, d2 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v2[8], point2=v2[4], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27181, 
        farPlane=3.65275, width=2.51363, height=1.09446, viewOffsetX=0.198654, 
        viewOffsetY=0.0871294)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1403, 
        farPlane=3.68101, width=2.36812, height=1.03111, cameraPosition=(
        -0.164915, -0.422719, 3.35958), cameraUpVector=(-0.223828, 0.9526, 
        -0.206044), cameraTarget=(0.100127, 0.0419429, 0.477118), 
        viewOffsetX=0.187154, viewOffsetY=0.0820857)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08471, 
        farPlane=3.73661, width=3.41252, height=1.48585, viewOffsetX=0.222558, 
        viewOffsetY=-0.533339)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58455, 
        farPlane=3.43886, width=2.59378, height=1.12936, cameraPosition=(
        -0.400004, 1.25037, 2.61663), cameraUpVector=(0.226368, 0.733256, 
        -0.641166), cameraTarget=(0.413076, 0.0884691, 0.0507734), 
        viewOffsetX=0.169162, viewOffsetY=-0.40538)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1b ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=10, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78797, 
        farPlane=3.23543, width=0.775596, height=0.337704, 
        viewOffsetX=-0.0370046, viewOffsetY=-0.163101)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#40824 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.04, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#40824 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.004, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78284, 
        farPlane=3.24056, width=0.751107, height=0.327041, 
        viewOffsetX=-0.0148392, viewOffsetY=-0.636563)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56501, 
        farPlane=3.05838, width=0.659333, height=0.287081, cameraPosition=(
        0.0137785, 1.72512, 2.09981), cameraUpVector=(0.62962, 0.425242, 
        -0.65019), cameraTarget=(0.791748, -0.238049, 0.066226), 
        viewOffsetX=-0.0130261, viewOffsetY=-0.558785)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.53022, 
        farPlane=3.09317, width=1.13897, height=0.495919, 
        viewOffsetX=0.0234848, viewOffsetY=-0.539364)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03523, 
        farPlane=3.30658, width=1.51485, height=0.659582, cameraPosition=(
        -0.686342, 0.414171, 3.02195), cameraUpVector=(-0.0356415, 0.929963, 
        -0.365922), cameraTarget=(0.226219, 0.403721, 0.235941), 
        viewOffsetX=0.0312353, viewOffsetY=-0.717365)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.93215, 
        farPlane=3.32387, width=1.43812, height=0.626176, cameraPosition=(
        -0.0756435, 0.715219, 3.06344), cameraUpVector=(0.260515, 0.882226, 
        -0.392186), cameraTarget=(0.528761, 0.378003, 0.214629), 
        viewOffsetX=0.0296532, viewOffsetY=-0.681031)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95783, 
        farPlane=3.2982, width=1.09153, height=0.475264, 
        viewOffsetX=-0.0384157, viewOffsetY=-0.343856)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00735, 
        farPlane=3.2656, width=1.11914, height=0.487284, cameraPosition=(
        -0.0484302, 0.526132, 3.11551), cameraUpVector=(0.0659447, 0.930328, 
        -0.36075), cameraTarget=(0.428938, 0.421791, 0.22484), 
        viewOffsetX=-0.0393874, viewOffsetY=-0.352553)
