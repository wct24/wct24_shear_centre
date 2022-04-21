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
    beam = 1
    with open("I-beam.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i == beam:
                h_beam  = float(row[1])/1000
                b_beam  = float(row[2])/1000
                tw_beam = float(row[3])/1000
                tf_beam = float(row[4])/1000
                r_beam  = float(row[5])/1000
                break


    os.chdir(r"E:\temp\I")
    #------------------------------------------------------------------------------------
    #                GEOMETRY
    #------------------------------------------------------------------------------------
    model = mdb.models['Model-1']

    s = model.ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    #step 1
    d_beam = (h_beam-2*tf_beam)/2
    s.rectangle(point1=(-tw_beam/2, -d_beam), point2=(tw_beam/2, d_beam))
    #step 2
    s.rectangle(point1=(-b_beam/2, d_beam), point2=(b_beam/2, h_beam/2))
    #step 3
    s.rectangle(point1=(-b_beam/2, -d_beam), point2=(b_beam/2, -h_beam/2))

    #Step 4
    s.autoTrimCurve(curve1=g[5], point1=(0.0, -d_beam))
    s.autoTrimCurve(curve1=g[13], point1=(0.0,  -d_beam))
    s.autoTrimCurve(curve1=g[3], point1=(0.0, d_beam))
    s.autoTrimCurve(curve1=g[9], point1=(0.0, d_beam))

    #step 5
    s.FilletByRadius(radius=r_beam, curve1=g[15], nearPoint1=(-tw_beam/2-0.001 ,
        -d_beam), curve2=g[2], nearPoint2=(tw_beam/2,-d_beam+0.001))
    s.FilletByRadius(radius=r_beam, curve1=g[14], nearPoint1=(tw_beam/2+0.001,
        -d_beam), curve2=g[4], nearPoint2=(tw_beam/2,
        -d_beam+0.001))
    s.FilletByRadius(radius=r_beam, curve1=g[4], nearPoint1=(tw_beam/2,
        d_beam/2-0.001), curve2=g[16], nearPoint2=(tw_beam/2+0.001,
        d_beam/2))
    s.FilletByRadius(radius=r_beam, curve1=g[2], nearPoint1=(-tw_beam/2,
        d_beam/2-0.001), curve2=g[17], nearPoint2=(-tw_beam/2-0.001,
        d_beam/2))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    part = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=1.0)
    s.unsetPrimaryObject()
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    #------------------------------------------------------------------------------------
    #               MESH
    #------------------------------------------------------------------------------------
    part.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.001)
    part.generateMesh()
    #------------------------------------------------------------------------------------
    #               SECTION
    #------------------------------------------------------------------------------------
    c = part.cells
    print(c)
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    I_section_geometry = part.Set(cells=cells, name='I_section_geometry')

    model.Material(name='I-material')
    model.materials['I-material'].Elastic(type=ENGINEERING_CONSTANTS,
        table=((210000000000.0, 210000000000.0, 210000000000.0,
                    0.3, 0.3, 0.3,
                    81000000000.0, 81000000000.0, 81000000000.0), ))
    model.HomogeneousSolidSection(name='I-section', material='I-material', thickness=None)
    ## asigning the section
    part.SectionAssignment(region=I_section_geometry, sectionName='I-section', offset=0.0,
            offsetType=MIDDLE_SURFACE, offsetField='',
            thicknessAssignment=FROM_SECTION)
    ##assigning the material orientaion
    orientation=None
    part.MaterialOrientation(region=I_section_geometry,
        orientationType=GLOBAL, axis=AXIS_1,
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='',
        stackDirection=STACK_3)
    #------------------------------------------------------------------------------------
    #               FIELD OUTPUT REQUEST
    #------------------------------------------------------------------------------------
    model.StaticStep(name='loading', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    model.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'MISES', 'NFORC','SEQUT', 'COORD'))
    #------------------------------------------------------------------------------------
    #               Assembly
    #------------------------------------------------------------------------------------
    a = model.rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    a.Instance(name='I_beam-1', part=part, dependent=ON)

    # ----------------------------------
    # Boundary Conditions ANd Load
    # ---------------------------------


    n1 = a.instances['I_beam-1'].nodes #all nodes in the instance I beam
    list_of_z = get_z_coordinates(n1)
    wall_nodes, number_of_wall_nodes = get_nodes(0.0,n1)
    loading_nodes, number_of_loading_nodes = get_nodes(list_of_z[0],n1)
    
    model.DisplacementBC(name='BC-1', createStepName='Initial',
        region=a.sets['nodes_at_z_0mm'], u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
        amplitude=UNSET, distributionType=UNIFORM, fieldName='',
        localCsys=None)
    #No warping allowed
    # a.Set(nodes=n1, name ="all_nodes")
    model.DisplacementBC(name='BC-2', createStepName='Initial',
        region=a.sets['nodes_at_z_1000mm'], u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
        amplitude=UNSET, distributionType=UNIFORM, fieldName='',
        localCsys=None)

    v1 = a.instances['I_beam-1'].vertices
    e1 = a.instances['I_beam-1'].edges
    Csys = a.DatumCsysByThreePoints(origin=v1[4], point1=v1[5], name='end',
        coordSysType=CARTESIAN,
        point2=a.instances['I_beam-1'].InterestingPoint(edge=e1[8],
        rule=MIDDLE))


    a.ReferencePoint(point=(0.0, 0.0, 1.0))
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
    mdb.models['Model-1'].Moment(name='Load-2', createStepName='loading',
        region=region, cm3=10000.0, distributionType=UNIFORM, field='',
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

    o3 = session.openOdb( name='E:/temp/I/analysis.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.mdbData.summary()

    odb = session.odbs['E:/temp/I/analysis.odb']
    session.fieldReportOptions.setValues(sort=DESCENDING,
        reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName='E:/temp/I/analysis.csv', append=OFF,
        sortItem='COORD.COOR3', odb=odb, step=0, frame=1, outputPosition=NODAL,
        variable=(('COORD', NODAL), ('NFORC.NFOR3', NODAL), ))

if __name__ == '__main__':
    main()

