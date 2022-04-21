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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.1)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(110.0, 54.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0637679, 
        farPlane=0.124794, width=0.150296, height=0.139354, cameraPosition=(
        -0.0492552, -0.00948952, 0.0942809), cameraTarget=(-0.0492552, 
        -0.00948952, 0))
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0869286, 
        farPlane=0.101633, width=0.0362149, height=0.0335785, cameraPosition=(
        -0.0033514, -0.00245593, 0.0942809), cameraTarget=(-0.0033514, 
        -0.00245593, 0))
    s.rectangle(point1=(0.0, 0.0), point2=(0.11, 0.054))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0869286, 
        farPlane=0.101633, cameraPosition=(-0.00744166, -0.0021931, 0.0942809), 
        cameraTarget=(-0.00744166, -0.0021931, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0194511, 
        0.00920667, 0.0942809), cameraTarget=(0.0194511, 0.00920667, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0521922, 
        farPlane=0.13637, width=0.234623, height=0.217543, cameraPosition=(
        -0.00737668, -0.028954, 0.0942809), cameraTarget=(-0.00737668, 
        -0.028954, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0555799, 
        0.0057798, 0.0942809), cameraTarget=(0.0555799, 0.0057798, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0652452, 
        farPlane=0.123317, width=0.161859, height=0.150076, cameraPosition=(
        -0.00659176, -0.00580011, 0.0942809), cameraTarget=(-0.00659176, 
        -0.00580011, 0))
    s.rectangle(point1=(0.002, 0.002), point2=(0.108, 0.052))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0577985, 
        0.0156394, 0.0942809), cameraTarget=(0.0577985, 0.0156394, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0847478, 
        farPlane=0.103814, width=0.0469564, height=0.0435381, cameraPosition=(
        0.0182926, 0.0054339, 0.0942809), cameraTarget=(0.0182926, 0.0054339, 
        0))
    s.Arc3Points(point1=(0.0, 0.004), point2=(0.004, 0.0), point3=(0.0, 0.003))
    s.CoincidentConstraint(entity1=v[8], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[9], entity2=g[5], addUndoState=False)
    s.CoincidentConstraint(entity1=v[10], entity2=g[2], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0858575, 
        farPlane=0.102704, width=0.0414907, height=0.0384703, cameraPosition=(
        0.0164751, 0.00497821, 0.0942809), cameraTarget=(0.0164751, 0.00497821, 
        0))
    s.Arc3Points(point1=(0.002, 0.006), point2=(0.0055, 0.002), point3=(0.002, 
        0.0055))
    s.CoincidentConstraint(entity1=v[11], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[12], entity2=g[9], addUndoState=False)
    s.CoincidentConstraint(entity1=v[13], entity2=g[6], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.085823, 
        farPlane=0.102739, width=0.0416605, height=0.0386277, cameraPosition=(
        0.0112385, 0.0434765, 0.0942809), cameraTarget=(0.0112385, 0.0434765, 
        0))
    s.Arc3Points(point1=(0.002, 0.048), point2=(0.006, 0.052), point3=(0.0055, 
        0.052))
    s.CoincidentConstraint(entity1=v[14], entity2=g[6], addUndoState=False)
    s.CoincidentConstraint(entity1=v[15], entity2=g[7], addUndoState=False)
    s.CoincidentConstraint(entity1=v[16], entity2=g[7], addUndoState=False)
    s.Arc3Points(point1=(0.0, 0.05), point2=(0.004, 0.054), point3=(0.0035, 0.054))
    s.CoincidentConstraint(entity1=v[17], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[18], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[19], entity2=g[3], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0883982, 
        farPlane=0.100164, width=0.028976, height=0.0268666, cameraPosition=(
        0.100405, 0.0533021, 0.0942809), cameraTarget=(0.100405, 0.0533021, 0))
    s.Arc3Points(point1=(0.107, 0.054), point2=(0.11, 0.0515), point3=(0.11, 
        0.052))
    s.CoincidentConstraint(entity1=v[20], entity2=g[3], addUndoState=False)
    s.CoincidentConstraint(entity1=v[21], entity2=g[4], addUndoState=False)
    s.CoincidentConstraint(entity1=v[22], entity2=g[4], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0867462, 
        farPlane=0.101816, width=0.037113, height=0.0344113, cameraPosition=(
        0.0979198, 0.0542585, 0.0942809), cameraTarget=(0.0979198, 0.0542585, 
        0))
    s.Arc3Points(point1=(0.1045, 0.052), point2=(0.108, 0.049), point3=(0.108, 
        0.0495))
    s.CoincidentConstraint(entity1=v[23], entity2=g[7], addUndoState=False)
    s.CoincidentConstraint(entity1=v[24], entity2=g[8], addUndoState=False)
    s.CoincidentConstraint(entity1=v[25], entity2=g[8], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0751418, 
        farPlane=0.11342, width=0.0942718, height=0.0874091, cameraPosition=(
        0.0842029, 0.0653765, 0.0942809), cameraTarget=(0.0842029, 0.0653765, 
        0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0842029, 
        0.0268871, 0.0942809), cameraTarget=(0.0842029, 0.0268871, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.085135, 
        farPlane=0.103427, width=0.0450494, height=0.0417699, cameraPosition=(
        0.0990549, 0.012467, 0.0942809), cameraTarget=(0.0990549, 0.012467, 0))
    s.Arc3Points(point1=(0.11, 0.004), point2=(0.1065, 0.0), point3=(0.11, 0.003))
    s.CoincidentConstraint(entity1=v[26], entity2=g[4], addUndoState=False)
    s.CoincidentConstraint(entity1=v[27], entity2=g[5], addUndoState=False)
    s.CoincidentConstraint(entity1=v[28], entity2=g[4], addUndoState=False)
    s.Arc3Points(point1=(0.1045, 0.002), point2=(0.108, 0.006), point3=(0.108, 
        0.0055))
    s.CoincidentConstraint(entity1=v[29], entity2=g[9], addUndoState=False)
    s.CoincidentConstraint(entity1=v[30], entity2=g[8], addUndoState=False)
    s.CoincidentConstraint(entity1=v[31], entity2=g[8], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0879197, 
        farPlane=0.100642, width=0.0313331, height=0.0290521, cameraPosition=(
        0.013952, 0.00877191, 0.0942809), cameraTarget=(0.013952, 0.00877191, 
        0))
    s.autoTrimCurve(curve1=g[2], point1=(0.000143003650009632, 0.0010696379467845))
    s.autoTrimCurve(curve1=g[5], point1=(0.000827345065772533, 
        9.15713608264923e-05))
    s.autoTrimCurve(curve1=g[9], point1=(0.00395576190203428, 0.00199880078434944))
    s.autoTrimCurve(curve1=g[6], point1=(0.00190273858606815, 0.0035637067630887))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0866221, 
        farPlane=0.10194, width=0.0377241, height=0.0349779, cameraPosition=(
        0.0108317, 0.0448154, 0.0942809), cameraTarget=(0.0108317, 0.0448154, 
        0))
    s.autoTrimCurve(curve1=g[18], point1=(-0.000144193880259991, 
        0.053441010415554))
    s.autoTrimCurve(curve1=g[3], point1=(0.00103284511715174, 0.0540297962725163))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0838453, 
        farPlane=0.104717, width=0.0581734, height=0.0539385, cameraPosition=(
        0.0136815, 0.0449906, 0.0942809), cameraTarget=(0.0136815, 0.0449906, 
        0))
    s.autoTrimCurve(curve1=g[21], point1=(0.00192883796989918, 0.0508468747138977))
    s.autoTrimCurve(curve1=g[7], point1=(0.00301788747310638, 0.0522995889186859))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0882769, 
        farPlane=0.100285, width=0.0295736, height=0.0274207, cameraPosition=(
        0.0995374, 0.0520875, 0.0942809), cameraTarget=(0.0995374, 0.0520875, 
        0))
    s.autoTrimCurve(curve1=g[25], point1=(0.1068961545825, 0.0521567054092884))
    s.autoTrimCurve(curve1=g[15], point1=(0.105142965912819, 0.0518336072564125))
    s.autoTrimCurve(curve1=g[8], point1=(0.108280256390572, 0.0513258762657642))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0917561, 
        farPlane=0.0968057, width=0.0124364, height=0.011531, cameraPosition=(
        0.104625, 0.0501196, 0.0942809), cameraTarget=(0.104625, 0.0501196, 0))
    s.autoTrimCurve(curve1=g[27], point1=(0.108126975595951, 0.0492364168167114))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.091047, 
        farPlane=0.0975148, width=0.0180271, height=0.0167148, cameraPosition=(
        0.10269, 0.0507503, 0.0942809), cameraTarget=(0.10269, 0.0507503, 0))
    s.autoTrimCurve(curve1=g[14], point1=(0.107709549367428, 0.0541969910264015))
    s.autoTrimCurve(curve1=g[23], point1=(0.109537579119205, 0.0540281757712364))
    s.autoTrimCurve(curve1=g[4], point1=(0.10993130505085, 0.0534373186528683))
    s.autoTrimCurve(curve1=g[30], point1=(0.110015675425529, 0.0517491586506367))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0882276, 
        farPlane=0.100334, width=0.0298161, height=0.0276455, cameraPosition=(
        0.0935036, 0.0142335, 0.0942809), cameraTarget=(0.0935036, 0.0142335, 
        0))
    s.autoTrimCurve(curve1=g[20], point1=(0.105946317315102, 0.0018317848443985))
    s.autoTrimCurve(curve1=g[28], point1=(0.108039490878582, 0.0031347842887044))
    s.autoTrimCurve(curve1=g[17], point1=(0.107992976903915, 0.00578731670975685))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0859652, 
        farPlane=0.102597, width=0.0409598, height=0.037978, cameraPosition=(
        0.0911823, 0.0155209, 0.0942809), cameraTarget=(0.0911823, 0.0155209, 
        0))
    s.autoTrimCurve(curve1=g[19], point1=(0.109234020113945, 
        -0.000173507258296013))
    s.autoTrimCurve(curve1=g[32], point1=(0.109936915338039, 0.00110505800694227))
    s.autoTrimCurve(curve1=g[16], point1=(0.110320314764977, 0.00308683328330517))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0635371, 
        farPlane=0.125025, width=0.151432, height=0.140408, cameraPosition=(
        0.0497864, 0.0573825, 0.0942809), cameraTarget=(0.0497864, 0.0573825, 
        0))
    s.undo()
    s.CircleByCenterPerimeter(center=(0.0265, 0.027), point1=(0.002, 0.0345))
    s.CoincidentConstraint(entity1=v[49], entity2=g[24], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0796493, 
        farPlane=0.108913, width=0.0815638, height=0.0756261, cameraPosition=(
        0.0396705, 0.0265927, 0.0942809), cameraTarget=(0.0396705, 0.0265927, 
        0))
    s.CircleByCenterPerimeter(center=(0.0265, 0.027), point1=(0.013, 0.045))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0796493, 
        farPlane=0.108913, width=0.0720697, height=0.0668232, cameraPosition=(
        0.0307536, 0.0285253, 0.0942809), cameraTarget=(0.0307536, 0.0285253, 
        0))
    s.autoTrimCurve(curve1=g[24], point1=(0.00146467797458172, 0.0285815857350826))
    s.autoTrimCurve(curve1=g[22], point1=(0.000452777370810509, 
        0.0271193012595177))
    s.undo()
    s.autoTrimCurve(curve1=g[39], point1=(0.000790076330304146, 
        0.0254320502281189))
    s.autoTrimCurve(curve1=g[43], point1=(0.0250756740570068, 0.0529904961585999))
    s.autoTrimCurve(curve1=g[26], point1=(0.0258627068251371, 0.0515282079577446))
    s.autoTrimCurve(curve1=g[44], point1=(0.028223805129528, 0.00113562680780888))
    s.autoTrimCurve(curve1=g[34], point1=(0.028223805129528, 0.00203549489378929))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0745609, 
        farPlane=0.114001, width=0.274908, height=0.103468, cameraPosition=(
        0.0471318, 0.0294169, 0.0942809), cameraTarget=(0.0471318, 0.0294169, 
        0))
    s.removeGapsAndOverlaps(geomList=(g[10], g[11], g[12], g[13], g[16], g[22], 
        g[29], g[31], g[33], g[35], g[36], g[37], g[38], g[40], g[41], g[42], 
        g[45], g[46], g[47], g[48], g[49], g[50], g[51]), tolerance=0.001)
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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=0.2)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.sketchOptions.setValues(decimalPlaces=3)
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(0.11, 0.054))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.165087, 
        farPlane=0.212036, width=0.289155, height=0.10883, cameraPosition=(
        -0.023757, 0.0109914, 0.188562), cameraTarget=(-0.023757, 0.0109914, 
        0))
    s.rectangle(point1=(0.002, 0.002), point2=(0.108, 0.052))
    s.CircleByCenterPerimeter(center=(0.0275, 0.027), point1=(0.002, 
        0.0302708651870489))
    s.CoincidentConstraint(entity1=v[9], entity2=g[6], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.180855, 
        farPlane=0.196269, width=0.0949362, height=0.0357315, cameraPosition=(
        -0.00482501, 0.0208032, 0.188562), cameraTarget=(-0.00482501, 
        0.0208032, 0))
    s.autoTrimCurve(curve1=g[6], point1=(0.00219303835183382, 0.0270739272236824))
    s.autoTrimCurve(curve1=g[10], point1=(0.00160079542547464, 0.0265415050089359))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.17653, 
        farPlane=0.200593, width=0.148203, height=0.0557796, cameraPosition=(
        -0.00287753, 0.0308324, 0.188562), cameraTarget=(-0.00287753, 
        0.0308324, 0))
    s.autoTrimCurve(curve1=g[13], point1=(0.0263839475810528, 0.0527194514870644))
    s.autoTrimCurve(curve1=g[7], point1=(0.02647640183568, 0.0521653555333614))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.178404, 
        farPlane=0.19872, width=0.125122, height=0.0470924, cameraPosition=(
        0.00158663, 0.00584334, 0.188562), cameraTarget=(0.00158663, 
        0.00584334, 0))
    s.autoTrimCurve(curve1=g[14], point1=(0.0267592463642359, 0.00124325091019273))
    s.autoTrimCurve(curve1=g[9], point1=(0.0273056272417307, 0.00241276295855641))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.181439, 
        farPlane=0.195685, width=0.0877387, height=0.0330225, cameraPosition=(
        0.00914519, 0.0396046, 0.188562), cameraTarget=(0.00914519, 0.0396046, 
        0))
    s.CircleByCenterPerimeter(center=(0.0275, 0.027), point1=(0.0249907001852989, 
        0.0506485402584076))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.18086, 
        farPlane=0.196264, width=0.0948759, height=0.0357088, cameraPosition=(
        -0.00601379, 0.0037113, 0.188562), cameraTarget=(-0.00601379, 
        0.0037113, 0))
    s.Arc3Points(point1=(0.00375, 0.0), point2=(0.0, 0.00375), point3=(0.0, 
        0.0025))
    s.CoincidentConstraint(entity1=v[18], entity2=g[5], addUndoState=False)
    s.CoincidentConstraint(entity1=v[19], entity2=g[2], addUndoState=False)
    s.CoincidentConstraint(entity1=v[20], entity2=g[2], addUndoState=False)
    s.Arc3Points(point1=(0.005, 0.002), point2=(0.002, 0.005), point3=(0.002, 
        0.00375))
    s.CoincidentConstraint(entity1=v[21], entity2=g[21], addUndoState=False)
    s.CoincidentConstraint(entity1=v[22], entity2=g[11], addUndoState=False)
    s.CoincidentConstraint(entity1=v[23], entity2=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.171977, 
        farPlane=0.205147, width=0.204296, height=0.0768916, cameraPosition=(
        -0.00581916, -0.0139112, 0.188562), cameraTarget=(-0.00581916, 
        -0.0139112, 0))
    s.undo()
    s.undo()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.179059, 
        farPlane=0.198065, width=0.117061, height=0.0440585, cameraPosition=(
        -0.00356072, -0.0084753, 0.188562), cameraTarget=(-0.00356072, 
        -0.0084753, 0))
    s.FilletByRadius(radius=0.002, curve1=g[2], nearPoint1=(-1.89661514014006e-05, 
        0.00137221906334162), curve2=g[5], nearPoint2=(0.00224483688361943, 
        -0.00037845317274332))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.183116, 
        farPlane=0.194007, width=0.0670751, height=0.0252453, cameraPosition=(
        -0.000830858, -0.00372771, 0.188562), cameraTarget=(-0.000830858, 
        -0.00372771, 0))
    s.FilletByRadius(radius=0.002, curve1=g[21], nearPoint1=(0.00437865918502212, 
        0.00195666728541255), curve2=g[11], nearPoint2=(0.00203542551025748, 
        0.00321057206019759))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=1.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76505, 
        farPlane=2.64222, width=1.42501, height=0.536336, viewOffsetX=0.084749, 
        viewOffsetY=0.0251273)
    p = mdb.models['Model-1'].parts['Part-1']
    s1 = p.features['Solid extrude-1'].sketch
    mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
    s2 = mdb.models['Model-1'].sketches['__edit__']
    g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
    s2.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s2, 
        upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03882, 
        farPlane=2.05569, width=0.103888, height=0.0391005, cameraPosition=(
        0.0297736, 0.036313, 2.04726), cameraTarget=(0.0297736, 0.036313, 0))
    s2.FilletByRadius(radius=0.002, curve1=g[2], nearPoint1=(-0.000329863280057907, 
        0.0515259727835655), curve2=g[3], nearPoint2=(0.00154957547783852, 
        0.0540506765246391))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03248, 
        farPlane=2.06204, width=0.20603, height=0.0775442, cameraPosition=(
        0.0377359, 0.0216214, 2.04726), cameraTarget=(0.0377359, 0.0216214, 0))
    s2.FilletByRadius(radius=0.002, curve1=g[3], nearPoint1=(0.101806938648224, 
        0.0541027076542377), curve2=g[4], nearPoint2=(0.109904199838638, 
        0.0516633950173855))
    s2.FilletByRadius(radius=0.002, curve1=g[17], nearPoint1=(0.104248970746994, 
        0.0523053221404552), curve2=g[8], nearPoint2=(0.10733363032341, 
        0.0502511747181416))
    s2.FilletByRadius(radius=0.002, curve1=g[17], nearPoint1=(0.10296368598938, 
        0.0524337030947208), curve2=g[8], nearPoint2=(0.107205107808113, 
        0.0506363250315189))
    s2.FilletByRadius(radius=0.002, curve1=g[17], nearPoint1=(0.106305405497551, 
        0.0521769337356091), curve2=g[8], nearPoint2=(0.107590690255165, 
        0.0508930943906307))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03141, 
        farPlane=2.06311, width=0.195256, height=0.0734892, cameraPosition=(
        0.055248, 0.0134519, 2.04726), cameraTarget=(0.055248, 0.0134519, 0))
    s2.FilletByRadius(radius=0.002, curve1=g[5], nearPoint1=(0.105736844241619, 
        0.000433132983744144), curve2=g[4], nearPoint2=(0.110121868550777, 
        0.002136523835361))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.0376, 
        farPlane=2.05692, width=0.119022, height=0.0447967, cameraPosition=(
        0.077814, 0.0137067, 2.04726), cameraTarget=(0.077814, 0.0137067, 0))
    s2.undo()
    s2.Arc3Points(point1=(0.105, 0.002), point2=(0.108, 0.005), point3=(0.108, 
        0.00375))
    s2.CoincidentConstraint(entity1=v[30], entity2=g[20], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[31], entity2=g[8], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[32], entity2=g[8], addUndoState=False)
    s2.Arc3Points(point1=(0.1075, 0.0), point2=(0.11, 0.0025), point3=(0.11, 
        0.00125))
    s2.CoincidentConstraint(entity1=v[33], entity2=g[5], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[34], entity2=g[4], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[35], entity2=g[4], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03923, 
        farPlane=2.05528, width=0.0988579, height=0.0372075, cameraPosition=(
        0.0364231, 0.0147465, 2.04726), cameraTarget=(0.0364231, 0.0147465, 0))
    s2.Arc3Points(point1=(0.002, 0.005), point2=(0.005, 0.002), point3=(0.002, 
        0.00375))
    s2.CoincidentConstraint(entity1=v[36], entity2=g[11], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[37], entity2=g[21], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[38], entity2=g[11], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.03553, 
        farPlane=2.05899, width=0.144474, height=0.0543762, cameraPosition=(
        0.0529903, 0.0366439, 2.04726), cameraTarget=(0.0529903, 0.0366439, 0))
    s2.Arc3Points(point1=(0.005, 0.052), point2=(0.002, 0.04875), point3=(0.00375, 
        0.052))
    s2.CoincidentConstraint(entity1=v[39], entity2=g[16], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[40], entity2=g[12], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[41], entity2=g[16], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04359, 
        farPlane=2.05092, width=0.0451376, height=0.0169886, cameraPosition=(
        0.0186992, 0.0487502, 2.04726), cameraTarget=(0.0186992, 0.0487502, 0))
    s2.autoTrimCurve(curve1=g[12], point1=(0.00207175873219967, 
        0.0495659075677395))
    s2.autoTrimCurve(curve1=g[31], point1=(0.00195912458002567, 
        0.0511972643435001))
    s2.autoTrimCurve(curve1=g[16], point1=(0.00252228975296021, 
        0.0520691946148872))
    s2.autoTrimCurve(curve1=g[29], point1=(0.004352574236691, 0.0521535761654377))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04037, 
        farPlane=2.05414, width=0.0848309, height=0.0319281, cameraPosition=(
        0.109714, 0.0114057, 2.04726), cameraTarget=(0.109714, 0.0114057, 0))
    s2.autoTrimCurve(curve1=g[20], point1=(0.107623621821404, 0.00226069521158934))
    s2.autoTrimCurve(curve1=g[8], point1=(0.108205735683441, 0.00257786083966494))
    s2.autoTrimCurve(curve1=g[26], point1=(0.108258664608002, 0.00448085926473141))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04569, 
        farPlane=2.04882, width=0.0192928, height=0.0072613, cameraPosition=(
        0.106538, 0.00372789, 2.04726), cameraTarget=(0.106538, 0.00372789, 0))
    s2.autoTrimCurve(curve1=g[36], point1=(0.105749703943729, 0.0019005408976227))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.01773, 
        farPlane=2.07679, width=0.411663, height=0.154939, cameraPosition=(
        0.0813486, -0.0543682, 2.04726), cameraTarget=(0.0813486, -0.0543682, 
        0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0813486, 
        0.0259231, 2.04726), cameraTarget=(0.0813486, 0.0259231, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04204, 
        farPlane=2.05248, width=0.0643247, height=0.0242101, cameraPosition=(
        0.102983, 0.0519014, 2.04726), cameraTarget=(0.102983, 0.0519014, 0))
    s2.Arc3Points(point1=(0.105, 0.052), point2=(0.108, 0.04875), point3=(0.108, 
        0.0491757988929749))
    s2.CoincidentConstraint(entity1=v[48], entity2=g[17], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[49], entity2=g[35], addUndoState=False)
    s2.CoincidentConstraint(entity1=v[50], entity2=g[35], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04658, 
        farPlane=2.04794, width=0.00838244, height=0.00315493, cameraPosition=(
        0.108636, 0.0494493, 2.04726), cameraTarget=(0.108636, 0.0494493, 0))
    s2.autoTrimCurve(curve1=g[35], point1=(0.107980094850063, 0.0489740036427975))
    s2.autoTrimCurve(curve1=g[38], point1=(0.1079957857728, 0.0494441092014313))
    s2.undo()
    s2.autoTrimCurve(curve1=g[39], point1=(0.107974864542484, 0.0500604696571827))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04541, 
        farPlane=2.04911, width=0.0257404, height=0.00968801, cameraPosition=(
        0.110371, 0.0476158, 2.04726), cameraTarget=(0.110371, 0.0476158, 0))
    s2.autoTrimCurve(curve1=g[17], point1=(0.107183761894703, 0.0520267523825169))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.009, 
        farPlane=2.08552, width=0.533426, height=0.200767, cameraPosition=(
        0.276179, 0.0228949, 2.04726), cameraTarget=(0.276179, 0.0228949, 0))
    s2.Line(point1=(0.0334957117235445, 0.052), point2=(0.105, 0.052))
    s2.HorizontalConstraint(entity=g[41], addUndoState=False)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04267, 
        farPlane=2.05185, width=0.0565339, height=0.0212779, cameraPosition=(
        0.0182396, 0.00288255, 2.04726), cameraTarget=(0.0182396, 0.00288255, 
        0))
    s2.autoTrimCurve(curve1=g[11], point1=(0.00199884176254272, 
        0.00221320986747742))
    s2.autoTrimCurve(curve1=g[21], point1=(0.00245731882750988, 
        0.00200183968991041))
    s2.autoTrimCurve(curve1=g[28], point1=(0.00189303793013096, 
        0.00436213240027428))
    s2.autoTrimCurve(curve1=g[43], point1=(0.00450283847749233, 
        0.00214275345206261))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04574, 
        farPlane=2.04878, width=0.0187125, height=0.00704288, cameraPosition=(
        0.108076, 0.00371075, 2.04726), cameraTarget=(0.108076, 0.00371075, 0))
    s2.autoTrimCurve(curve1=g[4], point1=(0.110042631626129, 0.00195002579130232))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04562, 
        farPlane=2.0489, width=0.0201522, height=0.00758475, cameraPosition=(
        0.107076, 0.00280992, 2.04726), cameraTarget=(0.107076, 0.00280992, 0))
    s2.autoTrimCurve(curve1=g[27], point1=(0.108251266181469, 
        -0.00012854696251452))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.04421, 
        farPlane=2.05031, width=0.0425169, height=0.0160022, cameraPosition=(
        0.104956, 0.00513726, 2.04726), cameraTarget=(0.104956, 0.00513726, 0))
    s2.autoTrimCurve(curve1=g[47], point1=(0.110034808516502, 
        0.000474364031106234))
    s2.autoTrimCurve(curve1=g[5], point1=(0.109690003097057, 0.000103451777249575))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.02034, 
        farPlane=2.07418, width=0.375323, height=0.141262, cameraPosition=(
        0.212005, 0.0400451, 2.04726), cameraTarget=(0.212005, 0.0400451, 0))
    s2.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    p.features['Solid extrude-1'].setValues(sketch=s2)
    del mdb.models['Model-1'].sketches['__edit__']
    p = mdb.models['Model-1'].parts['Part-1']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Part-1']
    p.regenerate()
    p = mdb.models['Model-1'].parts['Part-1']
    p.regenerate()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54266, 
        farPlane=2.76591, width=1.24547, height=0.46876, cameraPosition=(
        -0.277817, -0.238863, 2.61352), cameraUpVector=(-0.284051, 0.913413, 
        -0.291532), cameraTarget=(0.0123749, -0.0387161, 0.438264), 
        viewOffsetX=0.0740709, viewOffsetY=0.0219614)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55552, 
        farPlane=2.75387, width=1.25585, height=0.472669, cameraPosition=(
        -0.216529, -0.0160728, 2.63883), cameraUpVector=(-0.280789, 0.883351, 
        -0.375299), cameraTarget=(0.00962239, -0.0438565, 0.447006), 
        viewOffsetX=0.0746883, viewOffsetY=0.0221445)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62413, 
        farPlane=2.68526, width=0.336121, height=0.126507, 
        viewOffsetX=0.122267, viewOffsetY=0.0430497)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63711, 
        farPlane=2.69083, width=0.338809, height=0.127519, cameraPosition=(
        -0.0121617, 0.065507, 2.66438), cameraUpVector=(-0.333911, 0.862021, 
        -0.381343), cameraTarget=(0.00681911, -0.0485283, 0.46378), 
        viewOffsetX=0.123245, viewOffsetY=0.043394)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)


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
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    p.PartitionFaceByAuto(face=f[23])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6425, 
        farPlane=2.68544, width=0.249472, height=0.0941296, 
        viewOffsetX=0.101755, viewOffsetY=0.039381)
    p = mdb.models['Model-1'].parts['Part-1']
    p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
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
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.unsetPrimaryObject()
    del mdb.models['Model-1'].sketches['__profile__']
    acis = mdb.openAcis(
        'C:/Users/touze/project/Shear_centre/reid_section/reid_sketch.sat', 
        scaleFromFile=OFF)
    mdb.models['Model-1'].ConstrainedSketchFromGeometryFile(name='reid_sketch', 
        geometryFile=acis)
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.sketchOptions.setValues(gridOrigin=(0.0550505816936493, 0.0270000007003546))
    s1.retrieveSketch(sketch=mdb.models['Model-1'].sketches['reid_sketch'])
    session.viewports['Viewport: 1'].view.fitView()
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s1, depth=1.0)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
