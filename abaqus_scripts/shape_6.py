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
                E = float(Material[0])*1000000
                G = float(Material[1])*1000000
                v_poisson = float(Material[2])

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
    s1.Line(point1=(-0.01, 0.0), point2=(-0.01, 0.11))
    s1.VerticalConstraint(entity=g[11], addUndoState=False)
    s1.Line(point1=(-0.01, 0.11), point2=(0.21, 0.11))
    s1.HorizontalConstraint(entity=g[12], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)

    s1.Line(point1=(0.21, 0.11), point2=(0.21, -0.2))
    s1.VerticalConstraint(entity=g[13], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)

    s1.Line(point1=(0.21, -0.2), point2=(0.21, -0.21))
    s1.VerticalConstraint(entity=g[14], addUndoState=False)
    s1.ParallelConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
    s1.Line(point1=(0.21, -0.21), point2=(-0.21, -0.21))
    s1.HorizontalConstraint(entity=g[15], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
    s1.Line(point1=(-0.21, -0.21), point2=(-0.21, 0.31))
    s1.VerticalConstraint(entity=g[16], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
    s1.Line(point1=(-0.21, 0.31), point2=(0.4, 0.31))
    s1.HorizontalConstraint(entity=g[17], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)

    s1.Line(point1=(0.4, 0.31), point2=(0.4, 0.29))
    s1.VerticalConstraint(entity=g[18], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[17], entity2=g[18], addUndoState=False)
    s1.Line(point1=(0.4, 0.29), point2=(-0.18500000002794, 0.29))
    s1.HorizontalConstraint(entity=g[19], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[18], entity2=g[19], addUndoState=False)

    s1.Line(point1=(-0.18500000002794, 0.29), point2=(-0.19, -0.19))

    s1.Line(point1=(-0.19, -0.19), point2=(0.19, -0.19))
    s1.HorizontalConstraint(entity=g[21], addUndoState=False)

    s1.Line(point1=(0.19, -0.19), point2=(0.19, 0.09))
    s1.VerticalConstraint(entity=g[22], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[21], entity2=g[22], addUndoState=False)

    s1.Line(point1=(0.19, 0.09), point2=(0.01, 0.09))
    s1.HorizontalConstraint(entity=g[23], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[22], entity2=g[23], addUndoState=False)
    s1.Line(point1=(0.01, 0.09), point2=(0.01, 0.0))
    s1.VerticalConstraint(entity=g[24], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[23], entity2=g[24], addUndoState=False)
    s1.Line(point1=(0.01, 0.0), point2=(-0.01, 0.0))
    s1.HorizontalConstraint(entity=g[25], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[24], entity2=g[25], addUndoState=False)

    s1.delete(objectList=(g[6], g[5], g[7], g[8], g[9], g[10]))

    p = mdb.models['Model-1'].Part(name='part', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['part']
    p.BaseSolidExtrude(sketch=s1, depth=length)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['part']

    del mdb.models['Model-1'].sketches['__profile__']
    #------------------------------------------------------------------------------------
    #               MESH
    #------------------------------------------------------------------------------------


    p = mdb.models['Model-1'].parts['part']
    e = p.edges


    p = mdb.models['Model-1'].parts['part']
    f = p.faces
    p.PartitionFaceByAuto(face=f[14])
    p = mdb.models['Model-1'].parts['part']

    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.001)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1c4 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3b ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.02, deviationFactor=0.1,
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.23928,
        farPlane=12.9643, width=1.14253, height=0.477486, viewOffsetX=-1.35241,
        viewOffsetY=-0.660425)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3f ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.26298,
        farPlane=12.9406, width=0.851018, height=0.355657,
        viewOffsetX=-1.33573, viewOffsetY=-0.872709)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#3a01 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#7fd000 #120000 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['part']
    p.generateMesh()




    # #------------------------------------------------------------------------------------
    # #               SECTION
    # #------------------------------------------------------------------------------------
    c = p.cells
    print(c)
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    SC_section_geometry = p.Set(cells=cells, name='SC_section_geometry')

    model.Material(name='SC-material')
    model.materials['SC-material'].Elastic(type=ENGINEERING_CONSTANTS,
        table=((E, E, E,
                    v_poisson, v_poisson, v_poisson,
                    G, G, G), ))
    model.HomogeneousSolidSection(name='SC-section', material='SC-material', thickness=None)
    ## asigning the section
    p.SectionAssignment(region=SC_section_geometry, sectionName='SC-section', offset=0.0,
            offsetType=MIDDLE_SURFACE, offsetField='',
            thicknessAssignment=FROM_SECTION)
    ##assigning the material orientaion
    orientation=None
    p.MaterialOrientation(region=SC_section_geometry,
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
    a.Instance(name='SC_beam-1', part=p, dependent=ON)
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

