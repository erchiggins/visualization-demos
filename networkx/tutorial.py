import networkx as nx
import matplotlib.pyplot as plt

# https://networkx.github.io/documentation/networkx-1.10/tutorial/index.html

# undirected graph, no parallel edges or self-loops
G = nx.Graph()

# Digraph - directed Graph
# MultiGraph - undirected graph with parallel edges and self-loops
# DiMultiGraph - directed MultiGraph

# add single node
G.add_node(1)

# add nodes from list
# (or any nbunch (iterable container of nodes which is not itself a node) of nodes)
# can use any hashable object as a node, including another graph!
G.add_nodes_from([2, 3, 4, 5, 6, 7])
H = nx.path_graph(10)
# NOTE! duplicate nodes are ignored. Nodes 0-9 in this graph.
G.add_nodes_from(H)

# edges
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # asterisk unpacks edge tuple
# An ebunch is any iterable container of edge-tuples. An edge-tuple can be
# a 2-tuple of nodes or a 3-tuple with 2 nodes followed by an edge attribute
# dictionary, e.g. (2,3,{‘weight’:3.1415}).
# the path graph gives n nodes linearly connected by n-1 edges
G.add_edges_from(H.edges())
# once again, duplicates (this time for edges) are ignored!

# remove nodes and edges with
# .remove_node, .remove_nodes_from, .remove_edge, .remove_edges_from
# or remove all with .clear()

# strings count as an nbunch
# .add_nodes_from("spam") adds 4 new nodes

print(G.number_of_nodes())
print(G.number_of_edges())

print(G.nodes())
print(G.edges())
# list of neighbor nodes of node 3
print([n for n in G.neighbors(3)])

# "You might notice that nodes and edges are not specified as NetworkX objects.
# This leaves you free to use meaningful items as nodes and edges. The most
# common choices are numbers or strings, but a node can be any hashable object
# (except None), and an edge can be associated with any object x using
# G.add_edge(n1,n2,object=x)." HEYO

# directly access underlying dict with subscript notation
# do not change the returned dict! breaks consistency, potentially
print(G[2])  # {1: {}, 3: {}}
G.add_edge(2, 5)
G[2][5]['color'] = 'blue'
print(G[2])  # {1: {}, 3: {}, 5: {'color': 'blue'}}
# this shows you a dict representing the node's adjacency list

# layout is important, lots of options!
# https://networkx.github.io/documentation/stable/reference/drawing.html#module-networkx.drawing.nx_pylab
# nx.draw_networkx(G, pos=nx.circular_layout(G))
# plt.show()

# another example with weights and adjacency()
FG = nx.Graph()
# add nodes and edges at the same time!!
FG.add_weighted_edges_from(
    [(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
for n, neighbors in FG.adjacency():
    print(n, neighbors)
    for neighbor, edge_attr in neighbors.items():
        data = edge_attr['weight']  # grab edge weight
        if data < 0.5:
            print('(%d, %d, %.3f)' % (n, neighbor, data))

# nx.draw_networkx(FG, pos=nx.circular_layout(FG))
# plt.show()

# a note about attributes:
# "Attributes such as weights, labels, colors, or whatever Python object you like,
# can be attached to graphs, nodes, or edges.
# Each graph, node, and edge can hold key/value attribute pairs in an associated
# attribute dictionary (the keys must be hashable). By default these are empty, but
# attributes can be added or changed using add_edge, add_node or direct manipulation
# of the attribute dictionaries named G.graph, G.node and G.edge for a graph G."

# directed graphs
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
print(DG.out_degree(1, weight='weight'))
print(DG.degree(1, weight='weight'))
# like neighbors, but for directed graph
for successor in DG.successors(1):
    print(successor)
# the directed version of this does the same as successors() in order for algos to work correctly with it (ugh)
for neighbor in DG.neighbors(1):
    print(neighbor)
# https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.DiGraph.in_degree.html#networkx.DiGraph.in_degree

# nx.draw_networkx(DG, pos=nx.circular_layout(DG))
# plt.show()

# multigraphs
MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1,2,.5), (1,2,.75), (2,3,.5)])
for d in MG.degree(weight='weight'):
    print(d)
nx.draw_networkx(MG, pos=nx.circular_layout(MG))
# doesn't display parallel edges. Consider Graphviz as another solution. 
plt.show()