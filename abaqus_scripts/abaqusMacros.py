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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.Line(point1=(0.0, 0.0), point2=(0.0, 0.1))
    s1.VerticalConstraint(entity=g[2], addUndoState=False)
    s1.delete(objectList=(g[2], c[4]))
    s1.Line(point1=(-0.01, 0.0), point2=(-0.01, 0.1))
    s1.VerticalConstraint(entity=g[3], addUndoState=False)
    s1.Line(point1=(0.01, 0.0), point2=(0.01, 0.1))
    s1.VerticalConstraint(entity=g[4], addUndoState=False)
    s1.delete(objectList=(g[3], g[4], c[7], c[10]))
    s1.Line(point1=(0.0, 0.0), point2=(0.0, 0.1))
    s1.VerticalConstraint(entity=g[5], addUndoState=False)
    s1.Line(point1=(0.0, 0.1), point2=(0.2, 0.1))
    s1.HorizontalConstraint(entity=g[6], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.807636, 
        farPlane=1.07798, width=1.66505, height=0.69412, cameraPosition=(
        -0.192899, 0.138621, 0.942809), cameraTarget=(-0.192899, 0.138621, 0))
    s1.Line(point1=(0.2, 0.1), point2=(0.2, -0.2))
    s1.VerticalConstraint(entity=g[7], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    s1.Line(point1=(0.2, -0.2), point2=(-0.2, -0.2))
    s1.HorizontalConstraint(entity=g[8], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
    s1.Line(point1=(-0.2, -0.2), point2=(-0.2, 0.3))
    s1.VerticalConstraint(entity=g[9], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
    s1.Line(point1=(-0.2, 0.3), point2=(0.4, 0.3))
    s1.HorizontalConstraint(entity=g[10], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.878477, 
        farPlane=1.00714, width=0.79243, height=0.330346, cameraPosition=(
        -0.0934552, 0.0691754, 0.942809), cameraTarget=(-0.0934552, 0.0691754, 
        0))
    s1.Line(point1=(-0.01, 0.0), point2=(-0.01, 0.11))
    s1.VerticalConstraint(entity=g[11], addUndoState=False)
    s1.Line(point1=(-0.01, 0.11), point2=(0.21, 0.11))
    s1.HorizontalConstraint(entity=g[12], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.822391, 
        farPlane=1.06323, width=1.6787, height=0.699811, cameraPosition=(
        -0.439633, 0.0500148, 0.942809), cameraTarget=(-0.439633, 0.0500148, 
        0))
    s1.Line(point1=(0.21, 0.11), point2=(0.21, -0.2))
    s1.VerticalConstraint(entity=g[13], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.885265, 
        farPlane=1.00035, width=0.70882, height=0.295491, cameraPosition=(
        -0.0603675, -0.107252, 0.942809), cameraTarget=(-0.0603675, -0.107252, 
        0))
    s1.Line(point1=(0.21, -0.2), point2=(0.21, -0.21))
    s1.VerticalConstraint(entity=g[14], addUndoState=False)
    s1.ParallelConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
    s1.Line(point1=(0.21, -0.21), point2=(-0.21, -0.21))
    s1.HorizontalConstraint(entity=g[15], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.894028, 
        farPlane=0.99159, width=0.600876, height=0.250492, cameraPosition=(
        -0.0901356, 0.226501, 0.942809), cameraTarget=(-0.0901356, 0.226501, 
        0))
    s1.Line(point1=(-0.21, -0.21), point2=(-0.21, 0.31))
    s1.VerticalConstraint(entity=g[16], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.866659, 
        farPlane=1.01896, width=0.938014, height=0.391037, cameraPosition=(
        0.241224, 0.182161, 0.942809), cameraTarget=(0.241224, 0.182161, 0))
    s1.Line(point1=(-0.21, 0.31), point2=(0.4, 0.31))
    s1.HorizontalConstraint(entity=g[17], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.861798, 
        farPlane=1.02382, width=0.997887, height=0.415996, cameraPosition=(
        0.228762, 0.175927, 0.942809), cameraTarget=(0.228762, 0.175927, 0))
    s1.Line(point1=(0.4, 0.31), point2=(0.4, 0.29))
    s1.VerticalConstraint(entity=g[18], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[17], entity2=g[18], addUndoState=False)
    s1.Line(point1=(0.4, 0.29), point2=(-0.18500000002794, 0.29))
    s1.HorizontalConstraint(entity=g[19], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[18], entity2=g[19], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.823932, 
        farPlane=1.06169, width=1.46431, height=0.610438, cameraPosition=(
        0.423628, 0.0521057, 0.942809), cameraTarget=(0.423628, 0.0521057, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.423628, 
        -0.146811, 0.942809), cameraTarget=(0.423628, -0.146811, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.903779, 
        farPlane=0.981839, width=0.480768, height=0.200421, cameraPosition=(
        0.00691722, -0.184922, 0.942809), cameraTarget=(0.00691722, -0.184922, 
        0))
    s1.Line(point1=(-0.18500000002794, 0.29), point2=(-0.19, -0.19))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.905364, 
        farPlane=0.980254, width=0.522003, height=0.217611, cameraPosition=(
        -0.0735135, -0.180777, 0.942809), cameraTarget=(-0.0735135, -0.180777, 
        0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0560917, 
        -0.180777, 0.942809), cameraTarget=(0.0560917, -0.180777, 0))
    s1.Line(point1=(-0.19, -0.19), point2=(0.19, -0.19))
    s1.HorizontalConstraint(entity=g[21], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.916444, 
        farPlane=0.969174, width=0.324759, height=0.135385, cameraPosition=(
        0.107423, 0.0281998, 0.942809), cameraTarget=(0.107423, 0.0281998, 0))
    s1.Line(point1=(0.19, -0.19), point2=(0.19, 0.09))
    s1.VerticalConstraint(entity=g[22], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[21], entity2=g[22], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.870391, 
        farPlane=1.01523, width=1.00954, height=0.420856, cameraPosition=(
        -0.0692198, -0.105149, 0.942809), cameraTarget=(-0.0692198, -0.105149, 
        0))
    s1.Line(point1=(0.19, 0.09), point2=(0.01, 0.09))
    s1.HorizontalConstraint(entity=g[23], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[22], entity2=g[23], addUndoState=False)
    s1.Line(point1=(0.01, 0.09), point2=(0.01, 0.0))
    s1.VerticalConstraint(entity=g[24], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[23], entity2=g[24], addUndoState=False)
    s1.Line(point1=(0.01, 0.0), point2=(-0.01, 0.0))
    s1.HorizontalConstraint(entity=g[25], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[24], entity2=g[25], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.794336, 
        farPlane=1.09128, width=1.82887, height=0.762415, cameraPosition=(
        0.048655, 0.00759951, 0.942809), cameraTarget=(0.048655, 0.00759951, 
        0))
    s1.delete(objectList=(g[6], g[5], g[7], g[8], g[9], g[10]))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.786701, 
        farPlane=1.09892, width=1.92292, height=0.801621, cameraPosition=(
        0.11279, 0.0640674, 0.942809), cameraTarget=(0.11279, 0.0640674, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s1, depth=5.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.09477, 
        farPlane=13.1088, width=2.92948, height=1.22123, viewOffsetX=-0.908873, 
        viewOffsetY=-0.615785)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.10831, 
        farPlane=13.0953, width=2.93384, height=1.22305, cameraPosition=(
        6.39605, 6.34644, 9.13136), cameraUpVector=(-0.593841, 0.577111, 
        -0.560621), cameraTarget=(-0.0135665, -0.0631793, 2.72175), 
        viewOffsetX=-0.910226, viewOffsetY=-0.616702)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.PartitionFaceByAuto(face=f[14])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.25261, 
        farPlane=12.951, width=0.978508, height=0.408938, viewOffsetX=-1.31301, 
        viewOffsetY=-0.657078)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.01)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.22969, 
        farPlane=12.9739, width=1.26044, height=0.526763, viewOffsetX=-1.30693, 
        viewOffsetY=-0.661635)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.001)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1c4 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3b ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.02, deviationFactor=0.1, 
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.23928, 
        farPlane=12.9643, width=1.14253, height=0.477486, viewOffsetX=-1.35241, 
        viewOffsetY=-0.660425)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3f ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.26298, 
        farPlane=12.9406, width=0.851018, height=0.355657, 
        viewOffsetX=-1.33573, viewOffsetY=-0.872709)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3a01 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#7fd000 #120000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.07758, 
        farPlane=13.126, width=3.13409, height=1.3098, viewOffsetX=-1.02059, 
        viewOffsetY=-0.551736)
    p = mdb.models['Model-1'].parts['Part-1']
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85199, 
        farPlane=2.55535, width=0.192167, height=0.0803106, 
        viewOffsetX=-0.300861, viewOffsetY=-0.131459)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#91492491 #92454914 #4 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84359, 
        farPlane=2.56374, width=0.333853, height=0.139524, 
        viewOffsetX=-0.295619, viewOffsetY=-0.128414)
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84822, 
        farPlane=2.55912, width=0.238559, height=0.0996986, 
        viewOffsetX=-0.276387, viewOffsetY=-0.145632)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#91492491 #92454914 #4 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#91492491 #92454914 #4 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
