from abaqus import *
from abaqusConstants import *
import __main__
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
import os
import random
import csv
import json
#-------------------------------------------
# FUNCTIONS
#-------------------------------------------
def get_nodes(DAB, all_nodes):
    model = mdb.models['Model-1']
    a = model.rootAssembly
    """A function that will make a set of loading nodes at a given Distance Along Beam
    all_nodes = a.instances['name'].nodes"""
    number_of_nodes=0
    node_list = []
    for i in range(len(all_nodes)):
        node = all_nodes[i]
        if node.coordinates[2] == DAB:
            number_of_nodes+=1
            node_list.append(node)
        else:
            pass
    set_name = "nodes_at_z_%smm"%(int(DAB*1000))
    a.Set(nodes=mesh.MeshNodeArray(node_list), name =set_name)
    nodes = a.allSets[set_name].nodes
    return nodes, number_of_nodes

def get_z_coordinates(all_nodes):
    model = mdb.models['Model-1']
    a = model.rootAssembly
    z_coordinates = []
    for i in range(len(all_nodes)):
        node = all_nodes[i]
        if  node.coordinates[2] in z_coordinates:
            pass
        else:
            z_coordinates.append(node.coordinates[2])
    z_coordinates.sort(reverse=True)
    return z_coordinates



#------------------------------------------
#Script
#------------------------------------------
def main():

    beam = 0
    with open("beam.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i == beam+1:
                dimensions = str(row[3])
                dimensions = dimensions.strip('][').split(', ')
                # radius = float(dimensions[0])
                # thickness = float(dimensions[1])
                length = float(dimensions[0])
                print(length)
                Material = str(row[4])
                Material = Material.strip('][').split(', ')
                E = float(Material[0])*1000000000
                G = float(Material[1])*1000000000
                v_poisson = float(Material[2])
                print(E)
                BoundaryCondition = int(row[5])

                LoadType = int(row[6])
                print("loadType", LoadType)
                LoadZ = int(float(row[8]))
                LoadX = float(row[9])
                LoadY =  float(row[10])

                LoadMagnitude = float(row[11])
                LoadSection = int(row[12])

                break
    print("hello")
    #------------------------------------------------------------------------------------
    #                GEOMETRY
    #------------------------------------------------------------------------------------
    path = os.getcwd()
    folder = path
    # isExist = os.path.exists(path +r"/%s"%(str(LoadX*10)))
    # if isExist==False:
    #     os.mkdir(folder)
    #     os.chdir(folder)
    # else:
    #     os.chdir(folder)

    model = mdb.models['Model-1']
    s = model.ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints

    with open(r'C:\Users\touze\project\Shear_centre\NACA0025\points.csv') as f:
        x = csv.reader(f)
        data = list(x)
    x_o = data[0]
    y_o = data[1]
    x_i = data[2]
    y_i = data[3]


    number_of_points = len(x_o)
    for i in range(number_of_points):
        if i == number_of_points-1:
            s.Line(point1=(float(x_o[i]), float(y_o[i])), point2=(float(x_o[0]), float(y_o[0])))
            s.Line(point1=(float(x_i[i]), float(y_i[i])), point2=(float(x_i[0]), float(y_i[0])))
        else:
            s.Line(point1=(float(x_o[i]), float(y_o[i])), point2=(float(x_o[i+1]), float(y_o[i+1])))
            s.Line(point1=(float(x_i[i]), float(y_i[i])), point2=(float(x_i[i+1]), float(y_i[i+1])))

    p = mdb.models['Model-1'].Part(name='part', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)

    part = mdb.models['Model-1'].parts['part']
    part.BaseSolidExtrude(sketch=s, depth=length)
    s.unsetPrimaryObject()


    del mdb.models['Model-1'].sketches['__profile__']

    #------------------------------------------------------------------------------------
    #               MESH
    #------------------------------------------------------------------------------------


    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=(
        '[#92492491 #24924924 #49249249 #92492292 #24924924 #49249249 #12492 ]',
        ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['part']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()
    part.generateMesh()

    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#0:2 #40 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[22], rule=MIDDLE), point2=p.InterestingPoint(edge=e[184],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # print("f")
    # p.PartitionFaceByAuto(face=f[70])
    # print("f")
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.80657,
    #     farPlane=15.0222, width=1.21043, height=0.527033,
    #     viewOffsetX=-0.207603, viewOffsetY=-0.168948)
    # p = mdb.models['Model-1'].parts['part']
    # f1 = p.faces

    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.86586,
    #     farPlane=14.9629, width=0.481364, height=0.209591,
    #     viewOffsetX=-0.109004, viewOffsetY=-0.20079)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[54], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[50],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#800 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[51], rule=MIDDLE), point2=p.InterestingPoint(edge=e[62],
    #     rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84427,
    #     farPlane=14.9845, width=0.746747, height=0.325142,
    #     viewOffsetX=-0.151265, viewOffsetY=-0.17993)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#1000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[56], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[65],
    #     rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84458,
    #     farPlane=14.9776, width=0.74677, height=0.325152, cameraPosition=(
    #     0.21425, 0.406871, 14.9089), cameraTarget=(0.388984, 0.19342, 3.75298),
    #     viewOffsetX=-0.15127, viewOffsetY=-0.179936)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#2000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[61], rule=MIDDLE), point2=p.InterestingPoint(edge=e[68],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#4000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[66], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[71],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point2=v[60], faces=pickedFaces,
    #     point1=p.InterestingPoint(edge=e[71], rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84075,
    #     farPlane=14.9814, width=0.749534, height=0.326356,
    #     viewOffsetX=-0.613692, viewOffsetY=-0.110724)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#0:2 #8000000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[133], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[236],
    #     rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.76298,
    #     farPlane=15.0592, width=1.92782, height=0.839394, viewOffsetX=-0.98002,
    #     viewOffsetY=0.0844513)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.745,
    #     farPlane=15.0584, width=1.92427, height=0.837849, cameraPosition=(
    #     0.812899, 0.406871, 14.9089), cameraTarget=(0.987633, 0.19342,
    #     3.75298), viewOffsetX=-0.978216, viewOffsetY=0.0842958)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82062,
    #     farPlane=14.9828, width=0.881815, height=0.383952,
    #     viewOffsetX=-0.926651, viewOffsetY=0.0809218)
    # p = mdb.models['Model-1'].parts['part']
    # e = p.edges
    # pickedEdges = e.getSequenceFromMask(mask=('[#21084249 #912014a4 #502842 ]', ),
    #     )
    # p.seedEdgeByNumber(edges=pickedEdges, number=2, constraint=FINER)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.78916,
    #     farPlane=15.0143, width=1.26887, height=0.552482, viewOffsetX=-1.02599,
    #     viewOffsetY=-0.0690311)
    # p = mdb.models['Model-1'].parts['part']
    # e = p.edges
    # pickedEdges = e.getSequenceFromMask(mask=(
    #     '[#def7bfb6 #6edfeb5b #ffafd7bd #1fffff #490 #0:2 #248000 ]', ), )
    # p.seedEdgeBySize(edges=pickedEdges, size=0.001, deviationFactor=0.05,
    #     constraint=FINER)
    # p = mdb.models['Model-1'].parts['part']
    # e = p.edges
    # pickedEdges = e.getSequenceFromMask(mask=(
    #     '[#def7bfb6 #6edfeb5b #ffafd7bd #1fffff #490 #0:2 #248000 ]', ), )
    # p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.05,
    #     constraint=FINER)
    # p = mdb.models['Model-1'].parts['part']
    # p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    # p = mdb.models['Model-1'].parts['part']
    # p.generateMesh()
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83221,
    #     farPlane=14.9712, width=0.739256, height=0.321881,
    #     viewOffsetX=-0.83241, viewOffsetY=-0.0536775)
    # p = mdb.models['Model-1'].parts['part']
    # p.deleteMesh()
    # p = mdb.models['Model-1'].parts['part']
    # p.deleteSeeds()
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85061,
    #     farPlane=14.9528, width=0.513035, height=0.223381,
    #     viewOffsetX=-0.842597, viewOffsetY=-0.0689254)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v[23], point2=v[20], faces=pickedFaces)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v1[23], point2=v1[20], faces=pickedFaces)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.86156,
    #     farPlane=14.9419, width=0.378479, height=0.164794,
    #     viewOffsetX=-0.774296, viewOffsetY=-0.0869926)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point2=v[20], faces=pickedFaces,
    #     point1=p.InterestingPoint(edge=e[23], rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.85027,
    #     farPlane=14.9532, width=0.517224, height=0.225205,
    #     viewOffsetX=-0.963576, viewOffsetY=-0.0350074)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#100 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v1[28], point2=v1[25], faces=pickedFaces)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v[32], point2=v[29], faces=pickedFaces)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#0:3 #2 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v1[105], point2=v1[161],
    #     faces=pickedFaces)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.8547,
    #     farPlane=14.9487, width=0.462859, height=0.201534, viewOffsetX=-1.0263,
    #     viewOffsetY=-0.0217995)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v[5], point2=v[2], faces=pickedFaces)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83786,
    #     farPlane=14.9656, width=0.66979, height=0.291634,
    #     viewOffsetX=-0.965236, viewOffsetY=0.0179434)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#80 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v1[29], point2=v1[26], faces=pickedFaces)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84358,
    #     farPlane=14.9599, width=0.599469, height=0.261016,
    #     viewOffsetX=-0.997678, viewOffsetY=0.00170746)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84339,
    #     farPlane=14.9539, width=0.599457, height=0.261011, cameraPosition=(
    #     1.02834, 0.42158, 14.9089), cameraTarget=(1.20307, 0.208129, 3.75298),
    #     viewOffsetX=-0.997658, viewOffsetY=0.00170742)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82537,
    #     farPlane=14.9719, width=0.785399, height=0.341972,
    #     viewOffsetX=-1.06233, viewOffsetY=0.023007)
    # p = mdb.models['Model-1'].parts['part']
    # e = p.edges
    # pickedEdges = e.getSequenceFromMask(mask=('[#8888a11 ]', ), )
    # p.seedEdgeByNumber(edges=pickedEdges, number=2, constraint=FINER)
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.81175,
    #     farPlane=14.9855, width=1.07744, height=0.469132, viewOffsetX=-1.08328,
    #     viewOffsetY=0.100975)
    # p = mdb.models['Model-1'].parts['part']
    # p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    # p = mdb.models['Model-1'].parts['part']
    # p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    # session.viewports['Viewport: 1'].view.setValues(width=1.14564, height=0.498827,
    #     viewOffsetX=-1.06297, viewOffsetY=0.109077)
    # p = mdb.models['Model-1'].parts['part']
    # p.generateMesh()
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82869,
    #     farPlane=14.9686, width=0.744581, height=0.324199,
    #     viewOffsetX=-0.977131, viewOffsetY=0.0441334)
    # p = mdb.models['Model-1'].parts['part']
    # p.deleteMesh()
    # p = mdb.models['Model-1'].parts['part']
    # p.deleteSeeds()
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.84989,
    #     farPlane=14.9474, width=0.483886, height=0.210689,
    #     viewOffsetX=-0.913431, viewOffsetY=-0.00326986)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v[36], faces=pickedFaces,
    #     point2=p.InterestingPoint(edge=e[41], rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point2=v1[34], faces=pickedFaces,
    #     point1=p.InterestingPoint(edge=e1[40], rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.83207,
    #     farPlane=14.9652, width=0.703012, height=0.306099,
    #     viewOffsetX=-0.904051, viewOffsetY=0.0386102)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[50], rule=MIDDLE), point2=p.InterestingPoint(edge=e[51],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#400 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[40], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[38],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#10000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[54], rule=MIDDLE), point2=p.InterestingPoint(edge=e[55],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#800 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[44], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[42],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#20000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[58], rule=MIDDLE), point2=p.InterestingPoint(edge=e[59],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#1000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[48], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[46],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#40000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[62], rule=MIDDLE), point2=p.InterestingPoint(edge=e[63],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#40000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v1[50], faces=pickedFaces,
    #     point2=p.InterestingPoint(edge=e1[64], rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#0 #8 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(point1=v[90], faces=pickedFaces,
    #     point2=p.InterestingPoint(edge=e[123], rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82406,
    #     farPlane=14.9732, width=0.801492, height=0.348979,
    #     viewOffsetX=-0.870341, viewOffsetY=0.0580387)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#8000 ]', ), )
    # v1, e1, d1 = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e1[59], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[57],
    #     rule=MIDDLE))
    # session.viewports['Viewport: 1'].view.setValues(nearPlane=9.82406,
    #     farPlane=14.9732, width=0.801492, height=0.348979,
    #     viewOffsetX=-0.921632, viewOffsetY=0.0608707)
    # p = mdb.models['Model-1'].parts['part']
    # f = p.faces
    # pickedFaces = f.getSequenceFromMask(mask=('[#4000000 ]', ), )
    # v, e, d = p.vertices, p.edges, p.datums
    # p.PartitionFaceByShortestPath(faces=pickedFaces, point1=p.InterestingPoint(
    #     edge=e[81], rule=MIDDLE), point2=p.InterestingPoint(edge=e[82],
    #     rule=MIDDLE))
    # p = mdb.models['Model-1'].parts['part']
    # e = p.edges
    # pickedEdges = e.getSequenceFromMask(mask=('[#11155111 #111 ]', ), )
    # p.seedEdgeByNumber(edges=pickedEdges, number=2, constraint=FINER)
    # p = mdb.models['Model-1'].parts['part']
    # p = mdb.models['Model-1'].parts['part']
    # p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)




    # p.generateMesh()










    # #------------------------------------------------------------------------------------
    # #               SECTION
    # #------------------------------------------------------------------------------------
    c = part.cells
    print(c)
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    SC_section_geometry = part.Set(cells=cells, name='SC_section_geometry')

    model.Material(name='SC-material')
    model.materials['SC-material'].Elastic(type=ENGINEERING_CONSTANTS,
        table=((E, E, E,
                    v_poisson, v_poisson, v_poisson,
                    G, G, G), ))
    model.HomogeneousSolidSection(name='SC-section', material='SC-material', thickness=None)
    ## asigning the section
    part.SectionAssignment(region=SC_section_geometry, sectionName='SC-section', offset=0.0,
            offsetType=MIDDLE_SURFACE, offsetField='',
            thicknessAssignment=FROM_SECTION)
    ##assigning the material orientaion
    orientation=None
    part.MaterialOrientation(region=SC_section_geometry,
        orientationType=GLOBAL, axis=AXIS_1,
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='',
        stackDirection=STACK_3)
    #------------------------------------------------------------------------------------
    #               FIELD OUTPUT REQUEST
    #------------------------------------------------------------------------------------
    model.StaticStep(name='loading', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    model.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'MISES', 'SEQUT', 'U', 'COORD'))
    # ------------------------------------------------------------------------------------
    #               Assembly
    # ------------------------------------------------------------------------------------
    a = model.rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    a.Instance(name='SC_beam-1', part=part, dependent=ON)
    # ----------------------------------
    # Boundary Conditions ANd Load
    # ---------------------------------
    n1 = a.instances['SC_beam-1'].nodes #all nodes in the instance I beam

    list_of_z = get_z_coordinates(n1)
    loading_z = list_of_z[LoadSection]
    loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    wall_nodes, number_of_wall_nodes = get_nodes(0.0,n1)

    if BoundaryCondition == 2:
        model.DisplacementBC(name='BC-1', createStepName='Initial',
                region=a.sets['nodes_at_z_0mm'], u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                amplitude=UNSET, distributionType=UNIFORM, fieldName='',
                localCsys=None)

    if BoundaryCondition == 1:
        model.DisplacementBC(name='BC-1', createStepName='Initial',
            region=a.sets['nodes_at_z_0mm'], u1=SET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
            amplitude=UNSET, distributionType=UNIFORM, fieldName='',
            localCsys=None)
        terms_1 = [0 for i in range(number_of_wall_nodes)]
        terms_2 = [0 for i in range(number_of_wall_nodes)]
        terms_3 = [0 for i in range(number_of_wall_nodes)]

        for i in range(number_of_wall_nodes):
            node = wall_nodes[i]
            a.SetFromNodeLabels(nodeLabels=((node.instanceName, (node.label,)),), name='wall-%s'%(i))
            terms_1[i] = [1.0,'wall-%s'%(i), 3]
            (x,y,z) = node.coordinates
            terms_2[i] = [y,'wall-%s'%(i), 3]
            terms_3[i] = [x,'wall-%s'%(i), 3]

        #need to eliminate some terms that have alredy been used:
        def node_elimination(node_1, node_2, node_3):
            elmination_term = terms_2[node_1][0]
            for i in range(number_of_wall_nodes):
                terms_2[i][0] = terms_2[i][0]-elmination_term
            elmination_term = terms_3[node_1][0]
            for i in range(number_of_wall_nodes):
                terms_3[i][0] = terms_3[i][0]-elmination_term

            coefficient_node_2 = terms_2[node_2][0]
            for i in range(number_of_wall_nodes):
                terms_3[i][0] = terms_3[i][0]-terms_2[i][0]/coefficient_node_2
            a = terms_1[0]
            b = terms_1[node_1]
            terms_1[0] = b
            terms_1[node_1] = a
            a = terms_2[0]
            b = terms_2[node_2]
            terms_2[0] = b
            terms_2[node_2] = a
            terms_2.pop(node_1)
            a = terms_3[0]
            b = terms_3[node_3]
            terms_3[0] = b
            terms_3[node_3] = a
            unwanted = [node_1,node_2]

            for ele in sorted(unwanted, reverse = True):
                del terms_3[ele]
        node_elimination(3,1,2)
        model.Equation(name='sum_of_u3', terms=terms_1)
        model.Equation(name='moment_x_u3', terms=terms_2)
        model.Equation(name='moment_y_u3', terms=terms_3)






    v1 = a.instances['SC_beam-1'].vertices
    e1 = a.instances['SC_beam-1'].edges
    Csys = a.DatumCsysByThreePoints(origin=v1[4], point1=v1[5], name='end',
        coordSysType=CARTESIAN,
        point2=a.instances['SC_beam-1'].InterestingPoint(edge=e1[8],
        rule=MIDDLE))

    a.ReferencePoint(point=(LoadX, LoadY, list_of_z[LoadZ]))
    r1 = a.referencePoints.values()[0]


    model.ConnectorSection(name='warping', translationalType=SLOT)
    for i in range(0,number_of_loading_nodes):
        wire = a.WirePolyLine(points=((r1, loading_nodes[i]), ), mergeType=IMPRINT, meshable=OFF)
    e1 = a.edges
    a.Set(edges=e1, name='Wire-Set-loading')
    region=a.sets['Wire-Set-loading']
    csa = a.SectionAssignment(sectionName='warping', region=region)
    datums = a.datums.values() # make sure right one is used
    a.ConnectorOrientation(region=csa.getSet(), localCsys1=datums[1])

    #-------------------------------------------------
    #       LOADING
    #-----------------------------------------------

    refPoints1=(r1, )
    region = a.Set(referencePoints=refPoints1, name='loading')

    if LoadType == 1:
        # #force
        mdb.models['Model-1'].ConcentratedForce(name='Load-1',
            createStepName='loading', region=region, cf2=LoadMagnitude,
            distributionType=UNIFORM, field='', localCsys=None)
    if LoadType == 2:
        mdb.models['Model-1'].Moment(name='Load-2', createStepName='loading',
            region=region, cm3=LoadMagnitude, distributionType=UNIFORM, field='',
            localCsys=None)




    # n=0
    # for loading_z in list_of_z:
    #     if loading_z == list_of_z[LoadZ]:
    #         loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    #         a.ReferencePoint(point=(LoadX, LoadY, loading_z))
    #         r1 = a.referencePoints.values()[0]

    #         model.ConnectorSection(name='warping', translationalType=SLOT)
    #         for i in range(0,number_of_loading_nodes):
    #             wire = a.WirePolyLine(points=((r1, loading_nodes[i]), ), mergeType=IMPRINT, meshable=OFF)
    #         e1 = a.edges


    #         #-------------------------------------------------
    #         #       LOADING
    #         #-----------------------------------------------

    #         refPoints1=(r1, )
    #         region = a.Set(referencePoints=refPoints1, name='loading-%s'%(n))

    #         mdb.models['Model-1'].Moment(name='Load-%s'%(n), createStepName='loading',
    #             region=region, cm3=LoadMagnitude, distributionType=UNIFORM, field='',
    #             localCsys=None)
    #     elif n%5 == 0:
    #         loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    #         a.ReferencePoint(point=(LoadX, LoadY, loading_z))
    #         r1 = a.referencePoints.values()[0]
    #         e1 = a.edges

    #         model.ConnectorSection(name='warping', translationalType=SLOT)
    #         for i in range(0,number_of_loading_nodes):
    #             wire = a.WirePolyLine(points=((r1, loading_nodes[i]), ), mergeType=IMPRINT, meshable=OFF)

    #         #-------------------------------------------------
    #         #       LOADING
    #         #-----------------------------------------------

    #         refPoints1=(r1, )
    #         region = a.Set(referencePoints=refPoints1, name='loading-%s'%(n))

    #         mdb.models['Model-1'].Moment(name='Load-%s'%(n), createStepName='loading',
    #             region=region, cm3=-0.0001, distributionType=UNIFORM, field='',
    #             localCsys=None)

    #     elif n==29:
    #         loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    #         a.ReferencePoint(point=(LoadX, LoadY, loading_z))
    #         r1 = a.referencePoints.values()[0]
    #         e1 = a.edges

    #         model.ConnectorSection(name='warping', translationalType=SLOT)
    #         for i in range(0,number_of_loading_nodes):
    #             wire = a.WirePolyLine(points=((r1, loading_nodes[i]), ), mergeType=IMPRINT, meshable=OFF)

    #         #-------------------------------------------------
    #         #       LOADING
    #         #-----------------------------------------------

    #         refPoints1=(r1, )
    #         region = a.Set(referencePoints=refPoints1, name='loading-%s'%(n))

    #         mdb.models['Model-1'].Moment(name='Load-%s'%(n), createStepName='loading',
    #             region=region, cm3=-0.0001, distributionType=UNIFORM, field='',
    #             localCsys=None)

    #     elif n==31:
    #         loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    #         a.ReferencePoint(point=(LoadX, LoadY, loading_z))
    #         r1 = a.referencePoints.values()[0]
    #         e1 = a.edges

    #         model.ConnectorSection(name='warping', translationalType=SLOT)
    #         for i in range(0,number_of_loading_nodes):
    #             wire = a.WirePolyLine(points=((r1, loading_nodes[i]), ), mergeType=IMPRINT, meshable=OFF)

    #         #-------------------------------------------------
    #         #       LOADING
    #         #-----------------------------------------------

    #         refPoints1=(r1, )
    #         region = a.Set(referencePoints=refPoints1, name='loading-%s'%(n))

    #         mdb.models['Model-1'].Moment(name='Load-%s'%(n), createStepName='loading',
    #             region=region, cm3=-0.0001, distributionType=UNIFORM, field='',
    #             localCsys=None)
    #     else:
    #         pass
    #     n +=1
    # e1 = a.edges
    # a.Set(edges=e1, name='Wire-Set-loading')
    # region=a.sets['Wire-Set-loading']
    # csa = a.SectionAssignment(sectionName='warping', region=region)
    # datums = a.datums.values() # make sure right one is used
    # a.ConnectorOrientation(region=csa.getSet(), localCsys1=datums[1])



    #-------------------------------------------------
    #       JOB
    #-----------------------------------------------

    mdb.Job(name='analysis', model='Model-1', description='',
        type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None,
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)

    myJob = mdb.jobs['analysis']
    myJob.submit(consistencyChecking=OFF)
    myJob.waitForCompletion()

    o3 = session.openOdb( name=folder + '/analysis.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.mdbData.summary()


    odb = session.odbs[folder + '/analysis.odb']
    session.fieldReportOptions.setValues(sort=DESCENDING,
        reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName=folder + '/displacement.csv', append=OFF,
        sortItem='COORD.COOR3', odb=odb, step=0, frame=1, outputPosition=NODAL,
        variable=(('COORD', NODAL), ('U', NODAL), ))

    session.writeFieldReport(fileName=folder +'/stress.csv', append=OFF,
        sortItem='Node Label', odb=odb, step=0, frame=1,
        outputPosition=ELEMENT_NODAL, variable=(('S', INTEGRATION_POINT), ))








if __name__ == '__main__':
    main()

