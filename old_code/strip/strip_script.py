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


def main():
    os.chdir(r"E:\temp\strip")
    file = open("lambda.txt", "r")

    sc_str = file.read()
    lamb = float(sc_str)

    file.close()
    os.remove("lambda.txt")

    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(-0.02, 0.5), point2=(0.02, -0.5))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=10.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']


    E = 20000000.0
    G = 0.0212*E/(lamb**2)


    mdb.models['Model-1'].Material(name='variable_lambda')
    mdb.models['Model-1'].materials['variable_lambda'].Elastic(
        type=ENGINEERING_CONSTANTS, table=((E, E, E,0.3, 0.3, 0.3, 10000000.0, G, G), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='plate_section',
        material='variable_lambda', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='whole_plate')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='plate_section', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['Part-1']
    region = p.sets['whole_plate']
    orientation=None
    mdb.models['Model-1'].parts['Part-1'].MaterialOrientation(region=region,
        orientationType=GLOBAL, axis=AXIS_1,
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='',
        stackDirection=STACK_3)

    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()

    a = mdb.models['Model-1'].rootAssembly


    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)

    mdb.models['Model-1'].StaticStep(name='loading', previous='Initial')


    mdb.models['Model-1'].ExpressionField(name='symetric_ramp', localCsys=None,
        description='', expression=' Y +10')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface')
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading',
        region=region, distributionType=FIELD, field='symetric_ramp',
        magnitude=1.0, amplitude=UNSET)

    del mdb.models['Model-1'].loads['Load-1']

    mdb.models['Model-1'].ExpressionField(name='AnalyticalField-2', localCsys=None,
        description='', expression='-4 *Y +1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.surfaces['loading_surface']
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading',
        region=region, distributionType=FIELD, field='symetric_ramp',
        magnitude=1.0, amplitude=UNSET)

    p1 = mdb.models['Model-1'].parts['Part-1']
    p = mdb.models['Model-1'].parts['Part-1']
    s1 = p.features['Solid extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2,
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)

    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    a = mdb.models['Model-1'].rootAssembly

    p1 = mdb.models['Model-1'].parts['Part-1']

    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['Part-1']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[5], sketchUpEdge=e[2],
        sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 0.0))
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0,
        gridSpacing=0.05, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['Model-1'].parts['Part-1']
    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
    s.Line(point1=(-0.02, 0.0), point2=(0.02, 0.0))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[4], entity2=g[4], addUndoState=False)
    s.EqualDistanceConstraint(entity1=v[3], entity2=v[2], midpoint=v[4],
        addUndoState=False)
    s.CoincidentConstraint(entity1=v[5], entity2=g[2], addUndoState=False)
    s.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[5],
        addUndoState=False)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    pickedFaces = f.getSequenceFromMask(mask=('[#20 ]', ), )
    e1, d2 = p.edges, p.datums
    p.PartitionFaceBySketch(sketchUpEdge=e1[2], faces=pickedFaces, sketch=s)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']

    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()

    p1 = mdb.models['Model-1'].parts['Part-1']

    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()

    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()

    del mdb.models['Model-1'].loads['Load-1']
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface_upper')
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading',
        region=region, distributionType=FIELD, field='AnalyticalField-2',
        magnitude=1.0, amplitude=UNSET)

    mdb.models['Model-1'].ExpressionField(name='AnalyticalField-3', localCsys=None,
        description='', expression='4*Y+1')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface_lower')
    mdb.models['Model-1'].Pressure(name='Load-2', createStepName='loading',
        region=region, distributionType=FIELD, field='AnalyticalField-3',
        magnitude=1.0, amplitude=UNSET)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
            'S', 'SEQUT', 'PE', 'PEEQ', 'PEMAG', 'LE', 'TE', 'TEEQ', 'TEVOL',
            'EEQUT', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'COORD', 'MVF'))



    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
        numGPUs=1)
    myJob = mdb.jobs['Job-1']
    myJob.submit(consistencyChecking=OFF)
    myJob.waitForCompletion()




    o3 = session.openOdb(name='E:/temp/strip/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.mdbData.summary()

    odb = session.odbs['E:/temp/strip/Job-1.odb']
    session.fieldReportOptions.setValues(sort=ASCENDING,
        reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName='abaqus.csv', append=OFF,
            sortItem='COORD.COOR3', odb=odb, step=0, frame=1, outputPosition=NODAL,
            variable=(('COORD', NODAL, ((COMPONENT, 'COOR1'), (COMPONENT, 'COOR2'),
            (COMPONENT, 'COOR3'), )), ('S', INTEGRATION_POINT, ((INVARIANT,
            'Mises'), )), ))

if __name__ == '__main__':
    main()

