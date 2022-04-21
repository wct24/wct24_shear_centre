# -*- coding: mbcs -*-
# Do not delete the following import lines
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
import time


def main():
    os.chdir(r"E:\temp\semi-circle")
    file = open("sample.txt", "r")
    sc_str = file.read()
    sc = float(sc_str)

    file.close()
    os.remove("sample.txt")



    #sketch the section
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
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
    p = mdb.models['Model-1'].Part(name='section', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['section']
    p.BaseSolidExtrude(sketch=s, depth=3.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['section']

    del mdb.models['Model-1'].sketches['__profile__']
    p = mdb.models['Model-1'].parts['section']

    # Sketch the endplate
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 0.41))
    s1.Line(point1=(0.0, 0.41), point2=(0.0, -0.41))
    s1.VerticalConstraint(entity=g[3], addUndoState=False)
    s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s1.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
    s1.rectangle(point1=(0.0, 0.1), point2=(sc, -0.1))
    s1.autoTrimCurve(curve1=g[2], point1=(-0.3648801445961, 0.197754979133606))
    s1.autoTrimCurve(curve1=g[3], point1=(-0.00442303158342838,0.0543809235095978))
    s1.autoTrimCurve(curve1=g[7], point1=(0.128019914031029, 0.101864390075207))
    s1.autoTrimCurve(curve1=g[8], point1=(0.400449275970459, 0.0600906535983086))
    s1.autoTrimCurve(curve1=g[5], point1=(0.292911350727081, -0.0926816239953041))


    p = mdb.models['Model-1'].Part(name='end_plate', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['end_plate']
    p.BaseSolidExtrude(sketch=s1, depth=0.1)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['end_plate']
    del mdb.models['Model-1'].sketches['__profile__']


    #material
    mdb.models['Model-1'].Material(name='normal')
    mdb.models['Model-1'].materials['normal'].Elastic(table=((2e7, 0.3), ))
    mdb.models['Model-1'].Material(name='plate_material')
    mdb.models['Model-1'].materials['plate_material'].Elastic(
        type=ENGINEERING_CONSTANTS, table=((2000000000000.0, 2000000000000.0,
        2000000000000.0, 0.3, 0.3, 0.2, 10000000000, 1.0, 1.0), ))
    mdb.models['Model-1'].Material(name='high_lambda')
    mdb.models['Model-1'].materials['high_lambda'].Elastic(
        type=ENGINEERING_CONSTANTS, table=((2e7, 2e7,
        2e7, 0.34, 0.34, 0.4, 1e9, 1e9, 1e9), ))



    mdb.models['Model-1'].HomogeneousSolidSection(name='section', material='normal', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='end_plate', material='plate_material', thickness=None)
    p = mdb.models['Model-1'].parts['end_plate']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    orientation=None
    mdb.models['Model-1'].parts['end_plate'].MaterialOrientation(
        region=region, orientationType=GLOBAL, axis=AXIS_1,
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='',
        stackDirection=STACK_3)
    p = mdb.models['Model-1'].parts['end_plate']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='endplate_geometry')
    p = mdb.models['Model-1'].parts['end_plate']
    p.SectionAssignment(region=region, sectionName='end_plate', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

    p = mdb.models['Model-1'].parts['end_plate']
    region = p.sets['endplate_geometry']
    p = mdb.models['Model-1'].parts['end_plate']
    p.SectionAssignment(region=region, sectionName='end_plate', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

    del mdb.models['Model-1'].parts['end_plate'].sectionAssignments[0]
    p1 = mdb.models['Model-1'].parts['section']
    p = mdb.models['Model-1'].parts['section']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='section_geometry')
    orientation=None
    mdb.models['Model-1'].parts['section'].MaterialOrientation(
        region=region, orientationType=GLOBAL, axis=AXIS_1,
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='',
        stackDirection=STACK_3)
    p = mdb.models['Model-1'].parts['section']
    p.SectionAssignment(region=region, sectionName='section', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

    p1 = mdb.models['Model-1'].parts['section']

    p1 = mdb.models['Model-1'].parts['end_plate']

    p = mdb.models['Model-1'].parts['end_plate']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['end_plate']
    p.generateMesh()
    p1 = mdb.models['Model-1'].parts['section']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['section']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['section']
    p.generateMesh()

    a = mdb.models['Model-1'].rootAssembly

    mdb.models['Model-1'].StaticStep(name='loading',
        previous='Initial', description='applying a load at the shear centre',
        initialInc=0.1)

    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['end_plate']
    a.Instance(name='end_plate-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.fitView()
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['section']
    a.Instance(name='section-1', part=p, dependent=ON)

    a = mdb.models['Model-1'].rootAssembly
    v11 = a.instances['end_plate-1'].vertices
    v12 = a.instances['section-1'].vertices
    a.CoincidentPoint(movablePoint=v11[3], fixedPoint=v12[0])

    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['end_plate-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#80 ]', ), )
    region1=a.Surface(side1Faces=side1Faces1, name='inner_surf_plate')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['section-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
    region2=a.Surface(side1Faces=side1Faces1, name='c_3m')
    mdb.models['Model-1'].Tie(name='Constraint-1', master=region1,
        slave=region2, positionToleranceMethod=COMPUTED, adjust=ON,
        tieRotations=ON, thickness=ON)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['section-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#0:50 #fff00000 #7fff #0:50 #3ffffff8 ]', ), )
    a.Set(nodes=nodes1, name='wall_nodes_all')
    number_of_nodes = len(mdb.models['Model-1'].rootAssembly.allSets['wall_nodes_all'].nodes)

    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['section-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#0:51 #ffff8000 #ffffffff:50 #3fffffff ]', ), )
    a.Set(nodes=nodes1, name='outside_nodes')
    regionDef=mdb.models['Model-1'].rootAssembly.sets['outside_nodes']
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2',
        createStepName='loading', variables=('COORD', 'U'), region=regionDef,
        sectionPoints=DEFAULT, rebar=EXCLUDE)


    terms_1 = [0 for i in range( number_of_nodes)]
    terms_2 = [0 for i in range( number_of_nodes)]
    terms_3 = [0 for i in range( number_of_nodes)]

    for i in range( number_of_nodes):
        a = mdb.models['Model-1'].rootAssembly
        node = mdb.models['Model-1'].rootAssembly.allSets['wall_nodes_all'].nodes[i]
        #print(node.instanceName,node.label)
        a.SetFromNodeLabels(nodeLabels=((node.instanceName, (node.label,)),), name='wall-%s'%(i))
        terms_1[i] = [1.0,'wall-%s'%(i), 3]
        (x,y,z) = node.coordinates
        terms_2[i] = [y,'wall-%s'%(i), 3]
        terms_3[i] = [(x-0.255),'wall-%s'%(i), 3]
    #need to eliminate some terms that have alredy been used:
    def node_elimination(node_1, node_2, node_3):
        elmination_term = terms_2[node_1][0]
        for i in range( number_of_nodes):
            terms_2[i][0] = terms_2[i][0]-elmination_term

        elmination_term = terms_3[node_1][0]
        for i in range( number_of_nodes):
            terms_3[i][0] = terms_3[i][0]-elmination_term

        coefficient_node_2 = terms_2[node_2][0]
        for i in range( number_of_nodes):
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

    node_elimination(41,53,27)


    mdb.models['Model-1'].Equation(name='sum_of_u3', terms=terms_1)
    mdb.models['Model-1'].Equation(name='moment_x_u3', terms=terms_2)
    mdb.models['Model-1'].Equation(name='moment_y_u3', terms=terms_3)

    #Load:
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['end_plate-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Set(vertices=verts1, name='shear_centre_point')
    mdb.models['Model-1'].ConcentratedForce(name='Load-1',
        createStepName='loading', region=region, cf2=-10.0,
        distributionType=UNIFORM, field='', localCsys=None)


    #boundary conditions
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['wall_nodes_all']
    mdb.models['Model-1'].DisplacementBC(name='BC-1',
        createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET,
        ur1=SET, ur2=SET, ur3=SET, amplitude=UNSET,
        distributionType=UNIFORM, fieldName='', localCsys=None)
    mdb.Job(name='analysis', model='Model-1', description='',
        type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None,
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB)

    myJob = mdb.jobs['analysis']
    myJob.submit(consistencyChecking=OFF)
    myJob.waitForCompletion()



    o3 = session.openOdb( name='E:/temp/semi-circle/analysis.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.mdbData.summary()


    odb = session.odbs['E:/temp/semi-circle/analysis.odb']
    session.fieldReportOptions.setValues(sort=DESCENDING,
        reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName='E:/temp/semi-circle/analysis.csv', append=OFF,
        sortItem='COORD.COOR3', odb=odb, step=0, frame=6, outputPosition=NODAL,
        variable=(('COORD', NODAL), ('U', NODAL), ))


if __name__ == '__main__':
    main()
