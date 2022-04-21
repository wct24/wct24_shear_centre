
# n1 = a.instances['box_beam-1'].nodes
# nodes1 = n1.getSequenceFromMask(mask=('[#0:187 #ffff0000 #ffffffff #fff ]', ), )
# a.Set(nodes=nodes1, name='loading_nodes')
# loading_nodes = a.allSets['loading_nodes'].nodes
# a = model.rootAssembly
# f1 = a.instances['box_beam-1'].elements
# face2Elements1 = f1.getSequenceFromMask(mask=('[#0:92 #fc000000 #ffffff ]', ), )
# a.Surface(face2Elements=face2Elements1, name='loading_surface')

# loading_surface = a.surfaces['loading_surface'].elements


# number_of_surfaces = len(loading_surface)
# print(number_of_surfaces)


# for i in range(number_of_surfaces):
#     surface = loading_surface[i]
#     a.SetFromElementLabels(elementLabels=((surface.instanceName, (surface.label,)),), name='loading-%s'%(i))

# for i in range(number_of_surfaces-1):
#     terms = [[1.0,'loading-%s'%(i), 6],[-1.0,'loading-%s'%(i+1), 6]]
#     model.Equation(name='loading_%s'%(i), terms=terms)



# # for i in range(number_of_nodes):
#     node = loading_nodes[i]
#     a.SetFromNodeLabels(nodeLabels=((node.instanceName, (node.label,)),), name='loading-%s'%(i))

# for i in range(number_of_nodes-1):
#     terms = [[1.0,'loading-%s'%(i), 2],[-1.0,'loading-%s'%(i+1), 2]]
#     model.Equation(name='loading_%s'%(i), terms=terms)

# n1 = a.instances['box_beam-1'].nodes
# # print(n1.coordinates)
# nodes1 = n1.getSequenceFromMask(mask=('[#0:187 #ffff0000 #ffffffff #fff ]', ), )
# a.Set(nodes=nodes1, name='loading_nodes')
# loading_nodes = a.allSets['loading_nodes'].nodes
# coordinate=loading_nodes[0].coordinates
# print(coordinate)
# print(coordinate[2])
# node1 = (loading_nodes[0],loading_nodes[1],)
# print(5)
# node = loading_nodes[0]
# a.SetFromNodeLabels(nodeLabels=((node.instanceName, (node.label,)),), name='loading-1')
# print(5)


# #number_of_nodes = len(loading_nodes)
# n1 = a.instances['box_beam-1'].nodes
