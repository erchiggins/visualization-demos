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
H=nx.path_graph(10)
G.add_nodes_from(H) #NOTE! duplicate nodes are ignored. Nodes 0-9 in this graph. 

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
print(G[2]) # {1: {}, 3: {}}
G.add_edge(2,5)
G[2][5]['color'] = 'blue'
print(G[2]) # {1: {}, 3: {}, 5: {'color': 'blue'}}
# this shows you a dict representing the node's adjacency list



# layout is important, lots of options!
# https://networkx.github.io/documentation/stable/reference/drawing.html#module-networkx.drawing.nx_pylab
nx.draw_networkx(G, pos=nx.circular_layout(G))
plt.show()
