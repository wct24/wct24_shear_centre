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
    f = p.faces
    p.PartitionFaceByAuto(face=f[65])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.42854, 
        farPlane=14.4765, width=0.211374, height=0.228042, 
        viewOffsetX=-0.866386, viewOffsetY=-0.246741)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#45400801 #542244a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.00053, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.46704, 
        farPlane=14.438, width=0.0228783, height=0.0246824, 
        viewOffsetX=-0.931308, viewOffsetY=-0.232672)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#45400801 #542244a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.005, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#45400801 #542244a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.0005, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#45400801 #542244a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#45400801 #542244a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.002, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.44506, 
        farPlane=14.46, width=0.327519, height=0.142605, viewOffsetX=-0.71087, 
        viewOffsetY=-0.1557)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#babff7fe #fabddbb5 #7fff #4000000 #0 #80 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.3903, 
        farPlane=14.5148, width=1.13162, height=0.492719, 
        viewOffsetX=-0.483985, viewOffsetY=-0.127781)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.86246, 
        farPlane=14.012, width=0.793038, height=0.345298, 
        viewOffsetX=-0.0604061, viewOffsetY=0.0586341)
    p = mdb.models['Model-1'].parts['part']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #92492292 #24924924 #49249249 #12492 ]', 
        ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76335, 
        farPlane=14.1111, width=2.27277, height=0.989591, viewOffsetX=0.378279, 
        viewOffsetY=0.0294372)
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.83264, 
        farPlane=14.0419, width=1.1598, height=0.50499, viewOffsetX=0.0147709, 
        viewOffsetY=0.0918148)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    p.PartitionFaceByAuto(face=f[70])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.89486, 
        farPlane=13.9796, width=0.394589, height=0.171809, 
        viewOffsetX=-0.139267, viewOffsetY=0.0350845)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.0008, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.91819, 
        farPlane=13.9563, width=0.107887, height=0.0469751, 
        viewOffsetX=-0.213001, viewOffsetY=0.0368215)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.005, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.92193, 
        farPlane=13.9526, width=0.0618444, height=0.0269278, 
        viewOffsetX=-0.225267, viewOffsetY=0.038416)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.0005, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.002, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.003, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.91631, 
        farPlane=13.9582, width=0.13093, height=0.0570084, 
        viewOffsetX=-0.20622, viewOffsetY=0.0415531)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#10000000 #800140 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.7891, 
        farPlane=14.0854, width=1.91539, height=0.833984, 
        viewOffsetX=-0.200164, viewOffsetY=-0.0553463)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#ffffffff:7 #ffff ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.86408, 
        farPlane=14.0104, width=0.77301, height=0.336577, viewOffsetX=0.290831, 
        viewOffsetY=0.0729402)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#148900a5 #800142 #28 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84117, 
        farPlane=14.0333, width=1.05486, height=0.459298, viewOffsetX=0.051102, 
        viewOffsetY=0.0547461)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.87759, 
        farPlane=13.9969, width=0.606919, height=0.26426, 
        viewOffsetX=-0.0821121, viewOffsetY=0.0997664)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.86754, 
        farPlane=14.007, width=0.826038, height=0.359666, 
        viewOffsetX=-0.00840706, viewOffsetY=0.108922)
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.78257, 
        farPlane=14.0919, width=1.7761, height=0.773337, viewOffsetX=-0.676641, 
        viewOffsetY=0.114989)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.77774, 
        farPlane=14.0703, width=1.77513, height=0.772912, cameraPosition=(
        0.466522, -0.0835012, 13.9345), cameraTarget=(0.695159, -0.138311, 
        2.77766), viewOffsetX=-0.676269, viewOffsetY=0.114926)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.8445, 
        farPlane=14.0036, width=0.851247, height=0.370643, 
        viewOffsetX=-0.543153, viewOffsetY=0.10281)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84482, 
        farPlane=13.9957, width=0.851277, height=0.370656, cameraPosition=(
        0.650916, -0.0835012, 13.9345), cameraTarget=(0.879553, -0.138311, 
        2.77766), viewOffsetX=-0.543172, viewOffsetY=0.102814)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.80659, 
        farPlane=14.0339, width=1.43665, height=0.625534, 
        viewOffsetX=-0.549313, viewOffsetY=0.169038)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#eb76ff5a #ff7ffa3d #ffffffd7 #2400001 #0:2 #400000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.003, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#eb76ff5a #ff7ffa3d #ffffffd7 #2400001 #0:2 #400000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84668, 
        farPlane=13.9938, width=0.879725, height=0.383042, 
        viewOffsetX=-0.826265, viewOffsetY=0.196333)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.8427, 
        farPlane=13.9978, width=0.879329, height=0.38287, cameraPosition=(
        0.647834, -0.101693, 13.9345), cameraUpVector=(-0.0468664, 0.939624, 
        -0.338984), cameraTarget=(0.876471, -0.156503, 2.77769), 
        viewOffsetX=-0.825893, viewOffsetY=0.196244)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84083, 
        farPlane=14.0051, width=0.879143, height=0.382789, cameraPosition=(
        0.557927, 0.0376469, 13.9416), cameraUpVector=(-0.0341861, 0.935596, 
        -0.351414), cameraTarget=(0.872141, -0.164182, 2.78856), 
        viewOffsetX=-0.825719, viewOffsetY=0.196203)


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.8134, 
        farPlane=14.0325, width=1.16454, height=0.507056, 
        viewOffsetX=-0.805513, viewOffsetY=0.222565)
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76059, 
        farPlane=14.0853, width=1.81445, height=0.790031, viewOffsetX=-0.57634, 
        viewOffsetY=0.466558)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76916, 
        farPlane=14.0768, width=1.81622, height=0.790804, cameraPosition=(
        0.715147, 0.368656, 13.94), cameraUpVector=(-0.381403, 0.851566, 
        -0.359675), cameraTarget=(1.02936, 0.166827, 2.787), 
        viewOffsetX=-0.576904, viewOffsetY=0.467015)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.69757, 
        farPlane=14.0286, width=1.8014, height=0.784348, cameraPosition=(
        0.0456848, -1.50412, 13.7965), cameraUpVector=(-0.192873, 0.954498, 
        -0.227449), cameraTarget=(0.949802, -0.0520927, 2.76916), 
        viewOffsetX=-0.572195, viewOffsetY=0.463203)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76619, 
        farPlane=13.9599, width=0.864087, height=0.376233, 
        viewOffsetX=-0.663017, viewOffsetY=0.427287)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.78523, 
        farPlane=13.9767, width=0.865964, height=0.377051, cameraPosition=(
        0.214303, -0.848587, 13.8813), cameraUpVector=(-0.1705, 0.944908, 
        -0.279425), cameraTarget=(0.94345, -0.065166, 2.77357), 
        viewOffsetX=-0.664458, viewOffsetY=0.428216)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76626, 
        farPlane=13.9955, width=1.18221, height=0.514749, 
        viewOffsetX=-0.555439, viewOffsetY=0.438364)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#ffffffff:7 #ffff ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.78063, 
        farPlane=13.9812, width=0.869053, height=0.378396, 
        viewOffsetX=-0.570017, viewOffsetY=0.384147)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.78481, 
        farPlane=13.977, width=0.869466, height=0.378575, cameraPosition=(
        0.0396695, -1.12005, 13.8507), cameraUpVector=(0.171784, 0.951152, 
        -0.256516), cameraTarget=(0.768817, -0.336626, 2.74296), 
        viewOffsetX=-0.570288, viewOffsetY=0.38433)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.78856, 
        farPlane=14.003, width=0.869837, height=0.378737, cameraPosition=(
        -0.440928, -0.471641, 13.8985), cameraUpVector=(0.180188, 0.935802, 
        -0.302997), cameraTarget=(0.760405, -0.319879, 2.80522), 
        viewOffsetX=-0.570532, viewOffsetY=0.384494)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.64102, 
        farPlane=14.1505, width=2.97217, height=1.29412, viewOffsetX=-0.651505, 
        viewOffsetY=0.544449)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.65763, 
        farPlane=14.1829, width=2.97789, height=1.29661, cameraPosition=(
        -0.0254201, 0.229326, 13.9486), cameraUpVector=(0.00856979, 0.930253, 
        -0.36682), cameraTarget=(0.902704, -0.162956, 2.835), 
        viewOffsetX=-0.652758, viewOffsetY=0.545496)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84353, 
        farPlane=13.997, width=0.505643, height=0.220163, 
        viewOffsetX=-0.668475, viewOffsetY=0.0788592)
    p = mdb.models['Model-1'].parts['part']
    f1, e, v, d = p.faces, p.edges, p.vertices, p.datums
    p.PartitionFaceByCurvedPathEdgePoints(face=f1[10], edge1=e[60], edge2=e[50], 
        point1=p.InterestingPoint(edge=e[60], rule=MIDDLE), 
        point2=p.InterestingPoint(edge=e[50], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.79694, 
        farPlane=14.0436, width=1.07865, height=0.469658, 
        viewOffsetX=-0.572659, viewOffsetY=0.116141)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#900a5041 #2148 #140 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.84268, 
        farPlane=13.9978, width=0.516023, height=0.224682, 
        viewOffsetX=-0.33428, viewOffsetY=0.0950526)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#0 #140000 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76737, 
        farPlane=14.0732, width=1.44017, height=0.627065, viewOffsetX=-0.43109, 
        viewOffsetY=0.189579)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#6ff5afbe #ffffdeb7 #fffffebf #1200000f #0:2 #2000000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.00266384, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#6ff5afbe #ffffdeb7 #fffffebf #1200000f #0:2 #2000000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.008, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#6ff5afbe #ffffdeb7 #fffffebf #1200000f #0:2 #2000000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.76737, 
        farPlane=14.0732, width=1.44017, height=0.627065, 
        viewOffsetX=-0.431492, viewOffsetY=0.185957)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.09799, 
        farPlane=13.2206, width=3.60902, height=1.57141, viewOffsetX=-0.913299, 
        viewOffsetY=-0.300757)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.13048, 
        farPlane=14.6838, width=3.62191, height=1.57702, cameraPosition=(
        4.59334, 0.967376, 13.5005), cameraUpVector=(0.13897, 0.832622, 
        -0.536124), cameraTarget=(0.485127, -0.493658, 3.22832), 
        viewOffsetX=-0.916561, viewOffsetY=-0.301831)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.12903, 
        farPlane=14.6852, width=3.62134, height=1.57677, cameraPosition=(
        4.57048, 1.19578, 13.4772), cameraUpVector=(-0.0181764, 0.877284, 
        -0.479628), cameraTarget=(0.462263, -0.265251, 3.20498), 
        viewOffsetX=-0.916416, viewOffsetY=-0.301783)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.62797, 
        farPlane=15.2008, width=3.81926, height=1.66295, cameraPosition=(
        -0.0748464, 0.342374, 14.9089), cameraUpVector=(-0.212824, 0.910634, 
        -0.354192), cameraTarget=(0.0998872, 0.128922, 3.75298), 
        viewOffsetX=-0.966502, viewOffsetY=-0.318277)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.8726, 
        farPlane=14.9562, width=0.398456, height=0.173492, 
        viewOffsetX=-0.150509, viewOffsetY=-0.2416)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#0:2 #40 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[22], rule=MIDDLE), point2=p.InterestingPoint(edge=e[184], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    p.PartitionFaceByAuto(face=f[70])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.80657, 
        farPlane=15.0222, width=1.21043, height=0.527033, 
        viewOffsetX=-0.207603, viewOffsetY=-0.168948)
    p = mdb.models['Model-1'].parts['part']
    f1 = p.faces
    p.PartitionFaceByAuto(face=f1[10])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.86586, 
        farPlane=14.9629, width=0.481364, height=0.209591, 
        viewOffsetX=-0.109004, viewOffsetY=-0.20079)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[54], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[50], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#800 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[51], rule=MIDDLE), point2=p.InterestingPoint(edge=e[62], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84427, 
        farPlane=14.9845, width=0.746747, height=0.325142, 
        viewOffsetX=-0.151265, viewOffsetY=-0.17993)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[56], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[65], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84458, 
        farPlane=14.9776, width=0.74677, height=0.325152, cameraPosition=(
        0.21425, 0.406871, 14.9089), cameraTarget=(0.388984, 0.19342, 3.75298), 
        viewOffsetX=-0.15127, viewOffsetY=-0.179936)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#2000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[61], rule=MIDDLE), point2=p.InterestingPoint(edge=e[68], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#4000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[66], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[71], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point2=v[60], faces=pickedFaces, 
        point1=p.InterestingPoint(edge=e[71], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84075, 
        farPlane=14.9814, width=0.749534, height=0.326356, 
        viewOffsetX=-0.613692, viewOffsetY=-0.110724)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#0:2 #8000000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[133], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[236], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.76298, 
        farPlane=15.0592, width=1.92782, height=0.839394, viewOffsetX=-0.98002, 
        viewOffsetY=0.0844513)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.745, 
        farPlane=15.0584, width=1.92427, height=0.837849, cameraPosition=(
        0.812899, 0.406871, 14.9089), cameraTarget=(0.987633, 0.19342, 
        3.75298), viewOffsetX=-0.978216, viewOffsetY=0.0842958)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82062, 
        farPlane=14.9828, width=0.881815, height=0.383952, 
        viewOffsetX=-0.926651, viewOffsetY=0.0809218)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#21084249 #912014a4 #502842 ]', ), 
        )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.78916, 
        farPlane=15.0143, width=1.26887, height=0.552482, viewOffsetX=-1.02599, 
        viewOffsetY=-0.0690311)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#def7bfb6 #6edfeb5b #ffafd7bd #1fffff #490 #0:2 #248000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.05, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#def7bfb6 #6edfeb5b #ffafd7bd #1fffff #490 #0:2 #248000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.05, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83221, 
        farPlane=14.9712, width=0.739256, height=0.321881, 
        viewOffsetX=-0.83241, viewOffsetY=-0.0536775)
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85061, 
        farPlane=14.9528, width=0.513035, height=0.223381, 
        viewOffsetX=-0.842597, viewOffsetY=-0.0689254)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v[23], point2=v[20], faces=pickedFaces)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[23], point2=v1[20], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.86156, 
        farPlane=14.9419, width=0.378479, height=0.164794, 
        viewOffsetX=-0.774296, viewOffsetY=-0.0869926)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point2=v[20], faces=pickedFaces, 
        point1=p.InterestingPoint(edge=e[23], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85027, 
        farPlane=14.9532, width=0.517224, height=0.225205, 
        viewOffsetX=-0.963576, viewOffsetY=-0.0350074)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#100 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[28], point2=v1[25], faces=pickedFaces)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v[32], point2=v[29], faces=pickedFaces)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#0:3 #2 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[105], point2=v1[161], 
        faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.8547, 
        farPlane=14.9487, width=0.462859, height=0.201534, viewOffsetX=-1.0263, 
        viewOffsetY=-0.0217995)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v[5], point2=v[2], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83786, 
        farPlane=14.9656, width=0.66979, height=0.291634, 
        viewOffsetX=-0.965236, viewOffsetY=0.0179434)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#80 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[29], point2=v1[26], faces=pickedFaces)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84358, 
        farPlane=14.9599, width=0.599469, height=0.261016, 
        viewOffsetX=-0.997678, viewOffsetY=0.00170746)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84339, 
        farPlane=14.9539, width=0.599457, height=0.261011, cameraPosition=(
        1.02834, 0.42158, 14.9089), cameraTarget=(1.20307, 0.208129, 3.75298), 
        viewOffsetX=-0.997658, viewOffsetY=0.00170742)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82537, 
        farPlane=14.9719, width=0.785399, height=0.341972, 
        viewOffsetX=-1.06233, viewOffsetY=0.023007)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#8888a11 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.81175, 
        farPlane=14.9855, width=1.07744, height=0.469132, viewOffsetX=-1.08328, 
        viewOffsetY=0.100975)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(width=1.14564, height=0.498827, 
        viewOffsetX=-1.06297, viewOffsetY=0.109077)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82869, 
        farPlane=14.9686, width=0.744581, height=0.324199, 
        viewOffsetX=-0.977131, viewOffsetY=0.0441334)
    p = mdb.models['Model-1'].parts['part']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['part']
    p.deleteSeeds()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84989, 
        farPlane=14.9474, width=0.483886, height=0.210689, 
        viewOffsetX=-0.913431, viewOffsetY=-0.00326986)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v[36], faces=pickedFaces, 
        point2=p.InterestingPoint(edge=e[41], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point2=v1[34], faces=pickedFaces, 
        point1=p.InterestingPoint(edge=e1[40], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83207, 
        farPlane=14.9652, width=0.703012, height=0.306099, 
        viewOffsetX=-0.904051, viewOffsetY=0.0386102)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[50], rule=MIDDLE), point2=p.InterestingPoint(edge=e[51], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[40], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[38], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#10000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[54], rule=MIDDLE), point2=p.InterestingPoint(edge=e[55], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#800 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[44], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[42], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#20000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[58], rule=MIDDLE), point2=p.InterestingPoint(edge=e[59], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#1000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[48], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[46], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#40000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[62], rule=MIDDLE), point2=p.InterestingPoint(edge=e[63], 
        rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#40000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v1[50], faces=pickedFaces, 
        point2=p.InterestingPoint(edge=e1[64], rule=MIDDLE))
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#0 #8 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(point1=v[90], faces=pickedFaces, 
        point2=p.InterestingPoint(edge=e[123], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82406, 
        farPlane=14.9732, width=0.801492, height=0.348979, 
        viewOffsetX=-0.870341, viewOffsetY=0.0580387)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e1[59], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[57], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82406, 
        farPlane=14.9732, width=0.801492, height=0.348979, 
        viewOffsetX=-0.921632, viewOffsetY=0.0608707)
    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#4000000 ]', ), )
    v, e, d = p.vertices, p.edges, p.datums
    p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
        edge=e[81], rule=MIDDLE), point2=p.InterestingPoint(edge=e[82], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85734, 
        farPlane=14.9399, width=0.4439, height=0.193279, viewOffsetX=-1.04097, 
        viewOffsetY=-0.00589368)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85324, 
        farPlane=14.9399, width=0.443715, height=0.193199, cameraPosition=(
        1.17841, 0.435931, 14.9089), cameraTarget=(1.35314, 0.22248, 3.75298), 
        viewOffsetX=-1.04053, viewOffsetY=-0.00589123)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85177, 
        farPlane=14.9384, width=0.44365, height=0.19317, cameraPosition=(
        1.31931, 0.474312, 14.9089), cameraTarget=(1.49404, 0.260861, 3.75298), 
        viewOffsetX=-1.04038, viewOffsetY=-0.00589035)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85181, 
        farPlane=14.9384, width=0.443652, height=0.193171, cameraPosition=(
        1.30391, 0.463526, 14.9089), cameraTarget=(1.47864, 0.250075, 3.75298), 
        viewOffsetX=-1.04038, viewOffsetY=-0.00589038)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.78836, 
        farPlane=15.0019, width=1.35357, height=0.58936, viewOffsetX=-0.686893, 
        viewOffsetY=0.138832)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.7814, 
        farPlane=15.0071, width=1.35261, height=0.588942, cameraPosition=(
        1.26629, 0.387702, 14.9089), cameraTarget=(1.44102, 0.174251, 3.75298), 
        viewOffsetX=-0.686405, viewOffsetY=0.138734)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82463, 
        farPlane=14.9639, width=0.740773, height=0.322541, 
        viewOffsetX=-1.12536, viewOffsetY=0.105903)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82869, 
        farPlane=14.9608, width=0.74108, height=0.322675, cameraPosition=(
        1.23488, 0.387702, 14.9089), cameraTarget=(1.40961, 0.174251, 3.75298), 
        viewOffsetX=-1.12582, viewOffsetY=0.105947)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82924, 
        farPlane=14.9613, width=0.741122, height=0.322693, cameraPosition=(
        1.19985, 0.387702, 14.9089), cameraTarget=(1.37458, 0.174251, 3.75298), 
        viewOffsetX=-1.12588, viewOffsetY=0.105953)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82967, 
        farPlane=14.9618, width=0.741155, height=0.322707, cameraPosition=(
        1.17186, 0.387702, 14.9089), cameraTarget=(1.34659, 0.174251, 3.75298), 
        viewOffsetX=-1.12593, viewOffsetY=0.105958)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82961, 
        farPlane=14.9617, width=0.741151, height=0.322706, cameraPosition=(
        1.14492, 0.362734, 14.9089), cameraTarget=(1.31965, 0.149283, 3.75298), 
        viewOffsetX=-1.12592, viewOffsetY=0.105957)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82958, 
        farPlane=14.9617, width=0.741149, height=0.322705, cameraPosition=(
        1.14492, 0.360968, 14.9089), cameraTarget=(1.31965, 0.147517, 3.75298), 
        viewOffsetX=-1.12592, viewOffsetY=0.105957)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83009, 
        farPlane=14.9622, width=0.741188, height=0.322722, cameraPosition=(
        1.11261, 0.360968, 14.9089), cameraTarget=(1.28734, 0.147517, 3.75298), 
        viewOffsetX=-1.12598, viewOffsetY=0.105962)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83045, 
        farPlane=14.9626, width=0.741215, height=0.322734, cameraPosition=(
        1.08173, 0.35457, 14.9089), cameraTarget=(1.25646, 0.141119, 3.75298), 
        viewOffsetX=-1.12602, viewOffsetY=0.105966)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83091, 
        farPlane=14.963, width=0.741251, height=0.322749, cameraPosition=(
        1.05217, 0.354671, 14.9089), cameraTarget=(1.2269, 0.14122, 3.75298), 
        viewOffsetX=-1.12607, viewOffsetY=0.105971)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83143, 
        farPlane=14.9636, width=0.74129, height=0.322766, cameraPosition=(
        1.02037, 0.356144, 14.9089), cameraTarget=(1.1951, 0.142693, 3.75298), 
        viewOffsetX=-1.12613, viewOffsetY=0.105977)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#11155111 #111 ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=3, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()


