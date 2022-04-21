# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def box():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.72003, 
        farPlane=1.16559, width=1.24188, height=1.42435, cameraPosition=(
        0.0825926, -0.0312209, 0.942809), cameraTarget=(0.0825926, -0.0312209, 
        0))
    s.rectangle(point1=(-0.5, 0.25), point2=(0.5, -0.25))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.757015, 
        farPlane=1.1286, width=1.03571, height=1.18788, cameraPosition=(
        -0.0628717, 0.00826199, 0.942809), cameraTarget=(-0.0628717, 
        0.00826199, 0))
    s.rectangle(point1=(-0.48, 0.23), point2=(0.48, -0.23))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.719118, 
        farPlane=1.1665, width=1.24696, height=1.43017, cameraPosition=(
        -0.0342423, 0.0340528, 0.942809), cameraTarget=(-0.0342423, 0.0340528, 
        0))
    p = mdb.models['Model-1'].Part(name='box_beam', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['box_beam']
    p.BaseSolidExtrude(sketch=s, depth=10.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['box_beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2916, 
        farPlane=26.7093, width=6.8802, height=7.89108, viewOffsetX=-0.0278935, 
        viewOffsetY=0.167941)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='box-material')
    mdb.models['Model-1'].materials['box-material'].Elastic(
        type=ENGINEERING_CONSTANTS, table=((210000000000.0, 210000000000.0, 
        210000000000.0, 0.3, 0.3, 0.3, 81000000000.0, 81000000000.0, 
        81000000000.0), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='box-section', 
        material='box-material', thickness=None)
    p = mdb.models['Model-1'].parts['box_beam']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='box_section_geometry')
    p = mdb.models['Model-1'].parts['box_beam']
    p.SectionAssignment(region=region, sectionName='box-section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['box_beam']
    region = p.sets['box_section_geometry']
    orientation=None
    mdb.models['Model-1'].parts['box_beam'].MaterialOrientation(region=region, 
        orientationType=GLOBAL, axis=AXIS_1, 
        additionalRotationType=ROTATION_NONE, localCsys=None, fieldName='', 
        stackDirection=STACK_3)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['box_beam']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['box_beam']
    p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.4243, 
        farPlane=26.5766, width=6.17622, height=7.12815, viewOffsetX=-0.385959, 
        viewOffsetY=-0.766521)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2666, 
        farPlane=26.7342, width=6.95494, height=8.02689, 
        viewOffsetX=-0.0803244, viewOffsetY=-0.604141)
    p = mdb.models['Model-1'].parts['box_beam']
    p.deleteMesh()
    p = mdb.models['Model-1'].parts['box_beam']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.0911, 
        farPlane=25.9098, width=3.25997, height=3.76242, viewOffsetX=-1.58846, 
        viewOffsetY=-1.13216)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['box_beam']
    a.Instance(name='box_beam-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.6242, 
        farPlane=27.3767, width=10.2002, height=11.6989, viewOffsetX=1.527, 
        viewOffsetY=0.864483)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=20.0266, 
        farPlane=26.4432, width=12.2879, height=14.0933, cameraPosition=(
        17.7326, 14.859, 2.51892), cameraUpVector=(-0.885172, 0.459319, 
        -0.0741338), cameraTarget=(1.5975, 0.238807, 5.66937), 
        viewOffsetX=1.83952, viewOffsetY=1.04141)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.3608, 
        farPlane=31.7783, width=10.6522, height=12.2173, cameraPosition=(
        -1.68465, 5.66235, -18.9905), cameraUpVector=(-0.315766, 0.733208, 
        0.602244), cameraTarget=(2.0297, 0.0577404, 1.95728), 
        viewOffsetX=1.59466, viewOffsetY=0.902786)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.152, 
        farPlane=29.9872, width=2.83155, height=3.24758, viewOffsetX=1.74221, 
        viewOffsetY=0.618903)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1987, 
        farPlane=29.8217, width=2.83845, height=3.2555, cameraPosition=(
        -4.79078, 6.23094, -18.3786), cameraUpVector=(-0.0854518, 0.764327, 
        0.639141), cameraTarget=(1.62905, -0.20879, 1.65465), 
        viewOffsetX=1.74646, viewOffsetY=0.620412)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1262, 
        farPlane=29.894, width=3.40452, height=3.90473, viewOffsetX=1.77365, 
        viewOffsetY=0.790604)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.1909, 
        farPlane=29.8293, width=2.69994, height=3.09663, viewOffsetX=1.75733, 
        viewOffsetY=0.32465)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['box_beam-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#ffffffff #fffffff ]', ), )
    a.Set(nodes=nodes1, name='wall_nodes')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region = a.sets['wall_nodes']
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
        region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='loading', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='loading')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'MISES', 'SEQUT', 'U', 'COORD'))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3081, 
        farPlane=29.7121, width=2.12085, height=2.43246, viewOffsetX=1.50614, 
        viewOffsetY=0.237259)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.2515, 
        farPlane=29.7687, width=2.70846, height=3.10641, viewOffsetX=1.66372, 
        viewOffsetY=0.275581)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=20.6696, 
        farPlane=26.8363, width=2.90797, height=3.33522, cameraPosition=(
        -14.8787, 13.9378, -7.53275), cameraUpVector=(0.652044, 0.526264, 
        0.545788), cameraTarget=(-0.264572, 0.274438, 1.61907), 
        viewOffsetX=1.78627, viewOffsetY=0.295881)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4475, 
        farPlane=27.221, width=2.59535, height=2.97667, cameraPosition=(
        -12.8618, 12.8284, 19.0663), cameraUpVector=(0.873549, 0.439795, 
        -0.20855), cameraTarget=(-2.17266, 1.06028, 3.85876), 
        viewOffsetX=1.59423, viewOffsetY=0.264072)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.929, 
        farPlane=27.9202, width=2.38172, height=2.73166, cameraPosition=(
        2.29765, 0.239957, 27.4417), cameraUpVector=(0.451738, 0.785446, 
        -0.423093), cameraTarget=(-2.25273, 0.600752, 5.92007), 
        viewOffsetX=1.46301, viewOffsetY=0.242336)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.0199, 
        farPlane=27.8293, width=2.26005, height=2.59212, viewOffsetX=1.40941, 
        viewOffsetY=0.68549)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.9793, 
        farPlane=27.8987, width=2.25466, height=2.58592, cameraPosition=(
        0.248038, -0.904692, 27.5564), cameraUpVector=(0.544144, 0.765563, 
        -0.343251), cameraTarget=(-2.29514, 0.710874, 5.76332), 
        viewOffsetX=1.40604, viewOffsetY=0.683853)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.0281, 
        farPlane=27.8498, width=2.12548, height=2.43777, viewOffsetX=1.45545, 
        viewOffsetY=0.765017)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1321, 
        farPlane=27.8016, width=2.13845, height=2.45264, cameraPosition=(
        4.15781, 2.3983, 27.0712), cameraUpVector=(0.0479878, 0.879262, 
        -0.473914), cameraTarget=(-2.07579, -0.206097, 6.13377), 
        viewOffsetX=1.46434, viewOffsetY=0.769685)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.4954, 
        farPlane=27.4382, width=0.513888, height=0.238565, 
        viewOffsetX=0.928417, viewOffsetY=0.056679)
    e1 = a.instances['box_beam-1'].edges
    e11 = a.instances['box_beam-1'].edges
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['box_beam-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#100 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Model-1'].SurfaceTraction(name='Load-1', createStepName='loading', 
        region=region, magnitude=100.0, directionVector=(
        a.instances['box_beam-1'].InterestingPoint(edge=e1[10], rule=MIDDLE), 
        a.instances['box_beam-1'].InterestingPoint(edge=e11[22], rule=MIDDLE)), 
        distributionType=UNIFORM, field='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1766, 
        farPlane=27.757, width=5.01992, height=2.33043, viewOffsetX=2.27322, 
        viewOffsetY=0.178331)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.1546, 
        farPlane=27.7791, width=5.01348, height=2.32744, cameraPosition=(
        4.17349, 2.55047, 27.0476), cameraUpVector=(0.0941193, 0.868689, 
        -0.486334), cameraTarget=(-2.06011, -0.0539271, 6.11017), 
        viewOffsetX=2.2703, viewOffsetY=0.178102)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.9012, 
        farPlane=27.6832, width=4.93945, height=2.29307, cameraPosition=(
        -2.57522, 1.59996, 27.2093), cameraUpVector=(0.169938, 0.896485, 
        -0.409189), cameraTarget=(-2.32973, -0.271102, 5.29), 
        viewOffsetX=2.23677, viewOffsetY=0.175472)
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
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4331, 
        farPlane=25.5678, width=3.05196, height=1.41683, viewOffsetX=-2.2469, 
        viewOffsetY=-1.38743)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6479, 
        farPlane=28.0406, width=3.08753, height=1.43334, cameraPosition=(
        8.81684, 8.87656, 24.7301), cameraUpVector=(-0.226565, 0.718666, 
        -0.65741), cameraTarget=(0.898889, -0.238889, 6.33896), 
        viewOffsetX=-2.27308, viewOffsetY=-1.4036)
    a = mdb.models['Model-1'].rootAssembly
    n1 = a.instances['box_beam-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=('[#0:187 #ffff0000 #ffffffff #fff ]', ), 
        )
    a.Set(nodes=nodes1, name='loading_nodes')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.3382, 
        farPlane=27.802, width=1.38067, height=1.24789, viewOffsetX=-1.18728, 
        viewOffsetY=0.0367008)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['box_beam-1'].elements
    face2Elements1 = f1.getSequenceFromMask(mask=('[#0:92 #fc000000 #ffffff ]', ), 
        )
    a.Surface(face2Elements=face2Elements1, name='end_surface')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3034, 
        farPlane=25.6974, width=4.65283, height=1.70771, viewOffsetX=-1.60681, 
        viewOffsetY=-1.30958)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['box_beam-1'].vertices
    a.WirePolyLine(points=((v1[6], v1[1]), ), mergeType=IMPRINT, meshable=OFF)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.edges
    edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
    a.Set(edges=edges1, name='Wire-1-Set-1')


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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2742, 
        farPlane=27.6443, width=0.788207, height=0.712404, 
        viewOffsetX=0.123773, viewOffsetY=0.324935)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.1263, 
        farPlane=26.6136, width=0.827088, height=0.747545, cameraPosition=(
        -6.04557, -13.2256, 22.0066), cameraUpVector=(0.813597, 0.529518, 
        0.240147), cameraTarget=(-0.600219, -0.119178, 5.19628), 
        viewOffsetX=0.129878, viewOffsetY=0.340964)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7725, 
        farPlane=26.069, width=0.856576, height=0.774197, cameraPosition=(
        -15.5306, -8.89468, 18.5166), cameraUpVector=(0.909708, -0.0791112, 
        0.407642), cameraTarget=(-0.665039, 0.217884, 5.10049), 
        viewOffsetX=0.134508, viewOffsetY=0.35312)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2003, 
        farPlane=27.6412, width=9.59569, height=8.67285, viewOffsetX=-0.934504, 
        viewOffsetY=0.8788)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.7138, 
        farPlane=30.1847, width=9.32428, height=8.42754, cameraPosition=(
        6.41897, -3.01842, 27.3597), cameraUpVector=(0.729305, 0.436527, 
        -0.526838), cameraTarget=(-0.132565, -0.426787, 6.51804), 
        viewOffsetX=-0.908072, viewOffsetY=0.853943)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.1239, 
        farPlane=28.7745, width=2.02356, height=1.82895, viewOffsetX=-1.07961, 
        viewOffsetY=-0.441247)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3026, 
        farPlane=29.1048, width=2.04351, height=1.84698, cameraPosition=(
        3.07476, -2.84569, 28.34), cameraUpVector=(0.815976, 0.391778, 
        -0.42508), cameraTarget=(-0.334692, -0.466626, 6.73605), 
        viewOffsetX=-1.09025, viewOffsetY=-0.445595)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3646, 
        farPlane=29.0428, width=1.60087, height=1.44691, viewOffsetX=-1.01667, 
        viewOffsetY=-0.43759)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.2269, 
        farPlane=28.0269, width=1.58887, height=1.43607, cameraPosition=(
        9.10178, -7.03516, 25.0672), cameraUpVector=(0.632309, 0.611294, 
        -0.475925), cameraTarget=(0.105189, -0.516739, 6.07804), 
        viewOffsetX=-1.00905, viewOffsetY=-0.434309)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.9421, 
        farPlane=28.3118, width=3.28638, height=2.97032, viewOffsetX=-1.23882, 
        viewOffsetY=-0.441585)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9121, 
        farPlane=25.0105, width=3.46405, height=3.1309, cameraPosition=(
        17.5839, -10.2767, 13.2175), cameraUpVector=(0.280029, 0.877964, 
        -0.388281), cameraTarget=(0.0161316, -0.0327067, 4.82391), 
        viewOffsetX=-1.30579, viewOffsetY=-0.465459)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.3469, 
        farPlane=24.36, width=3.17735, height=2.87178, cameraPosition=(15.8586, 
        -8.69098, -5.40858), cameraUpVector=(0.14448, 0.988983, 0.0322236), 
        cameraTarget=(-1.04056, 0.855458, 4.95004), viewOffsetX=-1.19772, 
        viewOffsetY=-0.426936)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5712, 
        farPlane=25.8239, width=2.66895, height=2.41227, cameraPosition=(
        2.88701, -0.197451, -15.0164), cameraUpVector=(0.402251, 0.840295, 
        0.363453), cameraTarget=(-0.866907, 0.963981, 6.63022), 
        viewOffsetX=-1.00607, viewOffsetY=-0.358622)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5319, 
        farPlane=25.4713, width=2.66176, height=2.40577, cameraPosition=(
        -6.04164, 1.81424, -14.0107), cameraUpVector=(0.471702, 0.842597, 
        0.25986), cameraTarget=(-0.140318, 0.686865, 7.15347), 
        viewOffsetX=-1.00336, viewOffsetY=-0.357656)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.7834, 
        farPlane=25.2199, width=1.28871, height=1.16477, viewOffsetX=-1.51774, 
        viewOffsetY=-0.519339)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.9895, 
        farPlane=24.2904, width=1.30667, height=1.18101, cameraPosition=(
        -11.1849, 4.52112, -10.5402), cameraUpVector=(0.630385, 0.76035, 
        0.15647), cameraTarget=(0.84452, 0.493759, 7.4346), 
        viewOffsetX=-1.5389, viewOffsetY=-0.526578)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=16.7079, 
        farPlane=21.3673, width=1.45647, height=1.3164, cameraPosition=(
        -16.2314, 8.73782, 0.0541284), cameraUpVector=(0.74558, 0.654122, 
        -0.12742), cameraTarget=(2.65642, -0.251959, 6.86994), 
        viewOffsetX=-1.71532, viewOffsetY=-0.586944)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=15.0159, 
        farPlane=21.9801, width=1.30897, height=1.18309, cameraPosition=(
        -13.5562, 5.90903, 16.219), cameraUpVector=(0.471239, 0.805121, 
        -0.360158), cameraTarget=(3.70355, -0.477417, 4.16346), 
        viewOffsetX=-1.54161, viewOffsetY=-0.527503)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.9422, 
        farPlane=23.3936, width=1.12821, height=1.0197, cameraPosition=(
        -0.273141, 4.03081, 22.7923), cameraUpVector=(0.11565, 0.85657, 
        -0.502905), cameraTarget=(2.01361, -0.308183, 1.3455), 
        viewOffsetX=-1.32871, viewOffsetY=-0.454654)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.9347, 
        farPlane=23.4271, width=1.12755, height=1.01911, cameraPosition=(
        -0.273159, -0.250983, 23.2543), cameraUpVector=(0.15114, 0.945456, 
        -0.288565), cameraTarget=(2.03333, 0.462632, 1.38674), 
        viewOffsetX=-1.32794, viewOffsetY=-0.454389)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=13.2023, 
        farPlane=23.3089, width=1.15088, height=1.0402, cameraPosition=(
        -5.14691, 0.537355, 22.5879), cameraUpVector=(0.236455, 0.931625, 
        -0.275979), cameraTarget=(2.91065, 0.299974, 2.11751), 
        viewOffsetX=-1.35542, viewOffsetY=-0.463791)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['box_beam-1'].vertices
    e1 = a.instances['box_beam-1'].edges
    a.DatumCsysByThreePoints(origin=v1[4], point1=v1[5], name='end', 
        coordSysType=CARTESIAN, 
        point2=a.instances['box_beam-1'].InterestingPoint(edge=e1[8], 
        rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.9305, 
        farPlane=23.4227, width=1.12719, height=1.01879, cameraPosition=(
        -0.0327312, 0.21717, 23.2544), cameraUpVector=(0.143378, 0.938371, 
        -0.314489), cameraTarget=(2.00892, 0.379075, 1.34959), 
        viewOffsetX=-1.32752, viewOffsetY=-0.454244)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.9915, 
        farPlane=23.3616, width=0.781289, height=0.70615, viewOffsetX=-1.39043, 
        viewOffsetY=-0.524598)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=13.04, 
        farPlane=23.3782, width=0.784205, height=0.708787, cameraPosition=(
        -1.36657, -0.63212, 23.2264), cameraUpVector=(0.188379, 0.947569, 
        -0.25812), cameraTarget=(2.27956, 0.479963, 1.55879), 
        viewOffsetX=-1.39562, viewOffsetY=-0.526556)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=13.0078, 
        farPlane=23.3673, width=0.782271, height=0.707038, cameraPosition=(
        -0.408112, -0.247947, 23.2605), cameraUpVector=(0.138584, 0.947702, 
        -0.287498), cameraTarget=(2.07745, 0.499256, 1.41379), 
        viewOffsetX=-1.39218, viewOffsetY=-0.525257)
    mdb.models['Model-1'].ConnectorSection(name='warping', translationalType=SLOT)
    a = mdb.models['Model-1'].rootAssembly
    region=a.sets['Wire-1-Set-1']
    datum1 = mdb.models['Model-1'].rootAssembly.datums[69]
    csa = a.SectionAssignment(sectionName='warping', region=region)
    a.ConnectorOrientation(region=csa.getSet(), localCsys1=datum1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.7122, 
        farPlane=23.6628, width=2.4771, height=2.23887, viewOffsetX=-1.58957, 
        viewOffsetY=-0.154334)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=12.5079, 
        farPlane=23.4892, width=2.4373, height=2.2029, cameraPosition=(4.3566, 
        -0.921421, 22.534), cameraUpVector=(-0.112888, 0.967102, -0.227971), 
        cameraTarget=(1.02803, 1.17039, 0.887787), viewOffsetX=-1.56403, 
        viewOffsetY=-0.151854)


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
    datum1 = mdb.models['Model-1'].rootAssembly.datums[66]
    mdb.models['Model-1'].rootAssembly.connectorOrientations[0].setValues(
        localCsys1=datum1)
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
    mdb.models['Model-1'].ConnectorSection(name='ConnSect-1', 
        translationalType=SLOT)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.edges
    edges1 = e1.getSequenceFromMask(mask=('[#ffffffff #7ffffff ]', ), )
    region=a.Set(edges=edges1, name='wires')
    datum1 = mdb.models['Model-1'].rootAssembly.datums[66]
    csa = a.SectionAssignment(sectionName='ConnSect-1', region=region)
    a.ConnectorOrientation(region=csa.getSet(), localCsys1=datum1)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)


