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






    # v1 = a.instances['SC_beam-1'].vertices
    # e1 = a.instances['SC_beam-1'].edges
    # Csys = a.DatumCsysByThreePoints(origin=v1[4], point1=v1[5], name='end',
    #     coordSysType=CARTESIAN,
    #     point2=a.instances['SC_beam-1'].InterestingPoint(edge=e1[8],
    #     rule=MIDDLE))

    Csys = a.DatumCsysByThreePoints(name='end', coordSysType=CARTESIAN, origin=(
        0.0, 0.0, 3.0), point1=(0.0, 0.0, 0.0), line2=(0.0, 9.0, 0.0),
        isDependent=False)




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




