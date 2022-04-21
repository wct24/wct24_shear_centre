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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.688782, 
        farPlane=1.19684, width=1.25124, height=1.08801, cameraPosition=(
        -0.669278, 0.228933, 0.942809), cameraTarget=(-0.669278, 0.228933, 0))
    s.rectangle(point1=(-0.5, 0.5), point2=(0.5, 0.44))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.59938, 
        farPlane=1.28624, width=4.23033, height=1.49465, cameraPosition=(
        -1.14886, 0.897027, 0.942809), cameraTarget=(-1.14886, 0.897027, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1.14886, 
        0.288096, 0.942809), cameraTarget=(-1.14886, 0.288096, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-1.14886, 
        0.0561222, 0.942809), cameraTarget=(-1.14886, 0.0561222, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.798389, 
        farPlane=1.08723, width=1.77895, height=0.628535, cameraPosition=(
        -0.456977, -0.228694, 0.942809), cameraTarget=(-0.456977, -0.228694, 
        0))
    s.rectangle(point1=(-0.04, 0.44), point2=(0.04, -0.44))
    s.CoincidentConstraint(entity1=v[4], entity2=g[3], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(width=1.8925, height=0.668654, 
        cameraPosition=(-0.513539, -0.212738, 0.942809), cameraTarget=(
        -0.513539, -0.212738, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-0.203042, 
        -0.212738, 0.942809), cameraTarget=(-0.203042, -0.212738, 0))
    s.rectangle(point1=(-0.5, -0.44), point2=(0.5, -0.5))
    s.autoTrimCurve(curve1=g[7], point1=(0.00415322184562683, -0.440929412841797))
    s.autoTrimCurve(curve1=g[13], point1=(0.00415322184562683, -0.440929412841797))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.822365, 
        farPlane=1.06325, width=1.48361, height=0.524187, cameraPosition=(
        -0.152194, 0.312376, 0.942809), cameraTarget=(-0.152194, 0.312376, 0))
    s.autoTrimCurve(curve1=g[3], point1=(0.00190511345863342, 0.443191975355148))
    s.autoTrimCurve(curve1=g[9], point1=(0.00190511345863342, 0.443191975355148))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.671372, 
        farPlane=1.21425, width=3.78398, height=1.33695, cameraPosition=(
        -0.40716, -0.0375899, 0.942809), cameraTarget=(-0.40716, -0.0375899, 
        0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=5.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((210000000000.0, 
        0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='I-section', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='I-section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.82046, 
        farPlane=14.0125, width=7.97028, height=2.82308, viewOffsetX=0.153975, 
        viewOffsetY=-0.100677)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    mdb.models['Model-1'].StaticStep(name='loading', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.75829, 
        farPlane=14.0746, width=8.44032, height=2.98211, viewOffsetX=0.144947, 
        viewOffsetY=0.117236)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(width=8.97225, height=3.17005, 
        viewOffsetX=0.282023, viewOffsetY=0.188096)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.30079, 
        farPlane=14.8463, width=8.51002, height=3.00674, cameraPosition=(
        1.91099, 2.23664, -8.70532), cameraUpVector=(-0.57656, 0.706826, 
        0.409848), cameraTarget=(0.530975, 0.0474368, 2.41397), 
        viewOffsetX=0.267494, viewOffsetY=0.178406)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.39938, 
        farPlane=14.7477, width=8.09443, height=2.85991, viewOffsetX=0.122902, 
        viewOffsetY=0.611274)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['Part-1-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#ffffffff:4 #7f ]', ), )
    a.Set(nodes=nodes1, name='wall_nodes_all')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=9.65593, 
        farPlane=13.7906, width=9.30537, height=3.28775, cameraPosition=(
        9.93747, 4.09266, 7.2699), cameraUpVector=(-0.228253, 0.466733, 
        -0.854436), cameraTarget=(-0.104442, 0.270977, 3.41108), 
        viewOffsetX=0.141288, viewOffsetY=0.702721)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.33039, 
        farPlane=14.8591, width=8.02796, height=2.83642, cameraPosition=(
        3.22466, -1.80597, 13.5286), cameraUpVector=(0.497804, 0.757652, 
        -0.422083), cameraTarget=(-0.798504, -0.00690728, 2.99709), 
        viewOffsetX=0.121892, viewOffsetY=0.606254)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['wall_nodes_all']
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='loading', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=8.74632, 
        farPlane=14.4431, width=3.5445, height=1.25234, viewOffsetX=-0.169746, 
        viewOffsetY=0.38298)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['Part-1-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#0:425 #800000 ]', ), )
    a.Set(nodes=nodes1, name='loading_note=')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['loading_note=']
    mdb.models['Model-1'].ConcentratedForce(name='Load-1', 
        createStepName='loading', region=region, cf2=-1000.0, 
        distributionType=UNIFORM, field='', localCsys=None)
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)


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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=171.216, 
        farPlane=205.908, width=85.4413, height=79.2214, cameraPosition=(
        -2.57834, 1.39093, 188.562), cameraTarget=(-2.57834, 1.39093, 0))
    s.rectangle(point1=(-0.018, -0.464), point2=(0.018, 0.464))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.231, 
        farPlane=188.892, width=1.62874, height=1.51017, cameraPosition=(
        0.0464866, -0.063119, 188.562), cameraTarget=(0.0464866, -0.063119, 0))
    s.rectangle(point1=(-0.157, 0.464), point2=(0.157, 0.528))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.25, 
        farPlane=188.874, width=1.53728, height=1.42537, cameraPosition=(
        0.0682471, 0.23413, 188.562), cameraTarget=(0.0682471, 0.23413, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0682471, 
        -0.0509433, 188.562), cameraTarget=(0.0682471, -0.0509433, 0))
    s.rectangle(point1=(-0.157, -0.464), point2=(0.157, -0.528))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.471, 
        farPlane=188.653, width=0.504724, height=0.467981, cameraPosition=(
        0.00252485, -0.324949, 188.562), cameraTarget=(0.00252485, -0.324949, 
        0))
    s.autoTrimCurve(curve1=g[5], point1=(-0.0002310611307621, -0.46319916844368))
    s.autoTrimCurve(curve1=g[13], point1=(0.003705944865942, -0.46319916844368))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.516, 
        farPlane=188.608, width=0.227647, height=0.211075, cameraPosition=(
        0.00778074, 0.457679, 188.562), cameraTarget=(0.00778074, 0.457679, 0))
    s.autoTrimCurve(curve1=g[3], point1=(0.000855433754622936, 0.464962810277939))
    s.autoTrimCurve(curve1=g[9], point1=(0.00263115298002958, 0.464962810277939))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.365, 
        farPlane=188.759, width=0.968189, height=0.897707, cameraPosition=(
        0.0173353, -0.223762, 188.562), cameraTarget=(0.0173353, -0.223762, 0))
    s.FilletByRadius(radius=0.03, curve1=g[15], nearPoint1=(-0.0347746983170509, 
        -0.461762189865112), curve2=g[2], nearPoint2=(-0.0211807861924171, 
        -0.440606653690338))
    s.FilletByRadius(radius=0.03, curve1=g[14], nearPoint1=(0.0482992753386497, 
        -0.460251092910767), curve2=g[4], nearPoint2=(0.0165801271796227, 
        -0.416428923606873))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.398, 
        farPlane=188.726, width=0.807452, height=0.748672, cameraPosition=(
        -0.0328712, 0.291506, 188.562), cameraTarget=(-0.0328712, 0.291506, 0))
    s.FilletByRadius(radius=0.03, curve1=g[4], nearPoint1=(0.0131070464849472, 
        0.439583510160446), curve2=g[16], nearPoint2=(0.0634941309690475, 
        0.467308789491653))
    s.FilletByRadius(radius=0.03, curve1=g[2], nearPoint1=(-0.0209042280912399, 
        0.409337788820267), curve2=g[17], nearPoint2=(-0.0448380559682846, 
        0.462267845869064))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=188.307, 
        farPlane=188.817, width=1.25536, height=1.16397, cameraPosition=(
        -0.0754928, 0.000270486, 188.562), cameraTarget=(-0.0754928, 
        0.000270486, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=1.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11097, 
        farPlane=4.07296, width=1.47362, height=1.36634, viewOffsetX=0.113865, 
        viewOffsetY=0.0740027)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02993, 
        farPlane=3.93989, width=1.41705, height=1.31389, cameraPosition=(
        -0.612131, 1.09993, 3.21129), cameraUpVector=(0.309758, 0.743914, 
        -0.592151), cameraTarget=(-0.129762, 0.0127256, 0.357244), 
        viewOffsetX=0.109494, viewOffsetY=0.0711619)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21145, 
        farPlane=3.90037, width=1.54377, height=1.43139, cameraPosition=(
        2.35117, 1.5305, 1.71676), cameraUpVector=(-0.705385, 0.643652, 
        -0.296892), cameraTarget=(-0.0650401, -0.0357837, 0.590294), 
        viewOffsetX=0.119285, viewOffsetY=0.0775255)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05998, 
        farPlane=3.98599, width=1.43804, height=1.33335, cameraPosition=(
        1.32884, 1.10942, 2.98183), cameraUpVector=(-0.467024, 0.736251, 
        -0.489718), cameraTarget=(-0.136813, -0.0567517, 0.521718), 
        viewOffsetX=0.111115, viewOffsetY=0.0722156)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.12148, 
        farPlane=3.91372, width=1.48097, height=1.37316, cameraPosition=(
        1.76474, 0.864772, 2.79342), cameraUpVector=(-0.507279, 0.787018, 
        -0.3511), cameraTarget=(-0.131517, -0.0568547, 0.531775), 
        viewOffsetX=0.114432, viewOffsetY=0.0743716)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16448, 
        farPlane=3.87452, width=1.51099, height=1.40099, cameraPosition=(
        2.12722, 0.828489, 2.48093), cameraUpVector=(-0.465333, 0.81152, 
        -0.353413), cameraTarget=(-0.136141, -0.0358981, 0.559931), 
        viewOffsetX=0.116752, viewOffsetY=0.0758792)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.07706, 
        farPlane=3.94574, width=1.44996, height=1.35285, cameraPosition=(
        1.10876, 0.807461, 3.18451), cameraUpVector=(-0.351486, 0.806631, 
        -0.475188), cameraTarget=(-0.153122, -0.0491369, 0.494884), 
        viewOffsetX=0.112037, viewOffsetY=0.0728146)


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.688, 
        farPlane=2.77166, width=0.470336, height=0.177465, 
        viewOffsetX=0.00409226, viewOffsetY=0.0418611)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.PartitionFaceByAuto(face=f[16])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70118, 
        farPlane=2.75847, width=0.347878, height=0.13126, 
        viewOffsetX=0.0128589, viewOffsetY=0.0786118)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71245, 
        farPlane=2.75232, width=0.350184, height=0.132129, cameraPosition=(
        0.671479, 0.355208, 2.59998), cameraUpVector=(-0.292555, 0.858483, 
        -0.421211), cameraTarget=(-0.0360287, -0.0390791, 0.525143), 
        viewOffsetX=0.0129441, viewOffsetY=0.0791327)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71225, 
        farPlane=2.75252, width=0.350144, height=0.132114, cameraPosition=(
        0.695734, 0.358076, 2.59116), cameraUpVector=(-0.502292, 0.79598, 
        -0.337814), cameraTarget=(-0.0117736, -0.0362112, 0.516327), 
        viewOffsetX=0.0129426, viewOffsetY=0.0791236)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71225, 
        farPlane=2.75251, width=0.350144, height=0.132114, cameraPosition=(
        0.700576, 0.359452, 2.58925), cameraUpVector=(-0.543029, 0.776276, 
        -0.320179), cameraTarget=(-0.0069319, -0.0348347, 0.514414), 
        viewOffsetX=0.0129426, viewOffsetY=0.0791235)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70678, 
        farPlane=2.775, width=0.349025, height=0.131692, cameraPosition=(
        0.0999302, 0.255381, 2.72448), cameraUpVector=(-0.377613, 0.822301, 
        -0.42571), cameraTarget=(-0.0183343, -0.0374925, 0.519664), 
        viewOffsetX=0.0129012, viewOffsetY=0.0788706)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71507, 
        farPlane=2.76671, width=0.227434, height=0.0858142, 
        viewOffsetX=-0.000880936, viewOffsetY=0.0651551)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71615, 
        farPlane=2.76562, width=0.227578, height=0.0858686, cameraPosition=(
        0.108957, 0.259816, 2.72341), cameraUpVector=(-0.478245, 0.77454, 
        -0.413968), cameraTarget=(-0.00930739, -0.0330576, 0.518591), 
        viewOffsetX=-0.000881494, viewOffsetY=0.0651964)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.72091, 
        farPlane=2.76646, width=0.228209, height=0.0861067, cameraPosition=(
        0.179595, 0.51506, 2.67665), cameraUpVector=(-0.513873, 0.710782, 
        -0.480336), cameraTarget=(-0.00661567, -0.0291607, 0.524879), 
        viewOffsetX=-0.000883938, viewOffsetY=0.0653772)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69967, 
        farPlane=2.78769, width=0.47553, height=0.179425, viewOffsetX=0.100292, 
        viewOffsetY=0.0325223)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70189, 
        farPlane=2.78547, width=0.476151, height=0.179659, cameraPosition=(
        0.188192, 0.508204, 2.67764), cameraUpVector=(-0.576075, 0.672123, 
        -0.465176), cameraTarget=(0.00198145, -0.0360166, 0.525869), 
        viewOffsetX=0.100423, viewOffsetY=0.0325648)


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
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#10000 ]', ), )
    p.Set(faces=faces, name='end_surface')
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteSeeds()
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#92492491 #4924 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55924, 
        farPlane=2.61368, width=0.241117, height=0.224968, 
        viewOffsetX=-0.108616, viewOffsetY=-0.0990369)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEndEdges = e.getSequenceFromMask(mask=('[#92492491 #4924 ]', ), )
    p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEndEdges, minSize=0.002, 
        maxSize=0.01, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57062, 
        farPlane=2.6023, width=0.178249, height=0.16631, viewOffsetX=-0.177253, 
        viewOffsetY=-0.154932)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#92492491 #4924 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=('[#12490080 #24 ]', ), )
    pickedEdges2 = e.getSequenceFromMask(mask=('[#80002411 #4900 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, 
        end2Edges=pickedEdges2, minSize=0.002, maxSize=0.01, constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57044, 
        farPlane=2.60248, width=0.158774, height=0.14814, 
        viewOffsetX=-0.169009, viewOffsetY=-0.138076)
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['Part-1']
    p.deleteSeeds()
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#92492491 #4924 ]', ), )
    p.deleteSeeds(regions=pickedEdges)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#92492491 #4924 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.05, 
        constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57407, 
        farPlane=2.59884, width=0.159141, height=0.148483, 
        viewOffsetX=-0.169203, viewOffsetY=-0.138306)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
