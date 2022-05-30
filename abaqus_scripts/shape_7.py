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


    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.797034,
        farPlane=1.08858, width=2.17075, height=1.01856, cameraPosition=(
        -0.0231676, 0.132199, 0.942809), cameraTarget=(-0.0231676, 0.132199,
        0))
    s.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, 0.4), point2=(0.0, -0.4),
        direction=CLOCKWISE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914143,
        farPlane=0.971475, width=0.353102, height=0.165683, cameraPosition=(
        0.340686, -0.0152572, 0.942809), cameraTarget=(0.340686, -0.0152572,
        0))
    s.Arc3Points(point1=(0.0, 0.41), point2=(0.0, -0.41), point3=(
        0.412606418132782, 0.0193976201117039))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.908058,
        farPlane=0.977561, width=0.428066, height=0.200857, cameraPosition=(
        0.25893, -0.00494628, 0.942809), cameraTarget=(0.25893, -0.00494628,
        0))
    s.Arc3Points(point1=(0.0, 0.39), point2=(0.0, -0.39), point3=(0.39, 0.02))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.803878,
        farPlane=1.08174, width=1.93678, height=0.908778, cameraPosition=(
        -0.157778, -0.0127311, 0.942809), cameraTarget=(-0.157778, -0.0127311,
        0))
    s.delete(objectList=(g[2], ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.833002,
        farPlane=1.05262, width=1.35259, height=0.634665, cameraPosition=(
        -0.121323, 0.234666, 0.942809), cameraTarget=(-0.121323, 0.234666, 0))
    s.rectangle(point1=(0.0, -0.41), point2=(-0.02, 0.41))
    s.autoTrimCurve(curve1=g[5], point1=(0.00229237228631973, 0.400285542011261))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.882199,
        farPlane=1.00342, width=0.746594, height=0.350317, cameraPosition=(
        -0.0508321, -0.357238, 0.942809), cameraTarget=(-0.0508321, -0.357238,
        0))
    s.autoTrimCurve(curve1=g[9], point1=(-0.00122997164726257, -0.402132749557495))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.648681,
        farPlane=1.23694, width=4.10031, height=1.92395, cameraPosition=(
        -0.30632, -0.0456021, 0.942809), cameraTarget=(-0.30632, -0.0456021,
        0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=3.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.51035,
        farPlane=8.2819, width=1.94982, height=0.880874, viewOffsetX=-0.589305,
        viewOffsetY=-0.140395)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46631,
        farPlane=8.32594, width=2.80376, height=1.26983, viewOffsetX=-0.296069,
        viewOffsetY=-0.0733024)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#11491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.1,
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.45483,
        farPlane=8.33742, width=2.63, height=1.19114, viewOffsetX=-0.333459,
        viewOffsetY=-0.070095)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
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




