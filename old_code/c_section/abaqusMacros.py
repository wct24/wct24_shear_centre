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
    mdb.models['Model-1'].ConstrainedSketch(name='Sketch-1', objectToCopy=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    mdb.models['Model-1'].sketches['Sketch-1'].writeAcisFile(
        fileName='C:/Users/touze/project/Shear_centre/c_section/c_section.sat', 
        version=24)
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    acis = mdb.openAcis(
        'C:/Users/touze/project/Shear_centre/c_section/c_section.sat', 
        scaleFromFile=OFF)
    mdb.models['Model-1'].ConstrainedSketchFromGeometryFile(name='c_section', 
        geometryFile=acis)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.84722, 
        farPlane=4.08098, width=1.44337, height=0.543245, 
        viewOffsetX=-0.0204397, viewOffsetY=-0.0130976)
    session.viewports['Viewport: 1'].view.setValues(width=1.44337, cameraPosition=(
        2.93923, -0.515935, -0.5), cameraTarget=(-0.524868, -0.515935, -0.5), 
        viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.524868, 
        2.94816, -0.5), cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.sketchOptions.setValues(gridOrigin=(0.204999998211861, 0.0))
    s.retrieveSketch(sketch=mdb.models['Model-1'].sketches['c_section'])
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63601, 
        farPlane=2.03115, width=2.43364, height=0.915958, cameraPosition=(
        0.132796, -0.135571, 1.83358), cameraTarget=(0.132796, -0.135571, 0))
    s.move(vector=(0.2, 0.0), objectList=(g[4], g[5], g[6], g[7], g[8], g[9], 
        g[10], g[11]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78499, 
        farPlane=1.88216, width=0.67734, height=0.254933, cameraPosition=(
        0.209293, 0.331208, 1.83358), cameraTarget=(0.209293, 0.331208, 0))
    s.move(vector=(0.05, 0.0), objectList=(g[4], g[5], g[6], g[7], g[8], g[9], 
        g[10], g[11]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70864, 
        farPlane=1.95852, width=1.53899, height=0.579237, cameraPosition=(
        0.146448, 0.241486, 1.83358), cameraTarget=(0.146448, 0.241486, 0))
    s.undo()
    s.undo()


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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.745257, 
        farPlane=1.14036, width=2.43342, height=0.915874, cameraPosition=(
        0.0794345, 0.111843, 0.942809), cameraTarget=(0.0794345, 0.111843, 0))
    s.rectangle(point1=(0.0, 0.41), point2=(0.41, -0.41))
    s.rectangle(point1=(0.0, 0.39), point2=(0.39, -0.39))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.7174, 
        farPlane=1.16822, width=2.77656, height=1.04502, cameraPosition=(
        0.126076, 0.0466612, 0.942809), cameraTarget=(0.126076, 0.0466612, 0))
    s.autoTrimCurve(curve1=g[2], point1=(-0.00123333930969238, 0.122788846492767))
    s.autoTrimCurve(curve1=g[6], point1=(-0.00123333930969238, 0.112407743930817))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=1.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, minSizeFactor=0.01)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08495, 
        farPlane=3.71406, width=2.51161, height=0.947669, cameraPosition=(
        1.3061, 0.563107, 3.12276), cameraUpVector=(-0.349773, 0.841608, 
        -0.411528), cameraTarget=(0.196864, -0.0244345, 0.532571))
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteSeeds()
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#492491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03246, 
        farPlane=3.69592, width=2.44838, height=0.923809, cameraPosition=(
        1.17216, 2.33372, -0.849793), cameraUpVector=(-0.128944, 0.204516, 
        0.970333), cameraTarget=(0.195885, -0.0114963, 0.503543))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15276, 
        farPlane=3.58563, width=2.5933, height=0.978492, cameraPosition=(
        -2.18067, 0.908623, -0.809689), cameraUpVector=(0.578294, 0.784889, 
        0.222541), cameraTarget=(0.212419, -0.00446847, 0.503345))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03761, 
        farPlane=3.6982, width=2.45458, height=0.926151, cameraPosition=(
        -0.126269, 1.01449, 3.16194), cameraUpVector=(0.415935, 0.703729, 
        -0.575989), cameraTarget=(0.205894, -0.00480466, 0.490732))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14682, 
        farPlane=3.58961, width=2.58614, height=0.975788, cameraPosition=(
        0.814834, 0.00280665, 3.30263), cameraUpVector=(0.212851, 0.896422, 
        -0.388745), cameraTarget=(0.20248, -0.00113408, 0.490222))
