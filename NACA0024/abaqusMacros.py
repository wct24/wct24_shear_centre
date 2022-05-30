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
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #9249248a #24924924 #49249249 #2 ]', ), 
        )
    p.seedEdgeBySize(edges=pickedEdges, size=0.005, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.45505, 
        farPlane=13.7105, width=1.4807, height=0.644715, viewOffsetX=0.366575, 
        viewOffsetY=0.0152742)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.46761, 
        farPlane=13.6979, width=1.41056, height=0.614176, viewOffsetX=0.367119, 
        viewOffsetY=0.0152969)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.47725, 
        farPlane=13.6883, width=1.285, height=0.559502, viewOffsetX=0.367537, 
        viewOffsetY=0.0153143)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.40514, 
        farPlane=13.7604, width=2.36545, height=1.02995, viewOffsetX=0.747369, 
        viewOffsetY=-0.0420586)
    session.viewports['Viewport: 1'].view.setValues(width=2.34087, height=1.01924, 
        cameraPosition=(0.866842, 11.0603, 2.56017), cameraUpVector=(0, 0, 1), 
        cameraTarget=(0.866842, -0.0224281, 2.56017), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.49534, 
        farPlane=12.6253, width=20.8228, height=9.0665, viewOffsetX=-6.53277, 
        viewOffsetY=-2.36845)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.42621, 
        farPlane=12.6944, width=20.6712, height=9.00049, cameraPosition=(
        0.866842, 11.0603, 3.66906), cameraTarget=(0.866842, -0.0224281, 
        3.66906), viewOffsetX=-6.48521, viewOffsetY=-2.35121)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.8612, 
        farPlane=11.2594, width=2.00458, height=0.872817, viewOffsetX=0.351759, 
        viewOffsetY=-3.68834)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.8512, 
        farPlane=11.2694, width=2.01406, height=0.876945, viewOffsetX=0.351433, 
        viewOffsetY=-3.68492)
    session.viewports['Viewport: 1'].view.setValues(width=2.01814, height=0.878723, 
        cameraPosition=(11.5689, 0, -0.0868671), cameraUpVector=(0, 1, 0), 
        cameraTarget=(0.508637, 0, -0.0868671), viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.4102, 
        farPlane=12.719, width=12.6463, height=5.50635, viewOffsetX=1.50081, 
        viewOffsetY=0.215099)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=3.84934, 
        farPlane=10.7911, width=4.67618, height=2.03606, cameraPosition=(
        -1.17008, 0.82627, 9.85852), cameraUpVector=(0.337026, 0.940878, 
        -0.0340796), cameraTarget=(-1.62376, 0.588596, -1.18988), 
        viewOffsetX=0.554949, viewOffsetY=0.0795364)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.75093, 
        farPlane=9.88949, width=0.749037, height=0.326139, viewOffsetX=1.19254, 
        viewOffsetY=-0.239296)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.7545, 
        farPlane=9.88592, width=0.749599, height=0.326384, cameraPosition=(
        -1.31947, 0.517199, 9.8713), cameraUpVector=(0.159679, 0.986778, 
        -0.0277846), cameraTarget=(-1.77315, 0.279525, -1.1771), 
        viewOffsetX=1.19344, viewOffsetY=-0.239475)