def Macro8():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    a = mdb.models['Model-1'].rootAssembly
    a.ReferencePoint(point=(0.0, 0.0, 10.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.5996, 
        farPlane=25.6405, width=0.391435, height=0.34586, viewOffsetX=-2.84017, 
        viewOffsetY=-1.63471)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    v1 = a.instances['box_beam-1'].vertices
    a.WirePolyLine(points=((r1[416], v1[14]), ), mergeType=IMPRINT, meshable=OFF)
    a = mdb.models['Model-1'].rootAssembly
    e1 = a.edges
    edges1 = e1.getSequenceFromMask(mask=('[#1 ]', ), )
    a.Set(edges=edges1, name='Wire-204-Set-1')
    mdb.models['Model-1'].ConnectorSection(name='beam', assembledType=BEAM)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.6455, 
        farPlane=25.5945, width=0.165014, height=0.145802, viewOffsetX=-2.9379, 
        viewOffsetY=-1.65048)
    a = mdb.models['Model-1'].rootAssembly
    region=a.sets['Wire-204-Set-1']
    csa = a.SectionAssignment(sectionName='beam', region=region)
    a.ConnectorOrientation(region=csa.getSet(), localCsys1=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[416], )
    region = a.Set(referencePoints=refPoints1, name='Set-209')
    mdb.models['Model-1'].ConcentratedForce(name='Load-2', 
        createStepName='loading', region=region, cf2=-286.4, 
        distributionType=UNIFORM, field='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9105, 
        farPlane=27.3508, width=0.167359, height=0.147873, cameraPosition=(
        12.3223, 8.92973, 22.4249), cameraUpVector=(-0.453491, 0.73071, 
        -0.510303), cameraTarget=(0.357108, 0.142383, 6.02633), 
        viewOffsetX=-2.97965, viewOffsetY=-1.67394)


