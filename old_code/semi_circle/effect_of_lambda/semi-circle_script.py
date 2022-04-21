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
    os.chdir(r"E:\temp\SC")
    file = open("sample.txt", "r")
    sc_str = file.read()
    sc = float(sc_str)
    print(sc)
    file.close()
    os.remove("sample.txt")

    file = open("lambda.txt", "r")
    loading_z_str = file.read()
    lambda_position = int(float(loading_z_str))
    file.close()
    list_of_lambda = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    lambda_ =list_of_lambda[lambda_position]

    #------------------------------------------------------------------------------------
    #                GEOMETRY
    #------------------------------------------------------------------------------------
    model = mdb.models['Model-1']

    s = model.ConstrainedSketch(name='__profile__', sheetSize=1.0)

    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, 0.39), point2=(0.0, -0.39),
        direction=CLOCKWISE)
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, 0.41), point2=(0.0, -0.41),
        direction=CLOCKWISE)
    s.Line(point1=(0.0, 0.39), point2=(0.0, 0.41))
    s.VerticalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
    s.Line(point1=(0.0, -0.41), point2=(0.0, -0.39))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[5], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='part', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)

    part = mdb.models['Model-1'].parts['part']
    part.BaseSolidExtrude(sketch=s, depth=3.0)
    s.unsetPrimaryObject()

    del mdb.models['Model-1'].sketches['__profile__']
    #------------------------------------------------------------------------------------
    #               MESH
    #------------------------------------------------------------------------------------
    part.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.01)
    part.generateMesh()
    #------------------------------------------------------------------------------------
    #               SECTION
    #------------------------------------------------------------------------------------
    c = part.cells
    print(c)
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    SC_section_geometry = part.Set(cells=cells, name='SC_section_geometry')


    lambda_material = 1.5187
    G = 210000000000.0/((lambda_/lambda_material)**2)
    model.Material(name='SC-material')
    model.materials['SC-material'].Elastic(type=ENGINEERING_CONSTANTS,
        table=((210000000000.0, 210000000000.0, 210000000000.0,
                    0.3, 0.3, 0.3,
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
    #------------------------------------------------------------------------------------
    #               Assembly
    #------------------------------------------------------------------------------------
    a = model.rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    a.Instance(name='SC_beam-1', part=part, dependent=ON)

    # ----------------------------------
    # Boundary Conditions ANd Load
    # ---------------------------------
    n1 = a.instances['SC_beam-1'].nodes #all nodes in the instance I beam
    loading_position = 0
    list_of_z = get_z_coordinates(n1)
    loading_z = list_of_z[loading_position]
    loading_nodes, number_of_loading_nodes = get_nodes(loading_z,n1)
    wall_nodes, number_of_wall_nodes = get_nodes(0.0,n1)

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


    a.ReferencePoint(point=(sc, 0.0, loading_z))
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

    #moment
    # mdb.models['Model-1'].Moment(name='Load-2', createStepName='loading',
    #     region=region, cm3=-100.0, distributionType=UNIFORM, field='',
    #     localCsys=None)
    # #force
    mdb.models['Model-1'].ConcentratedForce(name='Load-1',
        createStepName='loading', region=region, cf2=-1000.0,
        distributionType=UNIFORM, field='', localCsys=None)

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

    o3 = session.openOdb( name='E:/temp/SC/analysis.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.mdbData.summary()

    odb = session.odbs['E:/temp/SC/analysis.odb']
    session.fieldReportOptions.setValues(sort=DESCENDING,
        reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName='E:/temp/SC/analysis.csv', append=OFF,
        sortItem='COORD.COOR3', odb=odb, step=0, frame=1, outputPosition=NODAL,
        variable=(('COORD', NODAL), ('U', NODAL), ))

if __name__ == '__main__':
    main()

