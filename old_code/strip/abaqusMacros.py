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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.68946, 
        farPlane=1.19616, width=3.12073, height=1.24651, cameraPosition=(
        0.222081, 0.235918, 0.942809), cameraTarget=(0.222081, 0.235918, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.222081, 
        -0.238573, 0.942809), cameraTarget=(0.222081, -0.238573, 0))
    s.rectangle(point1=(-0.02, 0.5), point2=(0.02, -0.5))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.656085, 
        farPlane=1.22953, width=3.53183, height=1.41072, cameraPosition=(
        0.206156, -0.11746, 0.942809), cameraTarget=(0.206156, -0.11746, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=3.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.23568, 
        farPlane=8.54897, width=6.00926, height=2.40027, viewOffsetX=-0.293275, 
        viewOffsetY=-0.0994449)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.26471, 
        farPlane=8.51994, width=6.04258, height=2.41358, cameraPosition=(
        3.92244, 3.90881, 5.6066), cameraUpVector=(-0.564366, 0.577206, 
        -0.59019), cameraTarget=(-0.0568441, -0.0704709, 1.62731), 
        viewOffsetX=-0.294901, viewOffsetY=-0.0999963)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.19121, 
        farPlane=8.84525, width=5.95822, height=2.37989, cameraPosition=(
        3.24588, 3.18457, 6.8482), cameraUpVector=(-0.398082, 0.675714, 
        -0.620437), cameraTarget=(0.0114912, -0.0530023, 1.69447), 
        viewOffsetX=-0.290784, viewOffsetY=-0.0986003)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='variable_lambda')
    mdb.models['Model-1'].materials['variable_lambda'].Elastic(
        type=ENGINEERING_CONSTANTS, table=((20000000.0, 20000000.0, 20000000.0, 
        0.3, 0.3, 0.3, 10000000.0, 1000000.0, 10000000.0), ))
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
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.29104, 
        farPlane=8.74542, width=1.99384, height=1.97599, viewOffsetX=-0.252593, 
        viewOffsetY=0.0194875)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.35288, 
        farPlane=8.43177, width=2.07222, height=2.04084, viewOffsetX=0.0509882, 
        viewOffsetY=0.0218009)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='loading', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.37513, 
        farPlane=8.40952, width=1.73538, height=1.7091, viewOffsetX=-0.108166, 
        viewOffsetY=-0.0682783)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.33171, 
        farPlane=8.48156, width=1.72136, height=1.6953, cameraPosition=(
        3.25545, 4.2645, 5.85219), cameraUpVector=(-0.527148, 0.523806, 
        -0.669136), cameraTarget=(-0.0490274, -0.0674335, 1.63095), 
        viewOffsetX=-0.107292, viewOffsetY=-0.0677268)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.25834, 
        farPlane=8.94553, width=1.69767, height=1.67197, cameraPosition=(
        -1.87971, 2.73607, 7.78209), cameraUpVector=(0.387297, 0.705958, 
        -0.592979), cameraTarget=(0.0188639, -0.0862897, 1.78761), 
        viewOffsetX=-0.105815, viewOffsetY=-0.0667948)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.31909, 
        farPlane=8.82205, width=1.71729, height=1.69129, cameraPosition=(
        3.19558, 1.82714, 7.53975), cameraUpVector=(-0.0239193, 0.771541, 
        -0.63573), cameraTarget=(0.149721, -0.123751, 1.67282), 
        viewOffsetX=-0.107037, viewOffsetY=-0.0675665)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.01531, 
        farPlane=7.9019, width=1.94207, height=1.91267, cameraPosition=(
        6.22185, 2.48991, 3.37949), cameraUpVector=(-0.547613, 0.716123, 
        -0.432768), cameraTarget=(0.120769, -0.105308, 1.49646), 
        viewOffsetX=-0.121047, viewOffsetY=-0.0764104)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.88843, 
        farPlane=8.7205, width=1.57825, height=1.55436, cameraPosition=(
        0.712758, 0.888037, -5.21013), cameraUpVector=(-0.272007, 0.859355, 
        0.433038), cameraTarget=(-0.115943, -0.111724, 1.55876), 
        viewOffsetX=-0.0983706, viewOffsetY=-0.062096)


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.82788, 
        farPlane=8.78107, width=2.12385, height=2.0917, viewOffsetX=0.0414388, 
        viewOffsetY=-0.113814)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.85676, 
        farPlane=8.75218, width=2.09656, height=2.06482, viewOffsetX=0.0416868, 
        viewOffsetY=-0.114495)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.84209, 
        farPlane=8.73263, width=2.09023, height=2.05858, cameraPosition=(
        1.09525, 1.128, -5.10436), cameraUpVector=(-0.288692, 0.845322, 
        0.449541), cameraTarget=(-0.121009, -0.116148, 1.56474), 
        viewOffsetX=0.0415609, viewOffsetY=-0.114149)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.10969, 
        farPlane=8.27589, width=2.20575, height=2.17235, cameraPosition=(
        4.4659, 1.54037, -3.24228), cameraUpVector=(-0.338426, 0.831342, 
        0.440838), cameraTarget=(-0.166436, -0.13761, 1.57746), 
        viewOffsetX=0.0438578, viewOffsetY=-0.120457)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.8471, 
        farPlane=8.65652, width=2.09239, height=2.06072, cameraPosition=(
        2.2338, 1.25179, -4.74839), cameraUpVector=(-0.299236, 0.848984, 
        0.435527), cameraTarget=(-0.101079, -0.116793, 1.59033), 
        viewOffsetX=0.0416039, viewOffsetY=-0.114267)
    mdb.models['Model-1'].ExpressionField(name='symetric_ramp', localCsys=None, 
        description='', expression=' Y +10')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface')
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading', 
        region=region, distributionType=FIELD, field='symetric_ramp', 
        magnitude=1.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.02823, 
        farPlane=8.47539, width=1.32312, height=1.30309, viewOffsetX=0.341264, 
        viewOffsetY=-0.138484)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.6765, 
        farPlane=6.92904, width=1.49371, height=1.47109, cameraPosition=(
        6.10421, 1.25179, 0.545279), cameraUpVector=(-0.526968, 0.848984, 
        -0.0391199), cameraTarget=(-0.547729, -0.116793, 1.72115), 
        viewOffsetX=0.385261, viewOffsetY=-0.156338)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.32463, 
        farPlane=7.2809, width=2.99249, height=2.94719, viewOffsetX=0.0416689, 
        viewOffsetY=-0.530887)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.54248, 
        farPlane=7.44062, width=3.11493, height=3.06777, cameraPosition=(
        6.10421, 1.1522, -0.67718), cameraTarget=(-0.547729, -0.216381, 
        0.498691), viewOffsetX=0.0433737, viewOffsetY=-0.552607)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.64236, 
        farPlane=7.34074, width=2.63383, height=2.59396, viewOffsetX=0.422882, 
        viewOffsetY=-0.497696)
    session.viewports['Viewport: 1'].view.setValues(width=2.79644, height=2.7541, 
        cameraPosition=(-0.107018, 5.73305, 0.0117876), cameraUpVector=(0, 0, 
        1), cameraTarget=(-0.107018, -0.758498, 0.0117876), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6.38453, 
        -0.758498, 0.0117876), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.11936, 
        farPlane=6.6497, width=1.36354, height=1.3429, viewOffsetX=0.0426551, 
        viewOffsetY=0.714911)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.10965, 
        farPlane=9.56054, width=1.36138, height=1.34077, cameraPosition=(
        2.10556, -0.251381, -6.1015), cameraUpVector=(-0.100672, 0.993718, 
        0.0488809), cameraTarget=(0.0838121, -0.758609, 0.0462987), 
        viewOffsetX=0.0425875, viewOffsetY=0.713777)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.09761, 
        farPlane=9.74785, width=1.3587, height=1.33813, cameraPosition=(0.7724, 
        2.01729, -6.18794), cameraUpVector=(-0.0698605, 0.932473, 0.35442), 
        cameraTarget=(-0.166258, -0.326165, -0.20736), viewOffsetX=0.0425036, 
        viewOffsetY=0.71237)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.16001, 
        farPlane=9.68545, width=1.09823, height=1.08161, 
        viewOffsetX=-0.0109787, viewOffsetY=0.497262)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    del mdb.models['Model-1'].loads['Load-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.18298, 
        farPlane=9.66248, width=0.860644, height=0.847614, 
        viewOffsetX=-0.0732055, viewOffsetY=0.439454)
    mdb.models['Model-1'].ExpressionField(name='AnalyticalField-2', localCsys=None, 
        description='', expression='-4 *Y +1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.surfaces['loading_surface']
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading', 
        region=region, distributionType=FIELD, field='symetric_ramp', 
        magnitude=1.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.41055, 
        farPlane=9.01558, width=0.89232, height=0.878811, cameraPosition=(
        5.18268, 1.65763, -4.05191), cameraUpVector=(-0.0821723, 0.92872, 
        0.361563), cameraTarget=(0.657227, -0.373098, 0.135766), 
        viewOffsetX=-0.0758999, viewOffsetY=0.455628)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.43004, 
        farPlane=9.1661, width=0.895034, height=0.881483, cameraPosition=(
        4.83208, 0.261789, -4.68677), cameraUpVector=(-0.0576624, 0.989453, 
        0.13288), cameraTarget=(0.587154, -0.634096, 0.142131), 
        viewOffsetX=-0.0761307, viewOffsetY=0.457013)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.20213, 
        farPlane=9.39403, width=2.21089, height=2.17742, viewOffsetX=-0.480125, 
        viewOffsetY=0.42738)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.85922, 
        farPlane=9.30332, width=2.08866, height=2.05703, cameraPosition=(
        -4.82378, 0.660528, -4.39517), cameraUpVector=(0.00677137, 0.970317, 
        0.241742), cameraTarget=(-1.09151, -0.647987, 0.752472), 
        viewOffsetX=-0.45358, viewOffsetY=0.40375)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.59676, 
        farPlane=9.55551, width=1.9951, height=1.9649, cameraPosition=(
        -0.810932, 1.3397, -5.98626), cameraUpVector=(-0.34059, 0.889785, 
        0.303777), cameraTarget=(-0.419691, -0.619245, 0.190286), 
        viewOffsetX=-0.433262, viewOffsetY=0.385665)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.91751, 
        farPlane=9.47165, width=2.10945, height=2.07751, cameraPosition=(
        3.05115, -1.78884, -5.41254), cameraUpVector=(-0.284191, 0.924478, 
        -0.254118), cameraTarget=(0.153091, -1.09447, 0.354551), 
        viewOffsetX=-0.458093, viewOffsetY=0.407768)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.14781, 
        farPlane=9.08973, width=2.19155, height=2.15837, cameraPosition=(
        5.40407, 0.473218, -3.94146), cameraUpVector=(-0.180093, 0.982407, 
        0.0494223), cameraTarget=(0.577183, -0.622915, 0.258526), 
        viewOffsetX=-0.475921, viewOffsetY=0.423638)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.98893, 
        farPlane=9.2486, width=3.10732, height=3.06028, viewOffsetX=-0.779631, 
        viewOffsetY=0.405631)
    session.viewports['Viewport: 1'].view.setValues(width=2.64759, height=2.6075, 
        cameraPosition=(0.284769, 7.39157, 1.76798), cameraUpVector=(0, 0, 1), 
        cameraTarget=(0.284769, -0.227194, 1.76798), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.284769, 
        -0.227194, 9.38674), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.284769, 
        -0.227194, -5.85078))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.90353, 
        -0.227194, 1.76798))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.69634, 
        farPlane=9.11072, width=5.90339, height=5.81401, viewOffsetX=-1.04363, 
        viewOffsetY=-0.613503)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.74674, 
        farPlane=9.06032, width=5.94782, height=5.85777, cameraPosition=(
        7.90353, -0.227194, 0.178878), cameraTarget=(0.284769, -0.227194, 
        0.178878), viewOffsetX=-1.05148, viewOffsetY=-0.61812)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.65618, 
        farPlane=8.15088, width=1.12191, height=1.10493, viewOffsetX=0.283304, 
        viewOffsetY=0.138271)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-1']
    s1 = p.features['Solid extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.81931, 
        farPlane=6.30923, width=1.36554, height=1.34486, cameraPosition=(
        0.0155741, -0.000425771, 6.06427), cameraTarget=(0.0155741, 
        -0.000425771, 0))
    s2.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__edit__']
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.61043, 
        farPlane=8.19663, width=1.34817, height=1.32776, viewOffsetX=-0.233946, 
        viewOffsetY=0.447082)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.62571, 
        farPlane=8.18135, width=1.35088, height=1.33043, cameraPosition=(
        7.90353, -0.593508, 0.32641), cameraTarget=(0.284769, -0.593508, 
        0.32641), viewOffsetX=-0.234416, viewOffsetY=0.447979)
    mdb.models['Model-1'].loads['Load-1'].setValues(field='AnalyticalField-2')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.46255, 
        farPlane=8.34451, width=2.08063, height=2.04913, viewOffsetX=-0.502512, 
        viewOffsetY=0.309115)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.69957, 
        farPlane=10.3411, width=1.8679, height=1.83962, cameraPosition=(
        2.96167, -2.22682, -6.22943), cameraUpVector=(0.452896, 0.891493, 
        -0.0111789), cameraTarget=(-0.432423, -0.42008, 0.347906), 
        viewOffsetX=-0.451135, viewOffsetY=0.277511)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.76681, 
        farPlane=10.2071, width=1.88665, height=1.85808, cameraPosition=(
        3.09846, 0.347805, -6.44641), cameraUpVector=(0.530664, 0.786517, 
        0.315892), cameraTarget=(-0.411287, 0.00343382, 0.307), 
        viewOffsetX=-0.455663, viewOffsetY=0.280296)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.96007, 
        farPlane=10.0138, width=0.816039, height=0.803685, 
        viewOffsetX=-0.209736, viewOffsetY=0.301968)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.9651, 
        farPlane=10.0233, width=0.816629, height=0.804265, cameraPosition=(
        2.99167, 0.397342, -6.49259), cameraUpVector=(0.531276, 0.787637, 
        0.31205), cameraTarget=(-0.424109, 0.00769516, 0.306389), 
        viewOffsetX=-0.209887, viewOffsetY=0.302186)
    session.viewports['Viewport: 1'].view.setValues(width=0.732464, 
        height=0.721375, cameraPosition=(8.05739, 0.0960217, 1.28606), 
        cameraUpVector=(0, 1, 0), cameraTarget=(-0.436814, 0.0960217, 1.28606), 
        viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.4758, 
        farPlane=8.63898, width=3.11738, height=3.07019, viewOffsetX=-0.689027, 
        viewOffsetY=-0.743407)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.44512, 
        farPlane=8.66966, width=3.10459, height=3.05759, cameraPosition=(
        8.05739, 0.0960217, -0.239053), cameraTarget=(-0.436814, 0.0960217, 
        -0.239053), viewOffsetX=-0.6862, viewOffsetY=-0.740356)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.11495, 
        farPlane=8.99983, width=4.5752, height=4.50593, viewOffsetX=-1.48129, 
        viewOffsetY=-0.889803)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=7.20143, 
        farPlane=8.91335, width=4.63081, height=4.5607, viewOffsetX=-1.45504, 
        viewOffsetY=-0.872252)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.66169, 
        farPlane=10.428, width=3.6407, height=3.58558, cameraPosition=(
        0.560853, 1.23978, -6.59334), cameraUpVector=(0.00434677, 0.990009, 
        0.140939), cameraTarget=(-1.68129, 0.0947095, 1.51919), 
        viewOffsetX=-1.14394, viewOffsetY=-0.685756)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.31431, 
        farPlane=9.7754, width=1.25312, height=1.23415, viewOffsetX=-1.08434, 
        viewOffsetY=-0.350866)
    session.viewports['Viewport: 1'].view.setValues(width=1.32312, height=1.30309, 
        cameraPosition=(-0.232105, 7.70044, 1.38724), cameraUpVector=(0, 0, 1), 
        cameraTarget=(-0.232105, -0.344407, 1.38724), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.81274, 
        -0.344407, 1.38724), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.232105, 
        -0.344407, 9.43209))
    session.viewports['Viewport: 1'].view.setValues(width=1.27465, height=1.25536, 
        viewOffsetX=0.00294265, viewOffsetY=0.00186595)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.08885, 
        farPlane=9.3191, width=1.2659, height=1.24674, cameraPosition=(3.79114, 
        2.26228, 7.82297), cameraUpVector=(0.0825243, 0.901772, -0.42426), 
        cameraTarget=(-0.288951, -0.380138, 1.41281), viewOffsetX=0.00292245, 
        viewOffsetY=0.00185314)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.82027, 
        farPlane=8.09641, width=1.41797, height=1.3965, cameraPosition=(
        6.54576, 3.54953, 1.01144), cameraUpVector=(-0.438864, 0.65743, 
        -0.612523), cameraTarget=(-0.407196, -0.435389, 1.71603), 
        viewOffsetX=0.00327351, viewOffsetY=0.00207575)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.56454, 
        farPlane=9.06532, width=1.1569, height=1.13938, cameraPosition=(
        2.75623, 1.57396, -5.09327), cameraUpVector=(-0.781093, 0.605435, 
        -0.152779), cameraTarget=(-0.105423, -0.279156, 2.19346), 
        viewOffsetX=0.0026708, viewOffsetY=0.00169357)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.53869, 
        farPlane=9.02468, width=1.15152, height=1.13409, cameraPosition=(
        0.259768, 0.203682, -5.77669), cameraUpVector=(-0.694382, 0.719299, 
        0.0210489), cameraTarget=(0.144269, -0.142967, 2.25986), 
        viewOffsetX=0.00265839, viewOffsetY=0.0016857)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.52475, 
        farPlane=9.03862, width=1.31596, height=1.29603, viewOffsetX=-0.12694, 
        viewOffsetY=0.025723)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.9849, 
        farPlane=9.05156, width=3.31244, height=3.26229, viewOffsetX=-0.415597, 
        viewOffsetY=-0.0839752)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.44139, 
        farPlane=8.18041, width=2.95128, height=2.9066, cameraPosition=(
        3.14922, 3.18457, -3.00158), cameraUpVector=(-0.486406, 0.675714, 
        0.553914), cameraTarget=(-0.911133, -0.0530023, 1.53006), 
        viewOffsetX=-0.370284, viewOffsetY=-0.0748194)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.82171, 
        farPlane=7.80009, width=1.26652, height=1.24734, viewOffsetX=0.0680722, 
        viewOffsetY=-0.595151)
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.62247, 
        farPlane=7.99933, width=6.31622, height=2.52288, 
        viewOffsetX=-0.0196749, viewOffsetY=-0.676649)
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.36528, 
        farPlane=9.19809, width=5.49928, height=2.19657, viewOffsetX=-0.192388, 
        viewOffsetY=-0.160922)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.94571, 
        farPlane=7.67609, width=1.62837, height=0.652045, viewOffsetX=0.263031, 
        viewOffsetY=-0.731917)
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.67908, 
        farPlane=8.16204, width=3.07519, height=1.22832, 
        viewOffsetX=-0.0360394, viewOffsetY=-0.0176946)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.6319, 
        farPlane=8.19632, width=3.04418, height=1.21593, cameraPosition=(
        -0.492743, 0.743749, -4.85208), cameraUpVector=(-0.668168, 0.730331, 
        0.142014), cameraTarget=(-0.0217819, -0.0606228, 1.50046), 
        viewOffsetX=-0.035676, viewOffsetY=-0.0175161)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.72181, 
        farPlane=8.10641, width=1.77816, height=0.710248, 
        viewOffsetX=-0.0489392, viewOffsetY=-0.0618817)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    del mdb.models['Model-1'].loads['Load-1']
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface_upper')
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='loading', 
        region=region, distributionType=FIELD, field='AnalyticalField-2', 
        magnitude=1.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.82594, 
        farPlane=8.11243, width=1.81737, height=0.725911, cameraPosition=(
        1.88431, -1.4007, -4.52873), cameraUpVector=(-0.798661, 0.4826, 
        -0.359496), cameraTarget=(-0.020724, -0.0913064, 1.46125), 
        viewOffsetX=-0.0500184, viewOffsetY=-0.0632463)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.75576, 
        farPlane=8.12801, width=1.79094, height=0.715355, cameraPosition=(
        0.0341171, -0.800994, -4.89225), cameraUpVector=(-0.753754, 0.651785, 
        -0.0838611), cameraTarget=(-0.0397358, -0.0657715, 1.48565), 
        viewOffsetX=-0.049291, viewOffsetY=-0.0623266)
    mdb.models['Model-1'].ExpressionField(name='AnalyticalField-3', localCsys=None, 
        description='', expression='4*Y+1')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='loading_surface_lower')
    mdb.models['Model-1'].Pressure(name='Load-2', createStepName='loading', 
        region=region, distributionType=FIELD, field='AnalyticalField-3', 
        magnitude=1.0, amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.88093, 
        farPlane=7.96185, width=1.83808, height=0.734182, cameraPosition=(
        -3.06206, -1.78283, -3.85564), cameraUpVector=(-0.542439, 0.839469, 
        0.0324179), cameraTarget=(-0.0347515, -0.0346343, 1.52979), 
        viewOffsetX=-0.0505883, viewOffsetY=-0.063967)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.71257, 
        farPlane=8.13021, width=4.23744, height=1.69256, viewOffsetX=0.410347, 
        viewOffsetY=-0.0772097)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.69554, 
        farPlane=8.14724, width=4.22212, height=1.68644, cameraPosition=(
        -3.18462, -1.67672, -3.82119), cameraUpVector=(-0.719798, 0.668335, 
        0.18767), cameraTarget=(-0.157308, 0.0714717, 1.56424), 
        viewOffsetX=0.408864, viewOffsetY=-0.0769306)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.66838, 
        farPlane=7.1045, width=4.1977, height=1.67669, cameraPosition=(5.25083, 
        0.611472, -1.17139), cameraUpVector=(-0.139852, 0.989655, 0.0320079), 
        cameraTarget=(-0.078176, -0.253976, 2.30371), viewOffsetX=0.406499, 
        viewOffsetY=-0.0764856)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.67011, 
        farPlane=7.10277, width=4.19927, height=1.67731, cameraPosition=(
        5.24911, 0.618331, -1.17231), cameraUpVector=(-0.147221, 0.988891, 
        0.0205173), cameraTarget=(-0.0798925, -0.247117, 2.30279), 
        viewOffsetX=0.40665, viewOffsetY=-0.076514)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.67011, 
        width=4.19927, height=1.67731, cameraPosition=(5.25393, 0.598472, 
        -1.16986), cameraUpVector=(-0.12588, 0.990593, 0.053667), 
        cameraTarget=(-0.0750719, -0.266976, 2.30524), viewOffsetX=0.40665, 
        viewOffsetY=-0.0765141)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.91412, 
        farPlane=6.85874, width=1.06471, height=0.425278, viewOffsetX=1.58176, 
        viewOffsetY=0.108758)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(
        name='C:/Users/touze/project/Shear_centre/strip/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.13737, 
        farPlane=8.57209, width=6.27279, height=2.50554, viewOffsetX=-0.197298, 
        viewOffsetY=-0.111199)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.21362, 
        farPlane=8.05532, width=6.3659, height=2.54273, cameraPosition=(
        5.43655, 1.45622, -1.72096), cameraUpVector=(-0.704609, 0.683, 
        -0.192451), cameraTarget=(-0.344341, -0.194029, 1.64981), 
        viewOffsetX=-0.200227, viewOffsetY=-0.112849)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.63699, 
        farPlane=7.63849, width=6.88284, height=2.74921, cameraPosition=(
        -6.4109, 0.402327, 0.180804), cameraUpVector=(0.383817, 0.921917, 
        0.0524831), cameraTarget=(0.201926, 0.0326847, 2.08816), 
        viewOffsetX=-0.216486, viewOffsetY=-0.122013)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.56211, 
        farPlane=7.51166, width=6.79141, height=2.71269, cameraPosition=(
        -6.39661, 0.86603, 0.349997), cameraUpVector=(0.452551, 0.890988, 
        0.0365661), cameraTarget=(0.220369, 0.0126752, 2.07959), 
        viewOffsetX=-0.21361, viewOffsetY=-0.120392)
    session.viewports['Viewport: 1'].view.setValues(width=7.16069, height=2.86019, 
        cameraPosition=(-0.0800172, 6.43277, 1.75477), cameraUpVector=(0, 0, 
        1), cameraTarget=(-0.0800172, -0.104117, 1.75477), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.0800172, 
        -0.104117, 8.29166), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6.45687, 
        -0.104117, 1.75477))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.79244, 
        farPlane=7.07732, width=7.45858, height=2.97918, cameraUpVector=(0, 
        -0.992885, 0.119074))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.32644, 
        farPlane=6.54332, width=0.569446, height=0.227454, 
        viewOffsetX=-1.38933, viewOffsetY=0.0160512)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.16962, 
        farPlane=9.36896, width=0.555331, height=0.221815, cameraPosition=(
        3.16747, -1.35287, -5.33656), cameraUpVector=(-0.163663, -0.981831, 
        0.0960371), cameraTarget=(1.33249, -0.439838, 0.870704), 
        viewOffsetX=-1.35489, viewOffsetY=0.0156533)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.44775, 
        farPlane=8.08335, width=0.580366, height=0.231815, cameraPosition=(
        7.08727, -0.548493, -0.332318), cameraUpVector=(-0.0314952, -0.990295, 
        0.135366), cameraTarget=(1.23034, 0.0267248, 2.5131), 
        viewOffsetX=-1.41597, viewOffsetY=0.016359)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.17984, 
        farPlane=8.35126, width=3.83378, height=1.53133, viewOffsetX=-1.64801, 
        viewOffsetY=-0.118254)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.19601, 
        farPlane=8.3351, width=4.08916, height=1.63333, viewOffsetX=-1.54775, 
        viewOffsetY=-0.129567)
    session.animationController.setValues(animationType=SCALE_FACTOR, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.animationController.setValues(animationType=NONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.02051, 
        farPlane=8.51059, width=6.51829, height=2.6036, viewOffsetX=-1.7072, 
        viewOffsetY=-0.0883547)
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.animationController.setValues(animationType=NONE)


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
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'SEQUT', 'PE', 'PEEQ', 'PEMAG', 'LE', 'TE', 'TEEQ', 'TEVOL', 
        'EEQUT', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'COORD', 'MVF'))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(
        name='C:/Users/touze/project/Shear_centre/strip/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    odb = session.odbs['C:/Users/touze/project/Shear_centre/strip/Job-1.odb']
    session.fieldReportOptions.setValues(reportFormat=COMMA_SEPARATED_VALUES)
    session.writeFieldReport(fileName='abaqus.csv', append=OFF, 
        sortItem='COORD.COOR3', odb=odb, step=0, frame=1, outputPosition=NODAL, 
        variable=(('COORD', NODAL, ((COMPONENT, 'COOR1'), (COMPONENT, 'COOR2'), 
        (COMPONENT, 'COOR3'), )), ('S', INTEGRATION_POINT, ((INVARIANT, 
        'Mises'), )), ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