def Macro9():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    r1 = a.referencePoints
    refPoints1=(r1[142], )
    region = a.Set(referencePoints=refPoints1, name='Set-141')
    mdb.models['Model-1'].Moment(name='Load-2', createStepName='loading', 
        region=region, cm2=100.0, distributionType=UNIFORM, field='', 
        localCsys=None)


def Macro10():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.16238, 
        farPlane=9.33848, width=7.99697, height=3.00985, viewOffsetX=0.435712, 
        viewOffsetY=0.126482)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p1 = mdb.models['Model-1'].parts['box_beam']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.66073, 
        farPlane=8.94582, width=5.33195, height=2.01182, cameraPosition=(
        6.18123, -0.629785, 5.34165), cameraUpVector=(-0.248798, 0.963517, 
        -0.0986657), cameraTarget=(-0.0230979, -0.103922, 1.62702))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.88655, 
        farPlane=8.73656, width=5.54466, height=2.09208, cameraPosition=(
        6.27432, -3.24859, 3.38761), cameraUpVector=(0.0538813, 0.982616, 
        0.177657), cameraTarget=(-0.0224243, -0.122872, 1.61288))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.82368, 
        farPlane=8.90184, width=5.48544, height=2.06974, cameraPosition=(
        4.50474, -5.37267, 3.75255), cameraUpVector=(0.386114, 0.892432, 
        0.233414), cameraTarget=(-0.0372183, -0.14063, 1.61593))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.20372, 
        farPlane=8.68226, width=5.84341, height=2.20481, cameraPosition=(
        -0.451047, -7.25808, 3.09075), cameraUpVector=(0.817457, 0.390609, 
        0.423306), cameraTarget=(-0.112826, -0.169394, 1.60583))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.94811, 
        farPlane=9.05199, width=5.60265, height=2.11397, cameraPosition=(
        -3.86118, -6.00619, 3.79782), cameraUpVector=(0.884437, 0.0326369, 
        0.465517), cameraTarget=(-0.201047, -0.137007, 1.62412))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.96338, 
        farPlane=9.03671, width=5.61705, height=2.1194, cameraPosition=(
        -3.86118, -6.00619, 3.79782), cameraUpVector=(0.950712, -0.249359, 
        -0.1843), cameraTarget=(-0.201047, -0.137007, 1.62412))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.50798, 
        farPlane=9.5436, width=5.1881, height=1.95755, cameraPosition=(1.97588, 
        -0.0664924, 8.76227), cameraUpVector=(0.76067, -0.313175, -0.568598), 
        cameraTarget=(-0.00678343, 0.0606723, 1.78934))
    p = mdb.models['Model-1'].parts['box_beam']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['box_beam']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#12a ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.05, deviationFactor=0.001, 
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['box_beam']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.01, deviationFactor=0.001, 
        minSizeFactor=0.001, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.85064, 
        farPlane=9.23845, width=5.51086, height=2.07933, cameraPosition=(
        3.66349, 5.64556, 4.91144), cameraUpVector=(0.617093, -0.77233, 
        -0.150674), cameraTarget=(0.0549617, 0.269661, 1.64845))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.83147, 
        farPlane=9.25762, width=5.16324, height=1.94817, viewOffsetX=0.0422788, 
        viewOffsetY=-0.0042013)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=6.31251, 
        farPlane=8.71041, width=5.58915, height=2.10887, cameraPosition=(
        3.82112, 6.44193, 0.922296), cameraUpVector=(0.630829, -0.775133, 
        0.0349624), cameraTarget=(0.0463625, 0.277469, 1.48753), 
        viewOffsetX=0.0457664, viewOffsetY=-0.00454786)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.46789, 
        farPlane=9.58055, width=4.84131, height=1.8267, cameraPosition=(2.7829, 
        -0.926122, 8.43095), cameraUpVector=(0.741866, 0.158841, -0.651463), 
        cameraTarget=(0.00930881, 0.0802162, 1.80801), viewOffsetX=0.0396428, 
        viewOffsetY=-0.00393935)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.69836, 
        farPlane=9.35008, width=2.40119, height=0.906007, 
        viewOffsetX=0.0173395, viewOffsetY=-0.0319586)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.99423, 
        farPlane=8.95709, width=2.52587, height=0.953049, cameraPosition=(
        0.626236, -6.09477, 5.78611), cameraUpVector=(0.904507, 0.311566, 
        -0.291194), cameraTarget=(-0.06346, -0.120337, 1.73651), 
        viewOffsetX=0.0182399, viewOffsetY=-0.0336179)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.98571, 
        farPlane=8.9656, width=2.37094, height=0.894593, 
        viewOffsetX=-0.0170413, viewOffsetY=-0.0371436)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.99657, 
        farPlane=8.95474, width=2.37524, height=0.896215, cameraPosition=(
        0.628039, -6.09258, 5.78904), cameraUpVector=(0.906782, 0.353976, 
        -0.229014), cameraTarget=(-0.0616567, -0.118145, 1.73944), 
        viewOffsetX=-0.0170722, viewOffsetY=-0.037211)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.87202, 
        farPlane=9.3231, width=2.32591, height=0.877601, cameraPosition=(
        0.44871, -0.132235, 9.08393), cameraUpVector=(0.916413, 0.0345837, 
        -0.398738), cameraTarget=(-0.0666435, 0.0498294, 1.85412), 
        viewOffsetX=-0.0167176, viewOffsetY=-0.0364381)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.74641, 
        farPlane=9.44872, width=4.26059, height=1.60759, viewOffsetX=0.45781, 
        viewOffsetY=0.318197)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.65226, 
        farPlane=9.41813, width=4.19079, height=1.58125, cameraPosition=(
        0.308993, 0.667289, 8.99996), cameraUpVector=(0.924701, -0.03018, 
        -0.379497), cameraTarget=(-0.0585198, 0.0978407, 1.78127), 
        viewOffsetX=0.45031, viewOffsetY=0.312984)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.45817, 
        farPlane=9.61222, width=7.179, height=2.70874, viewOffsetX=0.0298143, 
        viewOffsetY=1.09739)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.76524, 
        farPlane=9.12866, width=6.2676, height=2.36486, cameraPosition=(
        -2.27008, 0.0253148, 8.1558), cameraUpVector=(0.768874, -0.618591, 
        -0.161797), cameraTarget=(0.320153, 1.08721, 1.46761), 
        viewOffsetX=0.0260293, viewOffsetY=0.958077)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.12041, 
        farPlane=8.77349, width=2.35231, height=0.887562, viewOffsetX=0.275479, 
        viewOffsetY=0.54587)
    p = mdb.models['Model-1'].parts['box_beam']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['box_beam']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.005, deviationFactor=0.001, 
        minSizeFactor=0.001, constraint=FINER)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.1303, 
        farPlane=8.1873, width=2.35686, height=0.889277, cameraPosition=(
        -2.85469, -4.37806, 5.76341), cameraUpVector=(0.831865, -0.334544, 
        -0.44281), cameraTarget=(0.275346, 1.03627, 2.09508), 
        viewOffsetX=0.276011, viewOffsetY=0.546925)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.32744, 
        farPlane=8.97204, width=2.44743, height=0.923451, cameraPosition=(
        1.73242, 1.54202, 8.29097), cameraUpVector=(0.792485, -0.083625, 
        -0.604132), cameraTarget=(-0.518469, 0.344861, 1.50355), 
        viewOffsetX=0.286617, viewOffsetY=0.567942)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.43681, 
        farPlane=8.86267, width=0.872387, height=0.329165, 
        viewOffsetX=0.259065, viewOffsetY=0.463427)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.47336, 
        farPlane=8.81459, width=0.878252, height=0.331378, cameraPosition=(
        1.39472, 0.64213, 8.50314), cameraUpVector=(0.807158, 0.114379, 
        -0.579148), cameraTarget=(-0.558174, 0.253078, 1.53151), 
        viewOffsetX=0.260807, viewOffsetY=0.466542)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.48758, 
        farPlane=8.80035, width=0.646229, height=0.243832, 
        viewOffsetX=0.227711, viewOffsetY=0.508982)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.41508, 
        farPlane=8.8206, width=0.63769, height=0.24061, cameraPosition=(
        1.17347, -2.07068, 8.23629), cameraUpVector=(0.838433, 0.136523, 
        -0.527628), cameraTarget=(-0.506667, 0.355997, 1.61382), 
        viewOffsetX=0.224702, viewOffsetY=0.502257)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.38488, 
        farPlane=8.85078, width=1.1067, height=0.417575, viewOffsetX=0.267708, 
        viewOffsetY=0.498459)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.39593, 
        farPlane=8.86098, width=1.10897, height=0.418432, cameraPosition=(
        1.76699, -1.04683, 8.35405), cameraUpVector=(0.789806, 0.0851289, 
        -0.607421), cameraTarget=(-0.507799, 0.353978, 1.61374), 
        viewOffsetX=0.268257, viewOffsetY=0.499482)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.44453, 
        farPlane=8.81238, width=0.442317, height=0.166893, 
        viewOffsetX=-0.160797, viewOffsetY=0.435722)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.44667, 
        farPlane=8.81025, width=0.44249, height=0.166958, cameraPosition=(
        1.78455, -1.09455, 8.33821), cameraUpVector=(0.789719, 0.165968, 
        -0.590591), cameraTarget=(-0.490239, 0.30626, 1.5979), 
        viewOffsetX=-0.16086, viewOffsetY=0.435893)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.54579, 
        farPlane=8.84315, width=0.450542, height=0.169996, cameraPosition=(
        1.90674, -0.268084, 8.4559), cameraUpVector=(0.777764, 0.122727, 
        -0.616458), cameraTarget=(-0.481895, 0.2914, 1.63314), 
        viewOffsetX=-0.163787, viewOffsetY=0.443825)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.54068, 
        farPlane=8.84825, width=0.478859, height=0.180681, 
        viewOffsetX=-0.162168, viewOffsetY=0.430295)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.61549, 
        farPlane=8.85417, width=0.485324, height=0.18312, cameraPosition=(
        1.76738, 0.292127, 8.53523), cameraUpVector=(0.791031, 0.0486194, 
        -0.609841), cameraTarget=(-0.490466, 0.315079, 1.64537), 
        viewOffsetX=-0.164357, viewOffsetY=0.436104)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.61723, 
        farPlane=8.85242, width=0.428966, height=0.161855, 
        viewOffsetX=-0.144047, viewOffsetY=0.45206)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.6193, 
        farPlane=8.85035, width=0.429123, height=0.161915, cameraPosition=(
        1.75941, 0.316037, 8.53792), cameraUpVector=(0.792097, 0.00953236, 
        -0.610321), cameraTarget=(-0.498434, 0.338989, 1.64806), 
        viewOffsetX=-0.1441, viewOffsetY=0.452227)
    session.viewports['Viewport: 1'].view.setValues(width=0.430048, 
        height=0.162264, cameraPosition=(0.058291, 7.76452, 1.48266), 
        cameraUpVector=(0, 0, 1), cameraTarget=(0.058291, 0.529694, 1.48266), 
        viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7.29312, 
        0.529694, 1.48266), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.058291, 
        0.529694, 8.71749))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.41276, 
        farPlane=9.02222, width=4.22386, height=1.59372, viewOffsetX=-0.439808, 
        viewOffsetY=-0.583119)
    p = mdb.models['Model-1'].parts['box_beam']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#491491 ]', ), )
    p.Set(edges=edges, name='Set-2')
    p = mdb.models['Model-1'].parts['box_beam']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['box_beam']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#491491 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=0.025, constraint=FINER)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.61417, 
        farPlane=8.82081, width=1.27096, height=0.479553, 
        viewOffsetX=-0.409256, viewOffsetY=-0.232512)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.39199, 
        farPlane=9.04299, width=4.49453, height=1.69586, viewOffsetX=-0.440967, 
        viewOffsetY=-0.166023)
    p = mdb.models['Model-1'].parts['box_beam']
    c = p.cells
    pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.deleteMesh(regions=pickedRegions)
    p = mdb.models['Model-1'].parts['box_beam']
    f = p.faces
    p.PartitionFaceByAuto(face=f[8])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.62563, 
        farPlane=8.80936, width=1.27877, height=0.482498, 
        viewOffsetX=-0.423814, viewOffsetY=-0.111342)
    p = mdb.models['Model-1'].parts['box_beam']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.31153, 
        farPlane=9.12345, width=5.62111, height=2.12093, viewOffsetX=-0.537548, 
        viewOffsetY=-0.272217)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.98985, 
        farPlane=8.42682, width=5.28068, height=1.99248, cameraPosition=(
        5.25478, 2.90938, 4.67394), cameraUpVector=(-0.516548, 0.728407, 
        0.450113), cameraTarget=(-0.707862, 0.881011, 1.11368), 
        viewOffsetX=-0.504993, viewOffsetY=-0.25573)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.68651, 
        farPlane=8.81146, width=4.95966, height=1.87135, cameraPosition=(
        1.74147, -0.797514, 8.07004), cameraUpVector=(-0.69891, 0.60372, 
        0.383468), cameraTarget=(-0.183719, 1.21499, 1.39274), 
        viewOffsetX=-0.474293, viewOffsetY=-0.240184)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.04014, 
        farPlane=8.96906, width=5.3339, height=2.01256, cameraPosition=(
        -1.55592, 0.774044, 8.34132), cameraUpVector=(-0.0448364, 0.998818, 
        -0.0187428), cameraTarget=(0.51101, 0.736718, 1.40812), 
        viewOffsetX=-0.510081, viewOffsetY=-0.258307)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.88724, 
        farPlane=8.87732, width=5.17209, height=1.95151, cameraPosition=(
        1.75624, 0.362174, 8.20099), cameraUpVector=(-0.00310397, 0.998672, 
        0.0514297), cameraTarget=(0.436612, 0.723921, 1.09673), 
        viewOffsetX=-0.494607, viewOffsetY=-0.250471)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4.96485, 
        farPlane=8.87946, width=5.25423, height=1.9825, cameraPosition=(
        0.0651161, 0.195083, 8.4719), cameraUpVector=(0.0390548, 0.996696, 
        0.0712174), cameraTarget=(0.548961, 0.690696, 1.2703), 
        viewOffsetX=-0.502461, viewOffsetY=-0.254448)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.07132, 
        farPlane=8.773, width=4.02003, height=1.51682, viewOffsetX=-0.446136, 
        viewOffsetY=-0.285533)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.06247, 
        farPlane=8.77905, width=4.01301, height=1.51417, cameraPosition=(
        1.14416, 0.563458, 8.35877), cameraUpVector=(-0.0478803, 0.998453, 
        0.0282557), cameraTarget=(0.463161, 0.73457, 1.15809), 
        viewOffsetX=-0.445358, viewOffsetY=-0.285035)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.06775, 
        farPlane=8.92983, width=4.0172, height=1.51575, cameraPosition=(
        1.28102, 2.38163, 8.01439), cameraUpVector=(-0.10141, 0.968438, 
        -0.227694), cameraTarget=(0.430991, 0.652997, 1.04071), 
        viewOffsetX=-0.445822, viewOffsetY=-0.285332)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.12957, 
        farPlane=8.86801, width=3.02098, height=1.13986, viewOffsetX=-0.632474, 
        viewOffsetY=-0.890315)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5.40637, 
        farPlane=8.9252, width=3.184, height=1.20137, cameraPosition=(0.308854, 
        0.785508, 8.67404), cameraUpVector=(0.0133437, 0.999796, -0.0151914), 
        cameraTarget=(0.617794, 0.671561, 1.44669), viewOffsetX=-0.666603, 
        viewOffsetY=-0.938357)
def Macro11():
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
    p = mdb.models['Model-1'].parts['box_beam']
    f = p.faces
    p.PartitionFaceByAuto(face=f[8])
