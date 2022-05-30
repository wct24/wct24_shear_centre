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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=28.141, 
        farPlane=40.1575, width=1.13165, height=1.22089, viewOffsetX=-4.23287, 
        viewOffsetY=-1.87652)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#ffffffff:6 #7 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=28.2737, 
        farPlane=40.0248, width=0.3509, height=0.378572, viewOffsetX=-4.08366, 
        viewOffsetY=-1.81852)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #9249248a #24924924 #49249249 #2 ]', ), 
        )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #9249248a #24924924 #49249249 #2 ]', ), 
        )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=28.2684, 
        farPlane=40.03, width=0.425859, height=0.459442, viewOffsetX=-4.04894, 
        viewOffsetY=-1.71798)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=28.2332, 
        farPlane=40.0653, width=0.549235, height=0.592547, 
        viewOffsetX=-4.02624, viewOffsetY=-1.69594)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