def Macro5():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81947, 
        farPlane=2.96609, width=0.484752, height=0.452286, 
        viewOffsetX=-0.0102081, viewOffsetY=-0.12461)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.8183, 
        farPlane=3.00269, width=0.484442, height=0.451996, cameraPosition=(
        -0.309831, -0.631359, 2.81033), cameraUpVector=(0.645133, 0.764033, 
        0.0075025), cameraTarget=(0.0537107, 0.0539171, 0.722446), 
        viewOffsetX=-0.0102016, viewOffsetY=-0.12453)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86557, 
        farPlane=2.97678, width=0.497036, height=0.463746, cameraPosition=(
        -1.0946, 0.00368242, 2.66485), cameraUpVector=(0.660179, 0.750688, 
        0.025116), cameraTarget=(-0.0214702, 0.114146, 0.716208), 
        viewOffsetX=-0.0104668, viewOffsetY=-0.127767)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85465, 
        farPlane=2.98479, width=0.494127, height=0.461032, cameraPosition=(
        -0.761714, 1.06393, 2.54101), cameraUpVector=(0.780887, 0.539279, 
        -0.315267), cameraTarget=(0.0304944, 0.189203, 0.652024), 
        viewOffsetX=-0.0104055, viewOffsetY=-0.127019)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9176, 
        farPlane=2.92184, width=0.179177, height=0.167176, 
        viewOffsetX=0.117381, viewOffsetY=-0.164155)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.94947, 
        farPlane=3.02512, width=0.182154, height=0.169954, cameraPosition=(
        0.434523, 0.385879, 2.9221), cameraUpVector=(0.0273646, 0.889286, 
        -0.456533), cameraTarget=(-0.036988, 0.125735, 0.760843), 
        viewOffsetX=0.119332, viewOffsetY=-0.166882)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.97256, 
        farPlane=2.96398, width=0.184312, height=0.171967, cameraPosition=(
        1.03117, 0.862801, 2.57433), cameraUpVector=(-0.162053, 0.781131, 
        -0.60297), cameraTarget=(0.0147442, 0.169266, 0.717744), 
        viewOffsetX=0.120746, viewOffsetY=-0.168859)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.89292, 
        farPlane=3.04362, width=0.632858, height=0.590472, 
        viewOffsetX=0.186987, viewOffsetY=-0.120213)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.77679, 
        farPlane=3.02324, width=0.594034, height=0.554249, cameraPosition=(
        -0.296371, 0.797229, 2.74928), cameraUpVector=(0.0880815, 0.802069, 
        -0.590701), cameraTarget=(-0.127068, 0.14157, 0.627378), 
        viewOffsetX=0.175516, viewOffsetY=-0.112839)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80425, 
        farPlane=2.99578, width=0.515546, height=0.481017, 
        viewOffsetX=0.197977, viewOffsetY=-0.169578)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86655, 
        farPlane=2.69334, width=0.533347, height=0.497626, cameraPosition=(
        -1.89009, 0.781079, 1.52567), cameraUpVector=(0.498739, 0.803952, 
        -0.323915), cameraTarget=(-0.0930211, 0.129191, 0.38259), 
        viewOffsetX=0.204813, viewOffsetY=-0.175433)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75998, 
        farPlane=2.58322, width=0.502895, height=0.469213, cameraPosition=(
        -1.59156, 0.746653, -0.803038), cameraUpVector=(0.82361, 0.507951, 
        -0.252294), cameraTarget=(0.159398, -0.0863843, 0.29298), 
        viewOffsetX=0.193119, viewOffsetY=-0.165416)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52867, 
        farPlane=2.73634, width=0.436799, height=0.407545, cameraPosition=(
        0.186048, 0.188595, -1.63439), cameraUpVector=(0.732018, 0.562111, 
        0.384942), cameraTarget=(0.26615, -0.10584, 0.571956), 
        viewOffsetX=0.167737, viewOffsetY=-0.143675)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58134, 
        farPlane=2.68368, width=0.216807, height=0.202286, 
        viewOffsetX=0.197932, viewOffsetY=-0.159628)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69063, 
        farPlane=2.61516, width=0.231792, height=0.216267, cameraPosition=(
        -0.923519, 0.855978, -1.27829), cameraUpVector=(0.98071, -0.022079, 
        -0.194218), cameraTarget=(0.126702, -0.271297, 0.330237), 
        viewOffsetX=0.211612, viewOffsetY=-0.170661)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.98672, 
        farPlane=2.43184, width=0.272387, height=0.254144, cameraPosition=(
        -2.20686, 0.306658, 0.740129), cameraUpVector=(0.184321, 0.272063, 
        -0.944462), cameraTarget=(-0.107284, -0.217525, 0.21278), 
        viewOffsetX=0.248673, viewOffsetY=-0.20055)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9458, 
        farPlane=2.42362, width=0.266778, height=0.24891, cameraPosition=(
        -1.75667, 1.33242, 0.731935), cameraUpVector=(0.134415, -0.0517556, 
        -0.989573), cameraTarget=(-0.217615, -0.210403, 0.271409), 
        viewOffsetX=0.243552, viewOffsetY=-0.19642)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.07028, 
        farPlane=2.37689, width=0.283845, height=0.264834, cameraPosition=(
        -1.9564, -1.0138, 0.0449783), cameraUpVector=(0.136647, 0.626998, 
        -0.766943), cameraTarget=(0.0726875, -0.105326, 0.181147), 
        viewOffsetX=0.259133, viewOffsetY=-0.208986)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00526, 
        farPlane=2.48131, width=0.274931, height=0.256517, cameraPosition=(
        0.526885, -2.20377, 0.618901), cameraUpVector=(-0.812133, 0.0222329, 
        -0.583049), cameraTarget=(-0.0077063, -0.088467, 0.170812), 
        viewOffsetX=0.250995, viewOffsetY=-0.202423)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.94411, 
        farPlane=2.55291, width=0.266547, height=0.248695, cameraPosition=(
        1.66223, -1.44382, 1.07166), cameraUpVector=(-0.814213, -0.579378, 
        -0.0371197), cameraTarget=(-0.0539143, -0.263024, 0.28322), 
        viewOffsetX=0.243341, viewOffsetY=-0.19625)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08236, 
        farPlane=2.43143, width=0.285502, height=0.266381, cameraPosition=(
        0.797681, 2.13003, 0.720882), cameraUpVector=(0.455457, -0.494798, 
        0.74009), cameraTarget=(0.354321, -0.0454385, 0.542471), 
        viewOffsetX=0.260646, viewOffsetY=-0.210206)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.09991, 
        farPlane=2.4222, width=0.287909, height=0.268626, cameraPosition=(
        -2.18376, 0.673362, 0.345928), cameraUpVector=(0.307789, 0.415288, 
        0.856039), cameraTarget=(0.00904753, 0.358639, 0.577491), 
        viewOffsetX=0.262843, viewOffsetY=-0.211978)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.92146, 
        farPlane=2.60066, width=1.28439, height=1.19837, viewOffsetX=0.356433, 
        viewOffsetY=-0.19112)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43686, 
        farPlane=2.91704, width=0.960461, height=0.896134, cameraPosition=(
        -0.4701, 0.487308, -1.59917), cameraUpVector=(-0.377274, 0.756774, 
        0.533814), cameraTarget=(0.190476, 0.302901, 0.519956), 
        viewOffsetX=0.266539, viewOffsetY=-0.142919)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.45756, 
        farPlane=2.828, width=0.974299, height=0.909045, cameraPosition=(
        0.85297, 0.661117, -1.38607), cameraUpVector=(-0.619248, 0.734982, 
        0.276284), cameraTarget=(0.136974, 0.287713, 0.689736), 
        viewOffsetX=0.270379, viewOffsetY=-0.144978)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.61927, 
        farPlane=2.66629, width=0.149443, height=0.139434, 
        viewOffsetX=0.355953, viewOffsetY=-0.13773)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62324, 
        farPlane=2.39175, width=0.149809, height=0.139776, cameraPosition=(
        1.15496, 0.705624, 2.06791), cameraUpVector=(-0.464569, 0.803843, 
        -0.371501), cameraTarget=(-0.502475, 0.0533028, 0.730588), 
        viewOffsetX=0.356825, viewOffsetY=-0.138067)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.51636, 
        farPlane=2.57412, width=0.139945, height=0.130572, cameraPosition=(
        0.0301947, 0.240259, 2.59204), cameraUpVector=(-0.291335, 0.884424, 
        -0.364578), cameraTarget=(-0.531685, 0.01121, 0.448938), 
        viewOffsetX=0.333329, viewOffsetY=-0.128976)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.49235, 
        farPlane=2.59813, width=0.291768, height=0.272227, 
        viewOffsetX=0.338529, viewOffsetY=-0.087629)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56891, 
        farPlane=2.50439, width=0.306735, height=0.286192, cameraPosition=(
        0.990333, 0.35432, 2.31241), cameraUpVector=(-0.824515, 0.564535, 
        0.0384095), cameraTarget=(-0.411251, -0.26766, 0.696929), 
        viewOffsetX=0.355895, viewOffsetY=-0.0921243)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83643, 
        farPlane=2.21249, width=0.359037, height=0.334991, cameraPosition=(
        1.79161, 1.02793, 0.756194), cameraUpVector=(-0.668489, 0.498823, 
        0.551632), cameraTarget=(-0.0515338, -0.202269, 0.980944), 
        viewOffsetX=0.416579, viewOffsetY=-0.107832)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43853, 
        farPlane=2.58946, width=0.281244, height=0.262408, cameraPosition=(
        0.240236, 0.494501, -1.49338), cameraUpVector=(0.144795, 0.852372, 
        0.50249), cameraTarget=(0.482112, 0.0461864, 0.674933), 
        viewOffsetX=0.326318, viewOffsetY=-0.0844678)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.53515, 
        farPlane=2.49751, width=0.300135, height=0.280033, cameraPosition=(
        -0.870097, 0.252174, -1.36049), cameraUpVector=(0.454449, 0.868094, 
        0.199724), cameraTarget=(0.496314, -0.00811771, 0.379123), 
        viewOffsetX=0.348236, viewOffsetY=-0.0901413)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#3ffff ]', ), )
    p.Set(faces=faces, name='mesh_surf')
def Macro6():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83582, 
        farPlane=2.61885, width=0.16391, height=0.151978, 
        viewOffsetX=-0.201432, viewOffsetY=-0.158482)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85296, 
        farPlane=2.74042, width=0.16544, height=0.153397, cameraPosition=(
        1.39751, 0.695434, 2.2118), cameraUpVector=(0.22861, 0.399806, 
        -0.887633), cameraTarget=(0.143394, -0.244352, 0.629075), 
        viewOffsetX=-0.203313, viewOffsetY=-0.159962)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75601, 
        farPlane=2.83738, width=0.712273, height=0.660421, 
        viewOffsetX=-0.167383, viewOffsetY=-0.0202713)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74248, 
        farPlane=3.00856, width=0.706783, height=0.655331, cameraPosition=(
        -0.0466141, 0.681506, 2.78585), cameraUpVector=(0.0359448, 0.771411, 
        -0.635321), cameraTarget=(0.151748, -0.0810632, 0.702549), 
        viewOffsetX=-0.166093, viewOffsetY=-0.020115)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.91037, 
        farPlane=2.73171, width=0.774881, height=0.718471, cameraPosition=(
        -1.32848, 1.56835, 1.59802), cameraUpVector=(0.459923, 0.378687, 
        -0.803161), cameraTarget=(0.0254806, 0.030843, 0.724029), 
        viewOffsetX=-0.182096, viewOffsetY=-0.0220531)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00787, 
        farPlane=2.6342, width=0.184469, height=0.17104, viewOffsetX=0.0295822, 
        viewOffsetY=-0.173483)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00581, 
        farPlane=2.56827, width=0.184279, height=0.170864, cameraPosition=(
        -0.513304, 2.02636, 1.45151), cameraUpVector=(-0.246713, -0.065606, 
        -0.966865), cameraTarget=(-0.0639678, -0.0246114, 0.708139), 
        viewOffsetX=0.0295517, viewOffsetY=-0.173304)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10131, 
        farPlane=3.17225, width=0.193053, height=0.178999, cameraPosition=(
        -0.689064, -0.343773, 3.02275), cameraUpVector=(-0.512696, 0.779638, 
        -0.359594), cameraTarget=(-0.120224, 0.00224721, 0.897264), 
        viewOffsetX=0.0309587, viewOffsetY=-0.181555)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9793, 
        farPlane=3.29426, width=0.86815, height=0.804951, 
        viewOffsetX=0.0538091, viewOffsetY=-0.270621)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.2251, 
        farPlane=3.32483, width=0.975958, height=0.90491, cameraPosition=(
        1.88984, 1.17316, 2.17118), cameraUpVector=(-0.34229, 0.730178, 
        -0.591335), cameraTarget=(0.432344, 0.327245, 0.71477), 
        viewOffsetX=0.0604912, viewOffsetY=-0.304227)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11783, 
        farPlane=3.33496, width=0.928908, height=0.861286, cameraPosition=(
        0.780444, 1.46932, -1.6801), cameraUpVector=(-0.968964, -0.189828, 
        -0.158346), cameraTarget=(0.00806817, 0.149724, -0.0604986), 
        viewOffsetX=0.057575, viewOffsetY=-0.289561)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03277, 
        farPlane=3.38049, width=0.891598, height=0.826692, cameraPosition=(
        -0.438266, 0.648829, -2.11818), cameraUpVector=(-0.793594, -0.565248, 
        0.225176), cameraTarget=(-0.219923, -0.147065, -0.049394), 
        viewOffsetX=0.0552625, viewOffsetY=-0.277931)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15484, 
        farPlane=3.25841, width=0.275312, height=0.25527, 
        viewOffsetX=-0.0287984, viewOffsetY=-0.31072)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13957, 
        farPlane=3.20617, width=0.273362, height=0.253462, cameraPosition=(
        -1.17588, 0.276609, -1.91651), cameraUpVector=(-0.595809, -0.66204, 
        0.454659), cameraTarget=(-0.314797, -0.257623, 0.0669524), 
        viewOffsetX=-0.0285944, viewOffsetY=-0.30852)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27298, 
        farPlane=3.25693, width=0.290408, height=0.269267, cameraPosition=(
        1.41005, 0.642781, -1.84803), cameraUpVector=(-0.300799, -0.923183, 
        -0.239274), cameraTarget=(0.326363, -0.25571, -0.12196), 
        viewOffsetX=-0.0303774, viewOffsetY=-0.327758)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23978, 
        farPlane=3.12856, width=0.286167, height=0.265334, cameraPosition=(
        0.389887, 1.68225, -1.61699), cameraUpVector=(0.0114398, -0.872923, 
        -0.487724), cameraTarget=(0.193136, 0.0127476, -0.155813), 
        viewOffsetX=-0.0299337, viewOffsetY=-0.322971)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15762, 
        farPlane=3.11131, width=0.27567, height=0.255602, cameraPosition=(
        1.02636, 1.74013, 2.22297), cameraUpVector=(-0.612687, 0.566071, 
        -0.551525), cameraTarget=(0.118131, 0.498981, 0.611868), 
        viewOffsetX=-0.0288357, viewOffsetY=-0.311124)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.01486, 
        farPlane=3.12713, width=0.257431, height=0.23869, cameraPosition=(
        -0.709677, 0.471657, 2.94193), cameraUpVector=(-0.68189, 0.494189, 
        -0.539261), cameraTarget=(-0.249225, 0.24435, 0.774609), 
        viewOffsetX=-0.0269278, viewOffsetY=-0.290539)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03847, 
        farPlane=3.15161, width=0.260447, height=0.241487, cameraPosition=(
        -0.0716341, 0.585782, 3.04243), cameraUpVector=(-0.819403, 0.442706, 
        -0.36413), cameraTarget=(-0.183008, 0.248185, 0.843657), 
        viewOffsetX=-0.0272433, viewOffsetY=-0.293943)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.98326, 
        farPlane=3.20683, width=0.580458, height=0.538202, 
        viewOffsetX=0.0115076, viewOffsetY=-0.280241)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13682, 
        farPlane=3.19566, width=0.625403, height=0.579875, cameraPosition=(
        1.51522, 0.726152, 2.59204), cameraUpVector=(-0.810216, 0.578351, 
        0.095185), cameraTarget=(0.110535, 0.318496, 0.912264), 
        viewOffsetX=0.0123986, viewOffsetY=-0.30194)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.51783, 
        farPlane=2.95314, width=0.736917, height=0.683271, cameraPosition=(
        2.46376, 1.19648, 0.786069), cameraUpVector=(-0.621938, 0.67055, 
        0.404419), cameraTarget=(0.370939, 0.447219, 0.645755), 
        viewOffsetX=0.0146094, viewOffsetY=-0.355778)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.36545, 
        farPlane=3.13295, width=0.692319, height=0.641919, cameraPosition=(
        1.77795, 1.98021, -0.25699), cameraUpVector=(-0.622893, 0.480573, 
        0.617295), cameraTarget=(0.222629, 0.565301, 0.47785), 
        viewOffsetX=0.0137252, viewOffsetY=-0.334246)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['I_beam-1'].elements
    face1Elements1 = f1.getSequenceFromMask(mask=('[#ffffffff #fffff ]', ), )
    face2Elements1 = f1.getSequenceFromMask(mask=(
        '[#0:30 #f0000000 #ffffffff #ffff ]', ), )
    face3Elements1 = f1.getSequenceFromMask(mask=(
        '[#8100400 #40040007 #708100 #10040040 #4000708 #70810040 #4004000', 
        ' #70810 #81004004 #400070 #7081004 #400400 #40007081 #8100400', 
        ' #40040007 #708100 #10040040 #4000708 #70810040 #4004000 #70810', 
        ' #81004004 #400070 #7081004 #400400 #40007081 #8100400 #40040007', 
        ' #708100 #10040040 #4000708 #70810040 #4000 ]', ), )
    face4Elements1 = f1.getSequenceFromMask(mask=(
        '[#302fe970 #97000001 #1302fe #2fe97000 #130 #1302fe97 #e9700000', 
        ' #1302f #2fe9700 #70000013 #1302fe9 #fe970000 #1302 #302fe970', 
        ' #97000001 #1302fe #2fe97000 #130 #1302fe97 #e9700000 #1302f', 
        ' #2fe9700 #70000013 #1302fe9 #fe970000 #1302 #302fe970 #97000001', 
        ' #1302fe #2fe97000 #130 #1302fe97 ]', ), )
    face5Elements1 = f1.getSequenceFromMask(mask=(
        '[#c6100004 #421820 #820c6100 #10000421 #421820c6 #c610000 #42182', 
        ' #1820c610 #61000042 #421820c #20c61000 #4218 #21820c61 #c6100004', 
        ' #421820 #820c6100 #10000421 #421820c6 #c610000 #42182 #1820c610', 
        ' #61000042 #421820c #20c61000 #4218 #21820c61 #c6100004 #421820', 
        ' #820c6100 #10000421 #421820c6 #c610000 #2182 ]', ), )
    face6Elements1 = f1.getSequenceFromMask(mask=(
        '[#b04fe063 #6306000 #b04fe #4fe06306 #306000b0 #b04fe06 #e0630600', 
        ' #6000b04f #4fe0630 #6306000b #b04fe0 #fe063060 #6000b04 #b04fe063', 
        ' #6306000 #b04fe #4fe06306 #306000b0 #b04fe06 #e0630600 #6000b04f', 
        ' #4fe0630 #6306000b #b04fe0 #fe063060 #6000b04 #b04fe063 #6306000', 
        ' #b04fe #4fe06306 #306000b0 #b04fe06 #600 ]', ), )
    a.Surface(face1Elements=face1Elements1, face2Elements=face2Elements1, 
        face3Elements=face3Elements1, face4Elements=face4Elements1, 
        face5Elements=face5Elements1, face6Elements=face6Elements1, 
        name='mesh_surf')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
